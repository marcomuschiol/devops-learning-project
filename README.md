# DevOps Learning Project

Dieses Projekt ist ein lokales Multi-Container-System mit Docker Compose.

## Bestandteile

- nginx als Reverse Proxy
- Flask Backend API
- PostgreSQL Datenbank
- Docker Volumes für Persistenz
- Environment Variables über `.env`

## Architektur

Browser → nginx → backend → postgres

## Trigger CI

TEST

## Start

```bash
cd docker-website
docker compose up --build -d
