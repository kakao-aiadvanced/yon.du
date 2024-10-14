from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
