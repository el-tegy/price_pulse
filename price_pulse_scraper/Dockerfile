FROM python:3.9-slim

LABEL authors="el-tegy"

# Set environment variables needed for poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /price_pulse/

# Install poetry
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock /price_pulse/

# Install project dependencies
RUN poetry config virtualenvs.create false&& \
    poetry install --no-dev --no-root

# Now, copy the current project contents into the container \
# at /price_pulse/
COPY . /price_pulse/

# Specify the default command to run scrapy
CMD ["scrapy", "list"]

