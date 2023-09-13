import requests
from github import Github

# GitHub credentials
github_username = "mrajiraji"
github_token = "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"
repo_name = "employee-data"

# Initialize a GitHub instance with your credentials
g = Github(github_username, github_token)

# Get the repository
repo = g.get_user().get_repo(repo_name)
# Create employee data
for employee_id in range(1, 11):
    employee_data = {
        "name": f"Employee {employee_id}",
        "department": f"Department {employee_id}",
        # Add other employee data fields as needed
    }
# Convert employee_data to a string (you can use any serialization format like JSON)
    employee_data_str = "\n".join([f"{key}: {value}" for key, value in employee_data.items()])

    # Create a file with the employee data
    file_name = f"employee_{employee_id}.txt"
    repo.create_file(file_name, f"Add data for Employee {employee_id}", employee_data_str)

print("Employee data created and pushed to the GitHub repository.")
