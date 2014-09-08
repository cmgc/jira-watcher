from flask import render_template, url_for, redirect, request
from jira.client import JIRA
import sys, json
from config import USERNAME, PASSWORD, SERVER
from app import app
from models import getIssueByUser, getIssues, getIsuesS, getAllLeads

@app.route('/')
@app.route('/index')
def index():
  issues = getIssues()
  return render_template("index.html", server=SERVER, issues=issues)


@app.route('/lead')
def lead():
  with open('data.json', 'rb') as fp:
    leads = json.load(fp)
  return render_template("leads.html", leads=leads)

@app.route('/user/<username>')
def user(username):
  issues = getIssueByUser(username)
  return render_template("user.html",server=SERVER, name=username, issues=issues)

@app.route('/users')
def users():
  usernames = ['', '']
  return render_template("users.html", users=usernames)


@app.route('/f_update')
def f_update():
  data = getAllLeads()
  with open('data.json', 'wb') as fp:
    json.dump(data, fp)
  return "<b>Success!</b>"

@app.route('/test')
def test():
  tickets = getIsuesS()
  return render_template("test.html", server=SERVER, tickets=tickets)

@app.route('/is')
def test2():
  issues = getIssues()
  return str(issues)

@app.route('/help')
def help():
  links = {}
  for rule in app.url_map.iter_rules():
    links[rule.rule] = app.view_functions[rule.endpoint].__doc__
  return render_template("help.html", links=links)
