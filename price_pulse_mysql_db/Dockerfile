# Use the MySQL 8.0 image as the base
FROM mysql:8.0

# Copy the initialization script into the image
COPY ./price_pulse_comparator.sql /docker-entrypoint-initdb.d/
