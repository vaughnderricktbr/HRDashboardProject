
class BirthDate:
    def __init__(self, m, d, y) -> None:
        self.month=m
        self.day=d
        self.year=y

class Worker:
    def __init__(self):
        self.hours_worked = 0
        self.overtime_worked = 0
        pass
    def get_employee_number(self):
        return self.employee_number
    def set_employee_number(self, x):
        if x == int(x):
            self.employee_number = x
            return x
        else:
            raise Exception("Employeee Number must be an interger.")
    def get_office_number(self):
        return self.office_number
    def set_office_number(self, x):
        if (x < 100 or x > 500):
            raise Exception("Office number must be from 100 to 500.")
        self.office_number = x
        return x
    def get_name(self):
        return self.name
    def set_name(self, FirstName):
        if FirstName == "":
            raise Exception("Name must not be empty.")
        self.name = str(FirstName).replace("_", "", -1).replace(".", "", -1).replace("-", "", -1)
        return self.name
    def set_birthdate(self, d, m, y):
        if(m < 1 or m > 12):
            raise Exception("Month is invalid. Must be between 1 and 12.")
        elif(d < 1 or d > 31):
            raise Exception("Day is invalid. Must be between 1 and 31.")
        self.birthdate = BirthDate(m, d, y)
    def add_hours(self, x):
        if x > 9:
            self.hours_worked += 9
            self.overtime_worked += (x - 9)
        elif x < 0:
            raise Exception("Hours cannot be less than zero.")
        else:
            self.hours_worked += x
    def get_hours_worked(self):
        return self.hours_worked
    def get_hours_overtime(self):
        return self.overtime_worked
    

def ConvertWorkerToObj(str):
    line = str.split("\n")
    employee = Worker()
    for data in line:
        if data.split("-->:").__len__() > 1:
            data_content = data.split("-->:")
            property_name = data_content[0]
            property_value = data_content[1]
            #print(f"{property_name}:{property_value}")
            if property_name == "FIRST_NAME":
                employee.set_name(property_value)
            elif property_name == "EMPLOYEE_ID":
                employee.set_employee_number(int(property_value))
            elif property_name == "OFFICE_NUM":
                employee.set_office_number(int(property_value))
            elif property_name == "BIRTH_DATE:":
                birh_date = property_value.split("/")
                employee.set_birthdate(int(birh_date[1]), int(birh_date[0]), int(birh_date[2]))
            elif property_name == "HOURS_WORKED":
                hours_worked = property_value.split("+")
                for i in hours_worked:
                    employee.add_hours(int(i))
    return employee    
            
