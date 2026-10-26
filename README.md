# sast-sca-fp-test

A tiny deliberately-insecure Python app for exercising **both** false-positive
pipelines in one scan:

- **SAST** — each file under `app/` has one code pattern a SAST scanner
  (Semgrep/Opengrep) will flag.
- **SCA** — `requirements.txt` pins old, known-vulnerable dependency versions, so
  the SBOM/SCA scan finds CVEs to classify.

**Do not deploy. For security-tooling testing only.**

## SAST findings (app/)

| File | Pattern | Intent |
|------|---------|--------|
| app/sqli.py | SQL injection (string-formatted query) | true positive |
| app/cmdi.py | Command injection (shell + user input) | true positive |
| app/deserialize.py | Unsafe YAML/pickle load | true positive |
| app/ssrf.py | SSRF (user-controlled URL) | true positive |
| app/path_traversal.py | Path traversal (open user path) | true positive |
| app/secrets.py | Hardcoded password | true positive |
| app/weak_hash.py | MD5 used as a non-security cache key | likely false positive |
| app/eval_const.py | eval() of a hardcoded constant | likely false positive |

## SCA findings (requirements.txt)

Pinned vulnerable versions: `requests 2.19.1`, `PyYAML 5.1`, `Flask 0.12.2`,
`Jinja2 2.10`, `Werkzeug 0.14.1`, `urllib3 1.24.1`, `cryptography 2.3` — each
carries known CVEs for the SCA pipeline to analyze.
