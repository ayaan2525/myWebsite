import yaml
from jinja2 import Environment, FileSystemLoader

# load yaml data
with open("config.yaml", "r") as file:
    resume_data = yanl.safe_load(file)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume_template.html")

output = template.render(resume=resume_data)

with open("docs/index.html", "w") as file:
    file.write(output)

print("Resume generated successfully")