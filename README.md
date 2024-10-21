
# AI Voice Assistant with Llama and FastAPI (in progress)

This project is a simple AI voice assistant web application that uses a FastAPI back-end and a React front-end. The back-end processes user prompts through the local Llama model and returns responses to the front-end for display.

## Features

- User can submit text prompts via a web form.
- The prompt is sent to the FastAPI back-end, where it's processed by the Llama model.
- The response is displayed on the front-end.
- Input validation, error handling, and loading state are implemented.

---

## Project Structure

```bash
AI Voice Assistant/
├── FRONTEND/                # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/      # InputForm and ResponseDisplay Components
│   │   └── App.js           # Main React App
│   └── package.json         # Frontend dependencies
├── venv/                    # Python Virtual Environment
├── main.py                  # FastAPI Backend
├── requirements.txt          # Backend dependencies
└── README.md                # Project Documentation
```

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Node.js** (for React frontend)
- **Virtual Environment** (venv)
- **Ollama** (for running Llama locally)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-voice-assistant.git
   cd ai-voice-assistant
   ```

2. **Set Up Back-End (Python + FastAPI)**

   - Create a virtual environment:
   
     ```bash
     python -m venv venv
     source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
     ```

   - Install back-end dependencies:
   
     ```bash
     pip install -r requirements.txt
     ```

   - Start the FastAPI back-end:
   
     ```bash
     uvicorn main:app --reload
     ```

3. **Set Up Front-End (React)**

   Navigate to the `FRONTEND` folder and install the front-end dependencies:

   ```bash
   cd FRONTEND
   npm install
   ```

   Start the front-end development server:

   ```bash
   npm start
   ```

   The front-end will run on `http://localhost:3000`.

---

## Usage

1. Navigate to `http://localhost:3000` in your browser.
2. Enter a prompt in the input field and click **Submit**.
3. The back-end will process the prompt using the Llama model and return a response that is displayed on the front-end.

---

## API Endpoints

- **GET /** - Returns a welcome message.
- **POST /process-text** - Accepts a JSON object with a `prompt` field, processes it using the Llama model, and returns the response.

### Example Request

```json
POST /process-text
{
  "prompt": "Explain Python classes."
}
```

---

## Contributing

Feel free to submit pull requests, report issues, or suggest features. Contributions are always welcome!
