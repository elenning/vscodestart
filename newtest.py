

class person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return(self.name)

    def get_age(self):
        return self.age
    
    def print(self):
        print(self.get_name() + " is my name")


ben = person("Ben", 23)
ben.print()
