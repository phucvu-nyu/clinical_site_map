# Clinical Trials Interactive Map

An interactive web application for visualizing clinical trial locations globally. Uses the ClinicalTrials.gov API v2.

## Features
- Search clinical trials using expressions
- Interactive map visualization
- Filter trials by phase
- Detailed trial information on hover
- Responsive design

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python app.py
```
Or with gunicorn:
```bash
gunicorn -c gunicorn_config.py app:app
```

3. Visit http://localhost:5000 or http://localhost:8000 (if using gunicorn)

## Deployment
The application is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Tech Stack
- Flask
- Plotly
- ClinicalTrials.gov API v2
- Gunicorn