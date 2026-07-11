# Assignment 38 - CodeLlama with Ollama

Features

- Generate Python code
- Explain existing code
- Debug code
- Optimize code

Technologies

- Ollama
- CodeLlama
- LangChain
- Streamlit

Run

Install dependencies

pip install -r requirements.txt

start the ollama using this command:

ollama serve

to run the application use this command:

python -m streamlit run app.py


"Hugging Face has updated its Space creation options. At the time of submission, Streamlit Spaces were not available in the free tier of my account. Therefore, the application was successfully deployed on Streamlit Community Cloud, while Hugging Face deployment could not be completed due to platform limitations"

I know how to deploy in hugging face and in the future I can pay the bill and deploy the application

https://codellama-with-ollama.streamlit.app/   

the above link address is came after the deployment on the streamlit. I used the Groq API creddentials and stored in the Streamlit secrets. 
The original application was built using Ollama and CodeLlama for local execution

For cloud deployment (Streamlit Community Cloud), the application was adapted to use the Groq API with the Llama 3.3 70B Versatile model as this change was necessary because Streamlit Cloud does not support running a local Ollama server

The application logic and features remain the same:
- Generate Code
- Explain Code
- Debug Code
- Optimize Code

GitHub repo link: https://github.com/DEVANAND-JAYARAMAN/GenAI-Asssignements-TuteDude/

screenshot is attached

I attempted to complete the Hugging Face Spaces deployment. However, on my account the Gradio and Docker SDKs require a PRO subscription, and only Static Spaces are available for free