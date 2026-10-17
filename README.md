# Graphql-CTF

[![GitHub](https://img.shields.io/badge/GitHub-Pytech04/Graphql--CTF-blue)](https://github.com/Pytech04/Graphql-CTF)
[![Focus](https://img.shields.io/badge/Focus-GraphQL%20Security-purple)](https://github.com/Pytech04/Graphql-CTF)
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20Flask-3776AB)](https://github.com/Pytech04/Graphql-CTF)
[![CTF](https://img.shields.io/badge/Category-API%20Security-red)](https://github.com/Pytech04/Graphql-CTF)

## Overview

Hands-on GraphQL API security CTF. Built with Flask, Graphene, and SQLAlchemy - practice introspection, authorization bypass, and common GraphQL attack vectors.

## Structure

- `app.py`, `main.py` - Flask app with GraphQL endpoint (`/graphql`, GraphiQL enabled)
- `schema.py` - GraphQL schema/queries/mutations
- `models.py` - Database models
- `seed.py` - Initial data
- `templates/` - Challenge UI

## Getting Started

```bash
git clone https://github.com/Pytech04/Graphql-CTF.git
cd Graphql-CTF
pip install -r requirements.txt
python main.py
```

Access: `http://localhost:5000` | GraphQL: `http://localhost:5000/graphql`

## Attack Vectors

- Introspection & schema enumeration
- Excessive data exposure / over-fetching
- Authorization bypass in resolvers
- Query depth/complexity abuses
- IDOR via GraphQL queries

## Tech Stack

- Flask + Flask-GraphQL + Graphene
- SQLAlchemy + SQLite
- Jinja2 templates

## Resources

- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PortSwigger GraphQL Labs](https://portswigger.net/web-security/graphql)

## Disclaimer

For educational and authorized CTF practice only.

## Author

[Pytech04](https://github.com/Pytech04)
