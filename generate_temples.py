import pandas as pd
from jinja2 import Template
import os

# Load Excel data
df = pd.read_excel("data/north_temples.xlsx")


# Load HTML template
with open('temple-template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

# Output directory
output_dir = 'north/temples'
os.makedirs(output_dir, exist_ok=True)

# Generate pages
for _, row in df.iterrows():
    html = template.render(**row.to_dict())

    with open(f"{output_dir}/{row['FileName']}", 'w', encoding='utf-8') as f:
        f.write(html)

print("✅ North temple pages generated successfully!")
