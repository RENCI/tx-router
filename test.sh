#!/bin/bash
mkdir plugin.bak
mv plugin/* plugin.bak
docker-compose -f docker-compose.yml -f test/docker-compose.yml up --build -V --exit-code-from pds-backend-test
mv plugin.bak/* plugin
rm -r plugin.bak