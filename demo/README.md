# Dropbase On-Prem Deployment Demo

No database? No problem.

To start your on-premises deployment with a demo database, run the following commanad from the repo root

```
docker compose -f docker-compose.demo.yml up
```

Once your worker is connected to the frontend, your demo db can be accessed from your client as a source name `dropbasedemodb` and will contain two example tables: `users` and `orders`
