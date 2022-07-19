# PV_simulation

## Setup

Install system dependencies. This includes docker and docker-compose.
```
bash setup_system_dependencies.sh
```

Setup environment variables. Duplicate *.env_template* files and rename to *.env*:
- ./.env_template
- ./meter/.env_template
- ./pv_simulator/.env_template


## Run

Start containers using docker-compose:
```
bash start_docker.sh
```

Output will be written to file: *pv_simulator/log.dat*