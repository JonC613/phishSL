# phish_llm

A Python application to interact with Phish.net API and perform LLM-based analysis on Phish data.

## Setup

1. Clone the repository
2. Navigate to the project directory: `cd phish_llm`
3. Create and activate the virtual environment:
   ```
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the project root with:

```
BASE_URL=https://api.phish.net/v5
API_KEY=your_api_key_here
```

## Usage

(Documentation coming soon)

## Development

Run tests:
```
pytest
```

Format code:
```
black .
```

## License

MIT