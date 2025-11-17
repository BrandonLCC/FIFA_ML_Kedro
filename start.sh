# (no utilizado actualmente)
#Propositos: ejecutar airflow automaticamente
#Otros propositos: ...

#Documentacion: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

#!/bin/bash
set -e

COMMAND=$1

if [ "$COMMAND" = "airflow" ]; then
  docker-compose -f docker-compose.airflow.yml up -d
  echo "Airflow iniciado en http://localhost:8080"
else
  echo "Uso: ./start.sh airflow"
fi
