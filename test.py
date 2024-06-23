import jenkins

folder_name = "org1"
server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='admin')

try:
    # Check if the job (folder) exists
    if server.job_exists(folder_name):
        print(f"Folder '{folder_name}' already exists.")
    else:
        print(f"Folder '{folder_name}' not found, creating...")
        server.create_job(folder_name, None)  # Create a job (folder)
        print(f"Folder '{folder_name}' created successfully.")
except jenkins.JenkinsException as e:
    print(f"Failed to check or create folder '{folder_name}': {str(e)}")
