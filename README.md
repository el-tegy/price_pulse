# price_pulse

> price_pulse: Giving you the heartbeat of pricing across sites 💰🤩💰😱.

PricePulse is a solution designed to scrape price data from e-commerce sites, consolidate the data, and provide a centralized view of product prices. Built with Docker, Scrapy, MySQL, and Kubernetes.

## ✨ Features

- **Price Scraping**: Harness the power of Scrapy to fetch and process price data.
- **Centralized Database**: Use a MySQL database to store and manage price data.
- **Easy Management**: PhpMyAdmin integration for better database management.
- **Containerized Solution**: Everything runs in Docker for isolated and reproducible runs.
- **Kubernetes Orchestration**: Efficiently manage, scale, and maintain the service using Kubernetes.

## 🚀 Quick Start

1. **Setup Kubernetes Cluster**: Ensure you have a running Kubernetes cluster.

2. **Clone the Repository**:
   ```bash
   git clone https://gitlab.com/el-tegy/pricepulse.git
   cd pricepulse
   ```

3. **Build Docker Images**: 
   ```bash
   docker-compose build
   ```

4. **Deploy to Kubernetes**:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   ```

## 🧱 Directory Structure

- `/scrapers`: Contains Scrapy spiders and scripts.
- `/database`: MySQL database schema and initialization scripts.
- `/kubernetes`: Kubernetes deployment configurations.
- `/docker`: Dockerfiles and related configurations.

## ✒️ Development

Details about setting up the development environment, coding standards, etc.

## 🔍 Testing

How to run unit tests and understand test coverage.

## 🚚 Deployment

Steps for deploying to a staging or production environment.

## 🫱🏻‍🫲🏽 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## ⚠️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
