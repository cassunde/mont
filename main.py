import ExportIssues
import ExportMerges
import ExportIssuesRelated
import datetime
import yaml
import sys
import ExportProject
import ExportIssuesMergesRelated

with open('config.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    
    gitlabUrl = data['gitlabUrl']
    daysToExport = data['daysToExport']
    exportProjectId = data['exportProjectId']
    dateType = data["dateType"]
    path = "exported/"
    token = sys.argv[1]

    today = datetime.date.today()
    time_delta = datetime.timedelta(days=daysToExport)
    exportDate = str(today - time_delta)

    print(f"Data export from gitlab: Host:{gitlabUrl}, start date={exportDate}, projectID={exportProjectId}")

    projectName = ExportProject.export(exportProjectId, gitlabUrl, token)

    ExportIssues.export(exportDate, exportProjectId, path, gitlabUrl, token, dateType, projectName)
    ExportIssuesRelated.export(exportDate, exportProjectId, path, gitlabUrl, token, projectName)
    ExportIssuesMergesRelated.export(exportDate, exportProjectId, path, gitlabUrl, token, projectName)
    ExportMerges.export(exportDate, exportProjectId, path, gitlabUrl, token, dateType, projectName)
    
    print("Finish")