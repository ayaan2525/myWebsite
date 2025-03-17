import yaml
import os

# 1. Load the YAML data
with open("config.yaml", "r", encoding="utf-8") as f:
    resume_data = yaml.safe_load(f)

# 2. Construct the RST content
rst_content = f"""
{resume_data["name"]}'s Resume
{'=' * (len(resume_data["name"]) + 9)}

.. meta::
   :author: {resume_data["name"]}
   :description: Resume of {resume_data["name"]}

:Author: {resume_data["name"]}
:Email: {resume_data["email"]}
:LinkedIn: {resume_data["linkedin"]}
:GitHub: {resume_data["github"]}
:Location: {resume_data["location"]}

.. contents::
   :depth: 2
   :local:

About
-----
Email: {resume_data["email"]}
Location: {resume_data["location"]}
LinkedIn: {resume_data["linkedin"]}
GitHub: {resume_data["github"]}

Experience
----------
"""

# Add each experience entry
for job in resume_data.get("experience", []):
    rst_content += f"""
**{job["role"]}** at **{job["company"]}** ({job["duration"]})

- Skills: {", ".join(job.get("skills", []))}
"""

# Education Section
rst_content += "\nEducation\n---------\n"
for edu in resume_data.get("education", []):
    rst_content += f"""
**{edu["degree"]}** at **{edu["institution"]}** ({edu["duration"]})
"""

# Skills Section
rst_content += "\nSkills\n------\n"
skill_list = resume_data.get("skills", [])
if skill_list:
    rst_content += "- " + "\n- ".join(skill_list)

# Certifications Section
certs = resume_data.get("certifications", [])
if certs:
    rst_content += "\n\nCertifications\n-------------\n"
    for cert in certs:
        rst_content += f"""
- **{cert["name"]}**: {cert["link"]}
"""

# 3. Write the RST to docs/index.rst
os.makedirs("docs", exist_ok=True)
with open("docs/index.rst", "w", encoding="utf-8") as out_file:
    out_file.write(rst_content)

print("Successfully generated docs/index.rst from config.yaml!")
