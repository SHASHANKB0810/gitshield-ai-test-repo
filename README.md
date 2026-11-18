# GitShield AI – Security Scanner Test Repository

Synthetic, intentionally insecure repository for testing GitShield AI.

## Scanner coverage
- Bandit: eval, shell execution, unsafe deserialization, hard-coded password-like values
- Semgrep: SQL injection, command injection, unsafe YAML/pickle, disabled TLS verification
- Gitleaks: fake credential-like strings only
- pip-audit: deliberately outdated dependency pins

## Safety
All credentials are fabricated and non-functional. Do not replace them with real credentials.
Do not deploy this application or expose it to the internet. The examples are for static
analysis only; do not invoke the unsafe functions.

## Suggested workflow
1. Upload this ZIP's contents to a public test GitHub repository.
2. Submit that repository URL to GitShield AI.
3. Check repository discovery, scanner execution, file/line evidence, AI validation,
   severity classification, remediation suggestions, and verification status.
4. Exact finding counts can vary by scanner version and ruleset.

## Example scanner commands
```bash
bandit -r src -f json -o bandit-report.json
semgrep scan --config auto src --json --output semgrep-report.json
gitleaks detect --source . --no-git --report-format json --report-path gitleaks-report.json
pip-audit -r requirements.txt -f json
```
