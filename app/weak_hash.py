import hashlib


def cache_key(url: str) -> str:
    """LIKELY FALSE POSITIVE: MD5 here is only a cache-key digest, not security.

    Weak-crypto rules flag md5(), but no security property is relied on — it only
    produces a short, stable key for an in-memory cache."""
    return hashlib.md5(url.encode()).hexdigest()
