# price_pulse

> price_pulse: Giving you the heartbeat of pricing across sites 💰🤩💰😱.

PricePulse is a solution designed to scrape price data from e-commerce sites, consolidate the data, and provide a centralized view of product prices. Built with Docker, Scrapy, MySQL, and Docker Compose.

## ✨ Features

- **Price Scraping**: Harness the power of Scrapy to fetch and process price data.
- **Centralized Database**: Use a MySQL database to store and manage price data.
- **Easy Management**: PhpMyAdmin integration for better database management.
- **Containerized Solution**: Everything runs in Docker for isolated and reproducible runs.
- **Docker Compose**: Efficiently define, manage, and run application containers.

## 🚀 Quick Start

1. **Setup Kubernetes Cluster**: Ensure you have a running Kubernetes cluster.

2. **Clone the Repository**:
   ```bash
   git clone https://gitlab.com/el-tegy/pricepulse.git
   cd pricepulse
   ```

3. **Build and Run using Docker Compose**: 
   ```bash
   docker-compose up -d
   ```

4. **Accessing the Application**:
Open a browser and navigate to http://localhost:8080 to access phpMyAdmin.

5. **Stopping the Services**: 
   ```bash
   docker-compose down
   ```

## 🧱 Directory Structure

- `/scrapers`: Contains Scrapy spiders and scripts.
- `/db_init`: Contains initialization scripts for the MySQL database.
- `/docker-compose.yml`: Configuration file for Docker Compose to orchestrate the services.

## ✒️ Development

Details about setting up the development environment, coding standards, etc.

## 🔍 Testing

How to run unit tests and understand test coverage.

## 🚚 Troubleshooting

If you face any issues, please check the following:

   - Ensure all services are up by using `docker-compose ps`.
   - Check logs of a specific service: `docker-compose logs <service_name>` (e.g., `docker-compose logs mysql`).

## 🫱🏻‍🫲🏽 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## ⚠️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
