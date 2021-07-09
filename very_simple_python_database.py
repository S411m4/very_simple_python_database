class School:

    def __init__(self, firstName, lastName, email, money, job):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.money = money
        self.job = job

    def __str__(self):
        data = [self.firstName, self.lastName, self.email, self.money, self.job]
        return str(data)
        
        
def enter_data():
    global firstName, lastName, money, job, email
    
    firstName = input("first name: ")
    lastName = input("last name: ")
    money = input("student's fees or worker's salary: ")
    email = input("email: ")
    job = input("job: ")
    print("\n")

  


def enter_data_answer():
    
    answer = input("do you want to enter data of another person (yes / no): ")

    if answer not in ["yes", "y", "no", "n"]:
        print("\n")
        print("enter a valide option (yes / no)")
        print("\n")
        enter_data_answer()
        
    return answer

data_base = []

def make_object():
    school_object = School(firstName, lastName, money, email, job)
    data_base.append(school_object.__str__())

    
if __name__ == '__main__':
    enter_data()
    make_object()
    
    while enter_data_answer() in ["yes", "y"]:
        enter_data()
        make_object()

    print("\n")
    for data in data_base:
        print(data)
