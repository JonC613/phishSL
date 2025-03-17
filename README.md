# Phish.net API Integration

A Streamlit application for exploring Phish setlists and show information using the Phish.net API.

## Features

- View show information for any date from Phish's first show (December 2, 1983) up to 30 days in the future
- Display venue and location details
- Show complete setlists organized by sets
- Track song positions and transitions
- View special notes and footnotes

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd phishnet-api-viewer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows
source .venv/bin/activate     # On Unix/MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Phish.net API key:
     ```
     PHISHNET_API_KEY=your_api_key_here
     ```

5. Run the application:
```bash
streamlit run app.py
```

## Environment Variables

The following environment variables are required:

- `PHISHNET_API_KEY`: Your Phish.net API key

## Development

The project structure is organized as follows:

```
phishSL/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .env.example       # Example environment variables template
└── .gitignore         # Git ignore rules
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
