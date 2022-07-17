#!/bin/bash
source .env
docker network create $PV_SIMULATION_NETWORK
docker stop pv-broker
docker rm pv-broker
docker run -d --hostname $RABBIT_MQ_HOSTNAME --name $RABBIT_MQ_HOSTNAME --net $PV_SIMULATION_NETWORK -e RABBITMQ_DEFAULT_USER=$RABBIT_MQ_USER -e RABBITMQ_DEFAULT_PASS=$RABBIT_MQ_PASSWORD -p $RABBIT_MQ_MANAGEMENT_PORT:15672 -p $RABBIT_MQ_PORT rabbitmq:3-management

cd meter
bash start_docker.sh

cd ..
cd pv_simulator
bash start_docker.sh