# Test Flask App

A simple Flask web application with basic routing and templates.

## Features

- Home page with clean UI
- RESTful API endpoints
- JSON responses
- Environment variable support
- Ready for deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MeghVyas3132/test-flask-app.git
   cd test-flask-app
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/MacOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (optional):
   ```
   PORT=5000
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

- GET `/`: Home page with UI
- GET `/api/info`: API information and available endpoints
- GET `/api/data`: Sample data endpoint

## Deployment

This application can be easily deployed to platforms like:
- Heroku
- Railway
- Render
- DigitalOcean App Platform

## Requirements

See `requirements.txt` for a list of dependencies.