#!/bin/sh
set -e

# Espera o banco (simples) tentando conectar antes de executar migrate
echo "Waiting for database to be ready..."
attempts=0
until python manage.py showmigrations > /dev/null 2>&1 || [ $attempts -ge 20 ]; do
  attempts=$((attempts+1))
  echo "Database not ready yet (attempt $attempts/20). Sleeping..."
  sleep 2
done

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files (noinput)..."
python manage.py collectstatic --noinput || true

echo "Starting server..."
exec "$@"
