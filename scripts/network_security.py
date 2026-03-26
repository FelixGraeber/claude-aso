"""Helpers for validating outbound HTTP targets."""

from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse


PUBLIC_SCHEMES = {"http", "https"}


def is_private_ip(hostname: str) -> bool:
    """Return True when the hostname is an internal-only IP literal."""
    try:
        ip = ipaddress.ip_address(hostname)
    except ValueError:
        return False
    return ip.is_private or ip.is_loopback or ip.is_reserved or ip.is_link_local


def hostname_matches(hostname: str, allowed_hosts: set[str]) -> bool:
    """Return True when hostname exactly matches or is a subdomain of an allowed host."""
    normalized = hostname.lower().rstrip(".")
    for allowed in allowed_hosts:
        allowed = allowed.lower().rstrip(".")
        if normalized == allowed or normalized.endswith(f".{allowed}"):
            return True
    return False


def validate_remote_url(
    url: str,
    *,
    allowed_hosts: set[str] | None = None,
    allow_private_hosts: bool = False,
) -> str:
    """Validate a remote URL before making a network request."""
    parsed = urlparse(url.strip())
    if parsed.scheme.lower() not in PUBLIC_SCHEMES:
        raise ValueError("Only http and https URLs are allowed")
    if not parsed.hostname:
        raise ValueError("URL must include a hostname")
    if parsed.username or parsed.password:
        raise ValueError("URLs with embedded credentials are not allowed")

    hostname = parsed.hostname
    if allowed_hosts and not hostname_matches(hostname, allowed_hosts):
        raise ValueError(f"Host '{hostname}' is not in the allowlist")

    if is_private_ip(hostname):
        raise ValueError(f"Host '{hostname}' resolves to a private IP")

    if allow_private_hosts:
        return url

    try:
        infos = socket.getaddrinfo(hostname, parsed.port or None, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise ValueError(f"Could not resolve hostname '{hostname}'") from exc

    for family, _, _, _, sockaddr in infos:
        candidate = sockaddr[0]
        try:
            ip = ipaddress.ip_address(candidate)
        except ValueError:
            continue
        if ip.is_private or ip.is_loopback or ip.is_reserved or ip.is_link_local:
            raise ValueError(f"Host '{hostname}' resolves to a private IP")

    return url
