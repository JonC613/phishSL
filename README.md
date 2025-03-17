# Phish.net Setlist Explorer

A Streamlit application that allows you to explore Phish setlists and show information using the Phish.net API v5.

## Features

- Interactive calendar to select dates
- Display of show information including venue and location
- Detailed setlist information with song titles, durations, and notes
- Support for historical shows from 1983 to present
- Support for upcoming shows

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Create a `.env` file in the root directory with your Phish.net API key:
   ```
   API_KEY=your_api_key_here
   ```
   If no API key is provided, the app will use a default key.

## Running the App

To run the Streamlit app, execute:
```bash
streamlit run app.py
```

The app will open in your default web browser. You can then:
1. Select any date from the calendar
2. View show information including venue and location
3. Explore the complete setlist for that show

## API Documentation

This app uses the Phish.net API v5. For more information about the API, visit:
https://api.phish.net/v5/doc/
