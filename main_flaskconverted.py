from flask import Flask, abort
import Database.Worker_DBConfig as WorkerDB
import os

## Web Prepends

import Prepends.Prepend as Prepends

## Web Page Templates

import Pages.home as Home
import Pages.PageNotFound as PageNotFound
import Pages.contact as ContactUs
import Pages.reportIssue as ReportIssue

## Worker Table

import Components.workers_table as WorkerTable

## Compoennts

import Components.table as Table

## Stylesheet

Stylesheet = open("stylesheet.css").read()

## Internal

"""
print(f"{'Name':25}|{'Emplyee Num':11}|{'Office Num':10}|{'Hours Worked':12}|{'Overtime':8}|{'Estimated Pay':10}")
print("------------------------------------------------------------------------------------")


print(Home.Render(Table.RenderTable(WorkersToRenderTable, [
        'Name',
        'Employee Num',
        'Office Num',
        'Hours Worked',
        'Overtime Hours',
        'Estimated Pay'
    ])))

"""

## Flask App
app = Flask(__name__)

def base_page():
    return f"<html><head><title>HR Dashboard</title><style>{Stylesheet}</style></head><body>{Prepends.RenderHeader()}"

@app.route('/')
def home():
    page = base_page()
    page += f"{Home.Render(WorkerTable.RenderWorkerTable())}"
    page += "</body></html>"
    return page, 200

@app.route('/contact-us')
def contact():
    page = base_page()
    page += f"{ContactUs.RenderPage()}"
    page += "</body></html>"
    return page, 200

@app.route('/report-issue')
def report_issue():
    page = base_page()
    page += f"{ReportIssue.RenderPage()}"
    page += "</body></html>"
    return page, 200

@app.errorhandler(404)
def not_found(e):
    page = base_page()
    page += f"{PageNotFound.Render('')}"
    page += "</body></html>"
    return page, 404
            