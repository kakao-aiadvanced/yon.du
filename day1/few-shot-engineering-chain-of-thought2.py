from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



prompt = """
fill the Step-by-step solution for the following problem:

# Simple - 2
Solve the following problem step-by-step: 123 - 58

Step-by-step solution:
1. **Write the numbers vertically aligned by place value:**
   ```
     123
   -  58
   ```

2. **Subtract the ones place (rightmost digits):**
   - From 3 (ones) subtract 8 (ones).
   - Since 3 is less than 8, we need to borrow from the 2 (tens).
   - Borrow 1 ten (making it 1) and add 10 to the 3 (making it 13).
   - Now, subtract: 13 - 8 = 5.

3. **Subtract the tens place:**
   - After borrowing, we have 1 (from the original 2) in the tens place and we need to subtract 5 from it.
   - Since 1 is less than 5, we need to borrow again from the 1 in the hundreds place (making it 0).
   - So, we take 10 from the hundreds place, making the tens place 11.
   - Now, subtract: 11 - 5 = 6.

4. **Subtract the hundreds place:**
   - Now, we have 0 (from the original 1) and we subtract 0 from it.
   - So, 0 - 0 = 0.

Combining all the results from each place value, we have:
```
    123
   - 58
   -----
     65
```

Answer: 65
"""

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
