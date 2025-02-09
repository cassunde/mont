import requests
import csv

def export(data, projectId, path, gitlabUrl, token, dateType, projectName):
    print(f"start export gitlab: merges, projectid={projectId}, data={data}")
    r=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/merge_requests?{dateType}={data}T00:00:00Z", headers={"PRIVATE-TOKEN":token})
    issues = r.json()
    totalPages = r.headers["X-Total-Pages"]

    with open(f'{path}merges_origin_{projectId}_{data}.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=',')
        writer.writerow(['projectName','id', 'title', 'state', 'created_at','updated_at', 'merged_by', 'merged_at','assignee', 'time_estimate (seg)', 'total_time_spent (seg)'])
        
        for issue in issues:
            iid = issue["iid"]
            title = issue["title"]
            state = issue["state"]
            created_at = issue["created_at"]
            updated_at = issue["updated_at"]
            merged_by = ""
            if issue["merged_by"] is not None and issue["merged_by"]["name"] is not None:
                merged_by = issue["merged_by"]["name"]
            time_estimate = ""
            if issue["time_stats"] is not None and issue["time_stats"]["time_estimate"] is not None:
                time_estimate = issue["time_stats"]["time_estimate"]
            total_time_spent = ""
            if issue["time_stats"] is not None and issue["time_stats"]["total_time_spent"] is not None:
                total_time_spent = issue["time_stats"]["total_time_spent"]
            merged_at = issue["merged_at"]
            assignee = ""
            if issue["assignee"] is not None:
                assignee = issue["assignee"]["name"]

            writer.writerow([projectName, iid, title, state, created_at, updated_at, merged_by, merged_at, assignee, time_estimate, total_time_spent])
            
        if int(totalPages) > 1:
            pagesToGet = 2
            while pagesToGet <= int(totalPages) :
                responseInterator=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/merge_requests?{dateType}={data}T00:00:00Z&page={pagesToGet}", headers={"PRIVATE-TOKEN":token})
                issuesInterator = responseInterator.json()
                for issueInterator in issuesInterator:
                    iid = issueInterator["iid"]
                    title = issueInterator["title"]
                    state = issueInterator["state"]
                    created_at = issueInterator["created_at"]
                    updated_at = issueInterator["updated_at"]
                    merged_by = ""
                    if issueInterator["merged_by"] is not None and issueInterator["merged_by"]["name"] is not None:
                        merged_by = issueInterator["merged_by"]["name"]
                    time_estimate = ""
                    if issueInterator["time_stats"] is not None and issueInterator["time_stats"]["time_estimate"] is not None:
                        time_estimate = issueInterator["time_stats"]["time_estimate"]
                    total_time_spent = ""
                    if issueInterator["time_stats"] is not None and issueInterator["time_stats"]["total_time_spent"] is not None:
                        total_time_spent = issueInterator["time_stats"]["total_time_spent"]
                    merged_at = issueInterator["merged_at"]
                    assignee = ""
                    if issueInterator["assignee"] is not None and issueInterator["assignee"]["name"] is not None :
                        assignee = issueInterator["assignee"]["name"]

                    writer.writerow([projectName, iid, title, state, created_at, updated_at, merged_by, merged_at, assignee, time_estimate, total_time_spent])
                        
                pagesToGet += 1