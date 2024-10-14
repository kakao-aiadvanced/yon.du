from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



prompt = """
Convert the following natural language requests into SQL queries:
1. "Find employees with a salary greater than $50,000.": SELECT * FROM employees WHERE salary > 50000;
2. "Find products that are out of stock.": SELECT * FROM products WHERE stock = 0;
3. "Find students with a math score greater than 90.": SELECT name FROM students WHERE math_score > 90;
4. "Find orders from the last 30 days.": SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
5. "Count the number of customers in each city.": SELECT city, COUNT(*) FROM customers GROUP BY city;

Request: "Find the average salary of employees in the marketing department."
SQL Query:
"""

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
