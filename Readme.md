# Poke-berries Statistics API

## Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables: Create a `.env` file with necessary configurations.
3. Run the application: `flask run`
4. Access the API at `http://127.0.0.1:5000/allBerryStats`

## Running it using docker:

1. Build the Docker image `docker build -t poke-berries-api .`
2. Run the Docker container `docker run -p 5000:5000 --env-file .env poke-berries-api`
   
## Testing

Run tests using pytest:

```bash
pytest test_app.py
```