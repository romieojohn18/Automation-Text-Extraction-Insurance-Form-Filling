# 1. Import the necessary libraries
import openai
import os
import pandas as pd
import time


# Import library
from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = PdfReader(open("D:\insurace\Automation\Sample data\Sample-Filled.pdf", "rb"))
                        

# Read all the pages in the PDF
pages = [pdf_file.pages[i] for i in range(len(pdf_file.pages))]

# Join all the pages into a single string
text = '\n'.join([page.extract_text() for page in pages])

# 1. Import the necessary libraries
import openai

# 2. Set your API key from ChatGPT account
api_key = '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'
openai.api_key = api_key

# 3. Define your text
text = """
This is the content of the document. It contains information about tenants, including their (1) First name, (2) last name, (3) date of birth, (4) address, and (5) phone number.
"""

# 4. Set up a function to get the result
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message["content"]

# 5. Create a prompt
question = "Read and understand the document. Extract the following information from the document:"
response = get_completion(question + text)
print(response)