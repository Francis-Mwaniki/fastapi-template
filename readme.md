# Fastapi folder structure

my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   └── route_files.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── model_files.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schema_files.py
│   └── services/
│       ├── __init__.py
│       └── service_files.py
├── tests/
│   ├── __init__.py
│   └── test_files.py
├── alembic/
│   └── versions/
├── .env
├── .gitignore
├── requirements.txt
└── README.md