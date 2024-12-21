# Rental Price Prediction API

## Overview
This microservice provides real-time rental price predictions through a RESTful API interface. Built with a production-grade MLOps architecture, it transforms a machine learning model into a scalable, maintainable API service.

## Architecture
The application follows a modular microservice architecture:

```
app/
├── api/               # API endpoint definitions
│   ├── prediction.py  # Prediction endpoints
│   └── __pycache__/
├── config/            # Configuration management
│   ├── __init__.py
│   ├── logger.py
│   └── model.py
├── logs/              # Application logs
├── model/             # ML model artifacts
├── schema/            # Data validation schemas
│   └── apartment.py
└── services/          # Business logic layer
    ├── model_inference.py
    └── run.py
```

## Technical Stack
- **Framework**: Flask
- **ML Model Serving**: Custom inference service
- **Data Validation**: Pydantic

## Development Tools
- **Poetry** (Dependency Management)
- **Ruff** (Code Quality)
- **GitHub Actions** (CI/CD)
- **Make** (Automation)

## Prerequisites
- Python 3.9+
- Poetry
- Make (optional)

## Installation

Clone the repository:
```bash
git clone https://github.com/Mohammed-abdulaziz-eisa/Rental-Price-Prediction-App-to-Micro-Transformation-API-Development.git
cd Rental Price Prediction App to Micro Transformation API Development
```

Install dependencies:
```bash
poetry install
```

Configure environment:
```bash
cp .env.example .env
# Edit .env with your configurations
```

## Usage

Start the API server:
```bash
poetry run python3 run.py
```
or 
```bash
make runner
# it will install dependencies and run the server
```

Make predictions:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "area": 85,
    "construction_year": 2015,
    "bedrooms": 2,
    "garden_area": 20,
    "balcony_area": 1,
    "parking_present": 1,
    "furnished": 0,
    "garage_present": 0,
    "storage_present": 1
  }'
```

## API Endpoints

### GET /pred
Predicts rental price based on apartment features.

**Request Body Schema:**
```json
{
    "area": int,
    "bedrooms": int,
    // Additional features as defined in schema/apartment.py
}
```

**Response:**
```json
{
    "predicted_price": float,
}
```

## Development

### Code Quality
The project uses Ruff for code formatting and linting:
```bash
poetry run ruff format .
poetry run ruff check .

# also you can use flake8 for linting 
poetry run flake8 .

```

### Testing
```bash
poetry run pytest
```

### Logging
Logs are stored in `app/logs/app.log` with the following levels:
- **INFO**: General application flow
- **WARNING**: Unexpected but handled situations
- **ERROR**: Application errors requiring attention
- **DEBUG**: Detailed information for development

## Deployment
The application is containerized and can be deployed using Docker:
```bash
docker build -t rental-price-api .
docker run -p 5000:5000 rental-price-api
```

## Monitoring
The application includes basic monitoring endpoints:
- `/health`: API health check
- `/metrics`: Basic performance metrics

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Contact
Mohamed-abdulaziz-eisa - [mohamed.abdulaziz.eisa@gmail.com]