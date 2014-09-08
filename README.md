# Web app for watching tickets in JIRA
Using jql you can watch statuses, assignee, etc. of tickets
webapp uses microframework [flask][1] and [jira-python][2] library for watching statuses, assignees, etc.
It's a very simple project and it is not finished yet, but works fine as is. New features will be added in future.

# Installation

Download and install using pip:
  pip install jira-python
  pip install flask
You can also use [virtualenv][3]
clone git rep into your directory:
  git clone https://github.com/cmgc/jira_watcher.git

# Quickstart

1. Enter servername, and your credentials for accessing jira in config.py file.
   (also you can add jira sql in config.py which will be used in future)
2. just run it:
  $ nohup python run.py &
3. list of available actions:
  - /user/<username> - to get all tickets assigned to <username>
  - /lead - to get leads of all projects. Can be accessed only after /f_update
    which will update data.json file
  - /help  - to get list all actions
..

# useful things:
 you can use sample.html as example how to monitor tickets.
[1]: http://flask.pocoo.org/
[2]: http://jira-python.readthedocs.org/
[3]: http://virtualenv.org/en/latest/index.html
