import yaml
import os
from jinja2 import Environment, FileSystemLoader

# Load YAML Data
with open("config.yaml", "r") as file:
    resume_data = yaml.safe_load(file)

# Ensure the docs directory exists
os.makedirs("docs", exist_ok=True)

# Load Jinja Template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume_template.html")

# Render HTML Page
output = template.render(resume=resume_data)

# Save Output
output_path = "docs/index.html"
with open(output_path, "w") as file:
    file.write(output)

print(f"Resume successfully generated at {output_path}")
