
class Employee:
    category = "General"

    def __init__(self, name: str, work_experience: int, high_educated: bool):
        self.name = name
        self.work_experience = work_experience
        self.high_educated = high_educated  

    def info(self):
        return f"{self.name} {self.work_experience} {self.high_educated}"
    



# class Manager(Employee):

# class Developer(Employee):

