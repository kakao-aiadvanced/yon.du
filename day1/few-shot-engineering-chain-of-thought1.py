from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



prompt = """
fill the Step-by-step solution for the following problem:

# Simple - 1
Solve the following problem step-by-step: 23 + 47

Step-by-step solution:
1. Identify the numbers to be added: 23 and 47.
2. Align the numbers vertically by their place values:

   ```
     23
   + 47
   ```

3. Start adding from the rightmost column (the units place):
   - Units place: \( 3 + 7 = 10 \)
   - Write down 0 and carry over 1 to the next column.

4. Now add the tens place:
   - Tens place: \( 2 + 4 = 6 \)
   - Then add the carried over 1: \( 6 + 1 = 7 \)
   - Write down 7.

5. Combine the results from both columns:
   - The total is 70.

Answer: 70
"""

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
