import Database.Worker_DBConfig as WorkerDB
import os

## Web Page Templates

import Pages.home as Home
import Pages.PageNotFound as PageNotFound

## Compoennts

import Components.table as Table

def RenderWorkerTable():
        WorkersToRenderTable = []

        FetchdWorkers = os.listdir("./Database/Workers")

        PayPerHour = 25
        Workers = [
    
        ]

        
        for i in FetchdWorkers:
            data = open(f"./Database/Workers/{i}")
            WorkerData = WorkerDB.ConvertWorkerToObj(data.read())
            Workers.append(WorkerData)

        for i in Workers:
            WorkersToRenderTable.append([
                i.get_name(),
                i.get_employee_number(),
                i.get_office_number(),
                i.get_hours_worked(),
                i.get_hours_overtime(),
                f'${(i.get_hours_worked()+ i.get_hours_overtime()) * PayPerHour}'
            ])
#                print(f"{i.get_name():25}|{i.get_employee_number():11}|{i.get_office_number():10}|{i.get_hours_worked():12}|{i.get_hours_overtime():8}|{f'${(i.get_hours_worked()+ i.get_hours_overtime()) * PayPerHour}':10}")
            
        return f"{Table.RenderTable(WorkersToRenderTable, ['Name','Employee Num','Office Num','Hours Worked','Overtime Hours','Estimated Pay'])}"
                
    