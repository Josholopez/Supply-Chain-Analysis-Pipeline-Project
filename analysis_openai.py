import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    )
# load the dataset from kaggle
df = pd.read_csv("supply_chain_data.csv")

# sample data
sample = df.head(20).to_csv(index=False)

prompt = f"""
You are a data analyst. Summarise this dataset clearly.
Dataset sample (first 20 rows):
{sample}
Respond with:
1. High-level description of what the dataset contains.
2. Key columns and their meaning.
3. Data quality issues (missing values, duplicates, outliers).
"""
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}]
)

#Extract message text
summary_md = response.choices[0].message.content

#Save as Markdown file
with open("dataset_summary.md", "w", encoding="utf-8") as f:
    f.write(summary_md)

print(summary_md)
print("Markdown summary saved as dataset_summary.md.")
