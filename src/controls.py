"""Safer comparison examples for false-positive validation."""

import sqlite3
import hashlib
import hmac


def get_user_parameterized(user_id: str):
    """Parameterized SQL: should not be flagged as SQL injection."""
    connection = sqlite3.connect(":memory:")
    return connection.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,),
    ).fetchall()


def compare_digest(candidate: str, expected_digest: str) -> bool:
    """Constant-time comparison example."""
    candidate_digest = hashlib.sha256(candidate.encode("utf-8")).hexdigest()
    return hmac.compare_digest(candidate_digest, expected_digest)
