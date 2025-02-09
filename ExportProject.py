import requests

projectsNameMapper = {}

def export(projectId, gitlabUrl, token):

    if projectId in projectsNameMapper:
        return projectsNameMapper[projectId]
    else:
        try:
            projectResponse=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}", headers={"PRIVATE-TOKEN":token})
            projectResponse.raise_for_status()
            
            jsonProjectResponse = projectResponse.json()
            projectsNameMapper[projectId] = jsonProjectResponse["name"] 
            print(f"create projectName cache to projectID={projectId}, projectName={projectsNameMapper[projectId]}")
            return projectsNameMapper[projectId]    
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)