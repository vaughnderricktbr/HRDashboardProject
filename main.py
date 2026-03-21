import http.server
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

PORT = 8050

## Server

def main():
    class Server(http.server.BaseHTTPRequestHandler):
        def do_GET(self):

            page_render = f"<html><head><title>HR Dashboard</title><style>{Stylesheet}</style></head><body>"
            page_render += f"{Prepends.RenderHeader()}"
            response_code = 200
            if self.path == '/':
                page_render += f"{Home.Render(WorkerTable.RenderWorkerTable())}"
            elif self.path == '/contact-us':
                page_render += f"{ContactUs.RenderPage()}"
            elif self.path == '/report-issue':
                page_render += f"{ReportIssue.RenderPage()}"
            else:
                response_code = 404
                page_render +=  f"{PageNotFound.Render(self.path)}"
            page_render += "</body></html>"
            self.send_response(response_code)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes(page_render, "utf-8"))
            self.close_connection()
            return
            

    httpd = http.server.HTTPServer(('localhost', PORT), Server)
    httpd.serve_forever()


## DEPLOY/START SERVER

app = main()