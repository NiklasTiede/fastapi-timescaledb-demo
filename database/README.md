
# Set up Database & Populate with Data

Spin up a timescaledb container locally:

```bash
docker pull timescale/timescaledb:latest-pg14

docker-compose-up -d
```

Execute the python script to populate the database with 
test data:

```bash
python generate_data.py
```
