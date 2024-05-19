import pathlib
import textwrap

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

with open("notes_api_key.txt", 'r') as f:
  GOOGLE_API_KEY = f.read()
  f.close()

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def notarize(transcript):
  prompt = """can you turn the following block of text into sections by topic, with headings and subheadings?:

  """ + transcript
  response = model.generate_content(prompt)
  return response.text

def summarize(transcript):
  prompt = """can you give a brief summary of the following block of text?:

  """ + transcript
  response = model.generate_content(prompt)
  return response.text
