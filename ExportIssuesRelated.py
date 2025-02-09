import requests
import csv
import ExportProject

def export(data, projectId, path, gitlabUrl, token, projectName):
    print(f"start export gitlab: issues vs issues, projectid={projectId}, data={data}")
    with open(f'{path}issues_origin_{projectId}_{data}.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(f'{path}issues_related_issues_{projectId}_{data}.csv', 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=',')
            writer.writerow(['project_name', 'id_issues_origin', 'id_issue_related', 'project_name_related'])
            count = 0
            for row in reader:
                issueIdOrigin = row["id"]                
                issuesRelatedResponse=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/issues/{issueIdOrigin}/links", headers={"PRIVATE-TOKEN":token})
                issuesRelated = issuesRelatedResponse.json()
                for issueRelated in issuesRelated:
                    projectIdRelated = issueRelated["project_id"]
                    projectNameRelated = ExportProject.export(projectIdRelated, gitlabUrl, token) 
                    writer.writerow([projectName, issueIdOrigin, issueRelated["iid"], projectNameRelated])