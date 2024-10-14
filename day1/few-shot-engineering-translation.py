from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



prompt = """
Have you ever been to Paris? -> 파리에 가본 적 있어?
Sheep -> 양
Red -> 빨간색
Pencil -> 연필
Cat -> 고양이
Dog -> ?
"""

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
