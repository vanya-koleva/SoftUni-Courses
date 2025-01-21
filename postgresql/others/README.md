### Docker Workflow to Load Data from CSV into PostgreSQL

```bash
# List all running Docker containers
docker ps
# Copy the CSV file into the container
docker cp /path/to/your/file.csv <container_name>:/file.csv
# Open a Bash shell inside the container
docker exec -it <container_name> bash
# Connect to the database
psql -U <username> -d <database_name>
# Load data from the CSV file into the specified table
COPY your_table_name FROM '/file.csv' CSV HEADER;
```

