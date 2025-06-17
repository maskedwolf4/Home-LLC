# Home-LLC
This project is an Assessment Task from Home LLC

Set Up the Key in Your Project (.env file):

In the main folder of this project (where you see app.py and requirements.txt), create a new file named .env (make sure it starts with a dot!).
Open this .env file with a text editor and add the following line, replacing YOUR_GEMINI_API_KEY_HERE with the actual key you copied from the Groq console:
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
Important: Never share this .env file or your API key publicly! It's like your personal password for the AI service.

Running the Application Locally
Once you have everything set up, launching the app is simple:

Open Terminal/Command Prompt: Make sure you are in the project's main directory (the one containing app.py).

Run Streamlit:

Bash

streamlit run app.py

Access the App: Your web browser should automatically open a new tab showing the application (usually at http://localhost:8501). If not, copy and paste that address into your browser.
