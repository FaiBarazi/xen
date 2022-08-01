FROM postgres:13-alpine3.16
# Copying dump to this location to auto run the initdb script.
# and build the DB. This is a feature of the postgres image.
COPY rates.sql /docker-entrypoint-initdb.d/
