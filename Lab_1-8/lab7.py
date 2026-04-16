class Employee:
    def __init__(self, name, id): # type: ignore
        self.name = name
        self.id = id    
        pass
    def get_info(self):
        return "Employee's name: {}, Id: {}".format(self.name, self.id) # type: ignore
thomas = Employee("Thomas_Muller", 14422200095)
print(thomas.get_info())