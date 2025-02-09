import requests
import csv

def export(data, projectId, path, gitlabUrl, token, dateType, projectName):
    print(f"start export gitlab: issues, projectid={projectId}, data={data}")

    with open(f'{path}issues_origin_{projectId}_{data}.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=',')
        writer.writerow([ 'Project Name', 'id', 'title', 'state', 'created_at','updated_at', 'closed_at', 'closed_by', 'milestone','author', 'assignee', 'time_estimate (seg)', 'total_time_spent (seg)', 'labels'])

        pagesToGet = 1
        totalPages = 1

        while pagesToGet <= totalPages :
            request=requests.get(f"{gitlabUrl}/api/v4/projects/{projectId}/issues?{dateType}={data}T00:00:00Z&page={pagesToGet}", headers={"PRIVATE-TOKEN":token})
            issues = request.json()
            totalPages = int(request.headers["X-Total-Pages"])
            writerRow(projectName, issues, writer)
            pagesToGet += 1
            
def writerRow (projectName, issues, writer) :
    for issue in issues:
            iid = issue["iid"]
            title = issue["title"]
            state = issue["state"]
            created_at = issue["created_at"]
            updated_at = issue["updated_at"]
            closed_at = issue["closed_at"]
            closed_by = ""
            if issue["closed_by"] is not None:
                closed_by = issue["closed_by"]["name"]
            time_estimate = ""
            if issue["time_stats"] is not None and issue["time_stats"]["time_estimate"] is not None: 
                time_estimate = issue["time_stats"]["time_estimate"]
            total_time_spent = ""
            if issue["time_stats"] is not None and issue["time_stats"]["total_time_spent"] is not None: 
                total_time_spent = issue["time_stats"]["total_time_spent"]
            milestone = ""
            if issue["milestone"] is not None and issue["milestone"]["title"] is not None: 
                milestone = issue["milestone"]["title"]
            author = ""
            if issue["author"] is not None and issue["author"]["name"] is not None: 
                author = issue["author"]["name"]
            assignee = ""
            if issue["assignee"] is not None and issue["assignee"]["name"] is not None: 
                assignee = issue["assignee"]["name"]            
            labels = ""
            if issue["labels"] is not None:
                labelsSeparater = ","
                labels = labelsSeparater.join(issue["labels"])
            
            writer.writerow([projectName, iid, title, state, created_at, updated_at, closed_at, closed_by, milestone, author, assignee, time_estimate, total_time_spent, labels])