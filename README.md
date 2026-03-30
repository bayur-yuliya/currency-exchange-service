# Currency Exchange Service

Production-like Django service for aggregating currency exchange rates from multiple providers, selecting the best available rate, and performing conversion calculations.

---

# Overview

This project demonstrates a backend system that:

* Collects exchange rates from multiple external APIs
* Normalizes and stores them in a unified format
* Selects the optimal rate for a given operation (buy/sell)
* Provides conversion functionality
* Runs background updates using Celery

The goal of this project is to showcase real-world backend development skills beyond basic CRUD applications.

---

#  Key Features

## Multi-provider integration

Supports multiple providers:

* Monobank
* PrivatBank
* NBU
* Minfin

Each provider is isolated and follows a unified interface.

---

## Background processing (Celery)

* Periodic tasks fetch fresh rates
* Decouples API calls from request lifecycle
* Improves performance and reliability

---

## Best rate selection

The system:

* Aggregates rates from all providers
* Chooses the most выгодный rate depending on operation type

---

## Test coverage

* Provider logic is tested
* External APIs are mocked using `responses`
* Ensures stability and predictable behavior

---

# Architecture

```
Providers (API clients)
        ↓
Normalization Layer
        ↓
Database (Rate model)
        ↓
Service Layer (business logic)
        ↓
Views / API
```

### Components

* **providers/** – integration with external APIs
* **models/** – database structure
* **services/** – business logic (rate selection, conversion)
* **tasks/** – Celery background jobs
* **views/** – HTTP layer

---

# How it works

1. Celery periodically fetches rates
2. Data is normalized and saved to DB
3. User requests conversion
4. Service selects best rate
5. Result is returned to user

---

# Tech Stack

* Python 3.11+
* Django
* Celery
* Redis (broker)
* PostgreSQL / SQLite
* Pytest
* responses (API mocking)

---

# Getting Started

## 1. Clone repo

```bash
git clone https://github.com/bayur-yuliya/currency-exchange-service
cd currency-exchange-service
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Apply migrations

```bash
python manage.py migrate
```

## 4. Run server

```bash
python manage.py runserver
```

## 5. Run Celery

```bash
celery -A config worker -l info
celery -A config beat -l info
```

---

# Example Use Case

User wants to convert USD → UAH:

* System fetches latest rates
* Finds best provider
* Calculates result
* Returns final amount

---

# Possible Improvements

* Add Django REST Framework API
* Introduce caching (Redis)
* Add Docker support
* Improve validation via Django Forms / DRF serializers
* Add rate history tracking

---

# Why this project matters

This project demonstrates:

* Working with external APIs
* Asynchronous task processing
* Testable architecture
* Separation of concerns
* Real-world backend patterns
