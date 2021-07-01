Setup db

```bash
docker-compose exec postgresql bash
psql -U postgres tms_dev < tms-backup-2.sql
```

Connect to the local db with a Visual viewer
```
Host: 127.0.0.1
User: postgres
Password: abcDEF123
Database: tms_dev
Port: 5433    ** NOT 5432
```
