price_pulse/
│
├── scraper/
│   ├── spiders/
│   │   ├── shopA_spider.py
│   │   └── shopB_spider.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
│
├── db_init/
│   ├── init.sql  # Script pour initialiser la BD
│   └── Dockerfile  # Image Docker personnalisée pour initialiser MySQL avec le script
│
├── docker-compose.yml
│
├── README.md
│
└── .gitignore
