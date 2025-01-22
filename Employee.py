class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return (f"Name: {self.name} Address: {self.address}")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
def main():
    employee = Employee("Nehal", "homeless")
    print(employee.name)

main()