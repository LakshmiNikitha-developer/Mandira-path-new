import pandas as pd
from jinja2 import Template
import os

# Load ONLY South sheet from the same Excel file
df = pd.read_excel("data/north_temples.xlsx", sheet_name="south")

# Load HTML template
with open('temple-template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

# Output directory for South temples
output_dir = 'south/temples'
os.makedirs(output_dir, exist_ok=True)

# Generate pages
for _, row in df.iterrows():
    html = template.render(**row.to_dict())

    with open(f"{output_dir}/{row['FileName']}", 'w', encoding='utf-8') as f:
        f.write(html)

print("✅ South temple pages generated successfully!")
