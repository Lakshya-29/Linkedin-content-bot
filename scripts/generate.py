import os
from datetime import date
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = """
Write a professional LinkedIn article about AI,
Cybersecurity, Programming, Student Growth,
IIT internships, or Technology Trends.

Length: 500-700 words
Include:
- Title
- Introduction
- Key Learnings
- Conclusion
- Engagement Question
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

os.makedirs("articles", exist_ok=True)

filename = f"articles/{date.today()}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print("Article created:", filename)
