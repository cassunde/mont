import requests
import csv
import ExportProject

def export(data, projectId, path, gitlabUrl, token, projectName):
    print(f"start export gitlab: merges vs issues, projectid={projectId}, data={data}")
    with open(f'{path}merges_origin_{projectId}_{data}.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(f'{path}merges_related_{projectId}_{data}.csv', 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=',')
            writer.writerow(['projectName', 'id_merge', 'id_issues', 'project_name_issues_related'])
            for row in reader:
                merdeId = row["id"]
                issuesRelatedResponse=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/merge_requests/{merdeId}/closes_issues", headers={"PRIVATE-TOKEN":token})
                issuesRelated = issuesRelatedResponse.json()
                for issueRelated in issuesRelated:
                    projectIdRelated = issueRelated["project_id"]
                    projectNameRelated = ExportProject.export(projectIdRelated, gitlabUrl, token) 
                    writer.writerow([projectName, merdeId, issueRelated["iid"], projectNameRelated])