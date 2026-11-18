# Test fixture map

This is a test oracle, not a guarantee that every tool/version reports every item.

| File | Pattern | Likely scanner |
|---|---|---|
| `src/app.py` | SQL assembled with an f-string | Semgrep |
| `src/app.py` | `subprocess` with `shell=True` | Bandit, Semgrep |
| `src/app.py` | `eval()` | Bandit |
| `src/app.py` | `pickle.loads()` | Bandit, Semgrep |
| `src/app.py` | YAML unsafe loader | Ruleset-dependent |
| `src/app.py` | TLS verification disabled | Semgrep |
| `src/app.py` | User-controlled path join | Ruleset-dependent |
| `src/app.py`, `src/secret_fixture.py` | Fake credential-like strings | Gitleaks |
| `requirements.txt` | Outdated packages | pip-audit |

## Validation controls
- `get_user_parameterized` is a safer SQL control and should not be called SQL injection merely because it accepts `user_id`.
- `compare_digest` is a safer comparison example.
- Credential fixtures are fake. Reports should identify locations without repeating secret values.
- Treat the toy `authenticate` function in context; it is not a real authentication system.
