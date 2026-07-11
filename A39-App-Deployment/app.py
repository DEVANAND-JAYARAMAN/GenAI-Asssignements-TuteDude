import gradio as gr
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# function to get response
def get_response(task, user_input):

    prompts = {
        "Generate Code":
        f"""
Write Python code for the following requirement.

Requirement:
{user_input}

Return only the Python code with short comments.
""",

        "Explain Code":
        f"""
Explain the following Python code.

Code:
{user_input}
""",

        "Debug Code":
        f"""
Find and fix the errors in the following code.

Code:
{user_input}

Explain the changes.
""",

        "Optimize Code":
        f"""
Optimize the following Python code.

Code:
{user_input}

Improve readability and performance.
"""
    }

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",messages=[{"role": "user","content": prompts[task]}])
    return response.choices[0].message.content
demo = gr.Interface(
    fn=get_response,
    inputs=[
        gr.Dropdown(
            [
                "Generate Code",
                "Explain Code",
                "Debug Code",
                "Optimize Code"
            ],
            label="Task"
        ),
        gr.Textbox(
            lines=12,
            label="Enter Prompt or Code"
        )
    ],
    outputs=gr.Markdown(label="Response"),
    title="Code Assistant using Groq",
    description="Generate, Explain, Debug and Optimize Python code.")
demo.launch()