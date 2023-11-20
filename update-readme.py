import datetime

start_marker = "<!--START_SECTION:last-updated-->"
end_marker = "<!--END_SECTION:last-updated-->"

with open('README.md', 'r') as file:
    readme_content = file.read()

start_index = readme_content.find(start_marker) + len(start_marker)
end_index = readme_content.find(end_marker)

new_dynamic_content = "\nLast updated: " + str(datetime.datetime.now()) + "\n"

new_readme_content = readme_content[:start_index] + new_dynamic_content + readme_content[end_index:]

with open('README.md', 'w') as file:
    file.write(new_readme_content)
