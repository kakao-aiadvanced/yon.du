from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



prompt = """
The movie was terrible. -> negative
The acting was good. -> positive
The special effects were terrible. -> negative
The story was good, but the acting was terrible. -> negative
The sound was nice -> positive
The storyline was dull and uninspiring. -> ?
"""

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
