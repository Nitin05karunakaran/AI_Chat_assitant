## Python application that interacts with the OpenAI API to simulate a simple conversational agent.

## Setup and Installation

This project is configured to run in a Python 3.12 virtual environment (`venv`).

### 1. Activate the Virtual Environment

Depending on your operating system, run one of the following commands from the project root directory:

**On Linux/macOS:**

```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

---

# Create a .env file and add your openapi key there

OPENAI_API_KEY=your-key-here

# steps to create the key

visit https://cloud.boltiot.com create an account and then go to https://cloud.boltiot.com/apiDetails click on generate API key and save that key,now use it in the .env

## important commands to run-

# 2. pip install boltiotai

# 3. pip install python-dotenv

## Running the Tasks

Ensure your virtual environment is active before running any script.

### Task : run

```bash
python ai_assitant.py
```
