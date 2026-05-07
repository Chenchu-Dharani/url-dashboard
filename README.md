# VBO Dashboard

A simple Flask web dashboard to manage and navigate internal service URLs across multiple environments (Common, LAB, PROD).

## Features

- 🌐 Grouped environments (Lab AWS, Lab ECX, Lab Cloud, Prod AWS, Prod Cilium, Prod Cloud, Prod Lite)
- 🔍 Live search across all services
- 📌 Pin frequently used services to the top
- 🌙 Dark mode toggle
- 📱 Responsive layout

## Setup

1. Clone the repo and create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your service URLs in the `config/` folder:
   - `config/common.py` — shared services (wiki, Jira, SSO, etc.)
   - `config/lab.py` — LAB environment services
   - `config/prod.py` — PROD environment services
   - `config/password_reset.py` — password reset links

4. Run the app:
```bash
python app.py
```

5. Open your browser at: http://localhost:5000

## Configuration

Each service entry in the config files follows this structure:

```python
{
    "name": "Service Name",
    "url": "https://your-service.example.com/",
    "image": "static/logos/service-logo.png",  # optional
    "icon": "📊"                                 # emoji fallback
}
```

Add your own logo images to `static/logos/` and reference them in the config.

## Project Structure

```
vbo_dashboard/
├── app.py                  # Flask app entry point
├── requirements.txt
├── config/
│   ├── __init__.py
│   ├── common.py
│   ├── lab.py
│   ├── prod.py
│   └── password_reset.py
├── templates/
│   └── dashboard.html
└── static/
    ├── css/styles.css
    ├── js/script.js
    └── logos/              # Add your service logos here
```
