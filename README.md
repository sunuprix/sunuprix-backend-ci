# SunuPrix - Backend (`sunuprix-backend-ci`)

API REST de **SunuPrix**, plateforme de consultation et de comparaison des prix observes dans les marches senegalais.
Ce depot correspond au depot `backend-ci` de l'enonce : il contient le code de l'API, les tests, le Dockerfile et le pipeline CI.

## Stack
FastAPI, PostgreSQL, pytest, Docker, GitHub Actions.

## Lancer en local
```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell : .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn src.main:app --reload
```
- API : http://localhost:8000
- Documentation Swagger : http://localhost:8000/docs
- Health check : http://localhost:8000/health

## Tests
```bash
pytest -v
```

## Docker
```bash
docker build -t sunuprix-backend .
docker run -p 8000:8000 sunuprix-backend
```

## Pipeline CI (`.github/workflows/ci.yml`)
Declenchement : push sur `main` et Pull Requests.

1. Checkout du code
2. Installation de Python et des dependances
3. Tests unitaires (pytest)
4. Build de l'image Docker
5. Push sur Docker Hub (uniquement apres un push sur `main`)

Le job s'appelle `build` : ce nom est exige par la regle de protection de `main`.

### Secrets GitHub requis
| Secret | Role |
|---|---|
| `DOCKERHUB_USERNAME` | compte Docker Hub du projet |
| `DOCKERHUB_TOKEN` | access token Docker Hub (droits Read & Write) |

## Image Docker
- Depot Docker Hub : `<DOCKERHUB_USERNAME>/sunuprix-backend` (lien a ajouter)
- Tags : SHA court du commit (ex. `a1b2c3d`) et `latest`. Le deploiement reference toujours le SHA.
- Port expose : `8000`, sonde de sante : `GET /health`

## Variables d'environnement
| Variable | Role | Defaut |
|---|---|---|
| `CORS_ORIGINS` | origines autorisees, separees par des virgules | `*` |

## Workflow Git
Branche (`feat/...`, `fix/...`, `docs/...`), Pull Request, relecture par un autre membre, fusion. Pas de push direct sur `main`.

## Equipe
Binome backend (B1) : Loubano-Voumbi Jordie, Ryghen Michel Valdick Mbenangoye.
CI : binome B3.
