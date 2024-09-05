from datetime import datetime

class Task:    #Creating the basic class wich includes all the needed attributes
    def __init__(self):
        #Defining all the attributes:
        self.task_name = self.get_task_name()
        self.task_category = self.get_task_category()
        self.priority = self.get_task_priority() #using .get here to improve code
        self.task_status = self.get_task_status()
        self.creation_date = self.get_creation_date()
        self.end_date = self.get_end_date()  
        self.task_description = self.get_task_description()  

    def get_task_name(self):
        return input('Enter the task name: ')
        
    def get_task_category(self):
        categories = {'1': 'Personal', '2': 'Work', '3': 'Education', '4': 'Other'}
        while True:
            choice = input('Select task category (1: Personal, 2: Work, 3: Education, 4: Other): ')
            if choice in categories:
                return categories[choice]
            print("Invalid choice. Please select a valid option.") #To ensure the user's output is within the specified options.

    def get_task_priority(self):
        priorities = {'1': 'High', '2': 'Medium', '3': 'Low'}
        while True:
            choice = input('Select task priority (1: High, 2: Medium, 3: Low): ')
            if choice in priorities:
                return priorities[choice]
            print("Invalid choice. Please select a valid option.") #To ensure the user's output is within the specified options.
    
    def get_task_status(self):
        statuses = {'1': 'Not Started', '2': 'In Progress', '3': 'Completed', '4': 'Uncompleted'}
        while True:
            choice = input('Select Task Status (1: Not Started, 2: In Progress, 3: Completed, 4: Uncompleted): ')
            if choice in statuses:
                return statuses[choice]
            print("Invalid choice. Please select a valid option.") #To ensure the user's output is within the specified options.

    def get_creation_date(self):
        while True:
            date_input = input("Enter the creation date (YYYY-MM-DD) or press Enter to use today's date: ")
            if date_input == "":
                return datetime.now().strftime('%Y-%m-%d')
            try:
                datetime.strptime(date_input, '%Y-%m-%d')
                return date_input
            except ValueError:  #To ensure the user's input is within the specified format.
                print("Invalid date format. Please use YYYY-MM-DD format.")  

    def get_end_date(self):
       #the following code applies on cases which the user chhose the task to be completed to set the date to (Today) automatically.
        if self.task_status == 'Completed': 
            return datetime.now().strftime('%Y-%m-%d')
        else:
            while True:
                date_input = input("Enter the end date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(date_input, '%Y-%m-%d')
                    return date_input
                except ValueError: #To ensure the user's input is within the specified format.
                    print("Invalid date format. Please use YYYY-MM-DD format.") 

    def get_task_description(self):
        return input("Enter the task description: ")

    def display_task(self): #to display all the attributes according to the user input
        print(f"\nTask Created:")
        print(f"Task Name: {self.task_name}")
        print(f"Task Category: {self.task_category}")
        print(f"Task Priority: {self.priority}")
        print(f"Task Status: {self.task_status}")
        print(f"Creation Date: {self.creation_date}")
        print(f"End Date: {self.end_date}")
        print(f"Task Description: {self.task_description}")

# Create and display a task
user_task = Task()
user_task.display_task()





