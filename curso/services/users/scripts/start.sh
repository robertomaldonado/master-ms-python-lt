#!/usr/bin/env bash

echo "Starting server..."
echo "PORT: $PORT"
echo "CORES: $CORES"

uvicorn src.main:app --host 0.0.0.0 --port "$PORT" --workers "$CORES" --log-level debug
