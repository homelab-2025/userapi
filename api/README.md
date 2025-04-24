# Userapi

Small API used to try out mongodb

## Prerequisites

- Docker Desktop

## Getting started

1. Create Docker Network

```bash
docker network create shared
```

2. Start mongodb

```bash
cd /db/single-node/
docker compose up -d
```

3. Start fastapi

```bash
cd ../../api
docker compose up -d
```