
class Employee:
    category = "General"

    def __init__(self, name: str, work_experience: int, high_educated: bool):
        self.name = name
        self.work_experience = work_experience
        self.high_educated = high_educated  

    def info(self):
        return f"{self.name} {self.work_experience} {self.high_educated}"
    
    def salary(self):
        return 50_000 * self.work_experience * 1.1 * (int(self.high_educated) + 1)
      



class Manager(Employee):
    def __init__(self, name, work_experience, high_educated):
        super().__init__(name, work_experience, high_educated)

# class Developer(Employee):

