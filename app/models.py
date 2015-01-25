from app import app
from jira.client import JIRA
from config import SERVER, USERNAME, PASSWORD, S_JQL

options = {
    'server': str(SERVER)
}
jira = JIRA(options, basic_auth=(USERNAME, PASSWORD))

# get dict with issue.key:summary by provided JQL
def getIsuesS():
    issuesOnSupport = jira.search_issues(S_JQL)
    return dict(zip([issue.key for issue in issuesOnSupport],\
        [issue.fields.summary for issue in issuesOnSupport]))

# get list of all projects ( [[names, keys, leads], ...] )
def getAllLeads():
    projects = jira.projects()
    keys = [project.key for project in projects]
    names = [project.name for project in projects]
    leads = [jira.project(project.key).lead.displayName \
            for project in projects]
    result, i = [], 0
    mx = len(keys)
    while i < mx:
        result.append([names[i], keys[i], leads[i]])
        i += 1
    return result

# get issues by user where status in ( Open, "In Progress")
def getIssueByUser(username):
    issues = jira.search_issues('status in (Open, "In Progress") AND assignee in ('\
        + str(username)+ ')')
    return dict(zip([issue.key for issue in issues],\
        [issue.fields.summary for issue in issues]))

# get all keys of issues provided by JQL
def getIssues():
    issuesOnSupport = jira.search_issues(S_JQL)
    return [issue.key for issue in issuesOnSupport]

def assignToUser(S_JQL, user):
    issues = jira.search_issues(S_JQL)
    for issue in issues:
        jira.assign_issue(issue, user)
# function may be used throw jinja
#app.jinja_env.globals.update(getIssueByUser=getIssueByUser)

