Setup db

```bash
docker-compose exec postgresql bash
psql -U postgres tms_dev < tms-backup-1.sql
```

Connect to the local db with a Visual viewer
```
Host: 127.0.0.1
User: postgres
Password: abcDEF123
Database: tms_dev
Port: 5433    ** NOT 5432
```

Debug
stop all running heroku processes - then ensure the last line of the docker file is set to sleep forever:

```docker
CMD [ "tail", "-f", "/dev/null" ]
```

then place breakpoint(); where necessary in the app, then

```bash
docker-compose exec app bash
gunicorn -b 0.0.0.0:5000 unit_log.wsgi --log-file -
```