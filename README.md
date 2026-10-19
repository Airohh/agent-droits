# agent-droits

[![CI](https://github.com/Airohh/agent-droits/actions/workflows/ci.yml/badge.svg)](https://github.com/Airohh/agent-droits/actions/workflows/ci.yml)

Agent IA qui collecte les faits d'un foyer, calcule ses droits (aide au logement, prime d'activité, RSA, impôt) avec OpenFisca, cite les textes officiels, et dont la fiabilité est mesurée.

**Règle d'or : aucun montant ne vient du modèle.** Chaque chiffre de la réponse sort d'un appel à OpenFisca, et un contrôle automatique le vérifie.

*En cours de construction. Étape 0 (socle du dépôt) faite le 19/10/2026.*

## Feuille de route

| # | Étape | Technologies | État |
|---|---|---|---|
| 0 | Socle du dépôt | uv, ruff, pytest, pre-commit, GitHub Actions, Docker | ✅ |
| 1 | Outil de calcul en serveur MCP | OpenFisca-France 176.1.0, Pydantic v2, FastMCP | |
| 2 | Boucle d'agent écrite à la main | API compatible OpenAI (OpenRouter), client MCP | |
| 3 | Agent LangGraph | LangGraph, langchain-mcp-adapters, checkpointer, human-in-the-loop | |
| 4 | Évaluations | Inspect AI, utilisateur simulé, LLM-juge validé par kappa | |
| 5 | Observabilité | Langfuse, OpenTelemetry | |
| 6 | Garde-fous | contrôle déterministe des montants, tests d'injection, budgets | |
| 7 | API, interface, déploiement, CI d'éval | FastAPI (SSE), Chainlit, Docker Compose | |
| 8 | Résultats et démo | | |

L'outil de recherche des textes officiels est [insight-mcp](https://github.com/Airohh/insight-mcp).

## Lancer en local

```bash
uv sync                          # crée .venv et installe les dépendances (Python 3.12)
uv run pytest -q                 # tests
uv run ruff check . && uv run ruff format --check .
uv run pre-commit install        # une fois : lint et format à chaque commit
```

## Structure

| Dossier | Rôle | Étape |
|---|---|---|
| `src/agent_droits/outils/` | Serveur MCP `openfisca-mcp` | 1 |
| `src/agent_droits/agent/` | Boucle v0, puis graphe LangGraph | 2-3 |
| `src/agent_droits/garde_fous/` | Contrôle des montants, validation, budgets | 6 |
| `src/agent_droits/api/` | FastAPI en streaming | 7 |
| `evals/` | Tâches Inspect AI, jeux, résultats | 4 |
| `ui/` | Interface Chainlit | 7 |
| `tests/` | Tests pytest | toutes |

CI GitHub Actions : `uv sync --locked`, ruff (lint + format), pytest, puis build de l'image Docker.

## Avertissement

Les montants calculés sont indicatifs : ce ne sont pas des décisions de la CAF ni de l'administration fiscale. Pour une démarche, utiliser [mesdroitssociaux.gouv.fr](https://www.mesdroitssociaux.gouv.fr) et [impots.gouv.fr](https://www.impots.gouv.fr).
