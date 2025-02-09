import requests
import csv
import ExportProject

def export(data, projectId, path, gitlabUrl, token, projectName):
    print(f"start export gitlab: issues vs merges, projectid={projectId}, data={data}")
    with open(f'{path}issues_origin_{projectId}_{data}.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(f'{path}issues_related_merges_{projectId}_{data}.csv', 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=',')
            writer.writerow(['project_name', 'id_issues_origin', 'id_merge_related', 'project_name_merge_related'])
            count = 0
            for row in reader:
                issueIdOrigin = row["id"]                
                mergesRelatedResponse=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/issues/{issueIdOrigin}/related_merge_requests", headers={"PRIVATE-TOKEN":token})
                mergesRelated = mergesRelatedResponse.json()
                for mergeRelated in mergesRelated:
                    projectIdRelated = mergeRelated["project_id"]
                    projectNameRelated = ExportProject.export(projectIdRelated, gitlabUrl, token) 
                    idMergeRelated = mergeRelated["iid"]
                    writer.writerow([projectName, issueIdOrigin, idMergeRelated, projectNameRelated])