"""Synthetic static-analysis fixtures. Do not deploy or run."""

import os
import pickle
import subprocess
import sqlite3
import yaml
import requests

# Fake, non-functional token-shaped fixture for Gitleaks.
GITHUB_TOKEN = "ghp_0000000000000000000000000000000000000000"
DATABASE_PASSWORD = "test-password-do-not-use"


def get_user_unsafe(user_id: str):
    """SQL injection candidate: user input interpolated into SQL."""
    connection = sqlite3.connect(":memory:")
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return connection.execute(query).fetchall()


def run_command_unsafe(filename: str):
    """Command injection candidate: shell command includes caller input."""
    command = "cat " + filename
    return subprocess.check_output(command, shell=True)


def evaluate_expression_unsafe(expression: str):
    """Dangerous dynamic evaluation."""
    return eval(expression)


def load_object_unsafe(payload: bytes):
    """Unsafe pickle deserialization."""
    return pickle.loads(payload)


def parse_yaml_unsafe(payload: str):
    """Unsafe YAML loader example; rule coverage varies."""
    return yaml.load(payload, Loader=yaml.Loader)


def request_without_tls_verification(url: str):
    """TLS certificate verification is disabled."""
    return requests.get(url, verify=False, timeout=5)


def read_path_unsafe(user_supplied_path: str):
    """Path traversal candidate: user input is joined without validation."""
    root = "/tmp/gitshield-test-files"
    return open(os.path.join(root, user_supplied_path), "r", encoding="utf-8").read()


def authenticate(username: str, password: str):
    """Toy control example; not a production authentication implementation."""
    expected_username = "demo"
    expected_password = "not-a-real-password"
    return username == expected_username and password == expected_password
