# """
# این کلاس برای مدیریت یک کار در to do list نوشته شده

# ویژگی ها =
# name = اسم کار
# description = توضیحاتی راجب کار
# priority = اولویت کار مد نظر

# اگر اولویت خارج از موارد ذکر شده باشه با value error مواجه خواهد شد

# """
import csv
class Task():
    
    def __init__(self, name, description, priority):
        allowed_priorities= ["High", "Medium", "Low"]
        if priority not in allowed_priorities:
            raise ValueError(f"priority most be one of {allowed_priorities}")
        self.name = name
        self.description = description
        self.priority = priority
        
    def __str__(self):
         return f"[{self.priority}] {self.name} - {self.description}"

# در اینجا یک کلاس to do list داریم برای اینکه کار های جدید رو اضافه کنیم. به نمایش بگذاریم و حذف و بارگذازی کنیم

class To_do_list:
    def __init__(self):
        # لیست خالی برای نگهداری تسک ها و کار ها
        self.tasks = []
        #تابع برای اضافه کردن کار ها 
    
    def add_task(self, task):
        self.tasks.append(task)

        #تابع برای نشان دادن کار ها 
    def show_tasks(self):
        if not self.tasks:
            print("list is empty")
            return
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index)
            print(f"the {removed_task.name} removed")
        except IndexError:
            print("number is not valid")

    def save_task(self, filename="tasks.csv"):
        with open(filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.description},{task.priority}\n")
        print("list saved")

    def load_tasks(self, filename="tasks.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                self.tasks.clear()  
                for name, description, priority in reader:
                    self.tasks.append(Task(name, description, priority))
            print("list upload")
        except FileNotFoundError:
            print("list is empty")


if __name__ == "__main__":
    todo_list = To_do_list()

    while True:
        print("\n what do you want to do?")
        print("1. add a new task")
        print("2. Show all task")
        print("3. Remove all task")
        print("4. save task")
        print("5. load task")
        print("6. Exit")

        choice = input("enter your choice: ")

        if choice == "1":
            name = input("task name: ")
            description = input ("Descriptiion: ")
            priority = input("priprity(High, Medium, Low): ")
            try:
                task = Task(name, description, priority)
                todo_list.add_task(task)
                print("task added successfully")
            except ValueError as e:
                print(e)

        elif choice == "2":
            todo_list.show_tasks()

        elif choice == "3":
            todo_list.remove_task()

        elif choice == "4":
            todo_list.save_task()

        elif choice == "5":
            todo_list.load_tasks()  

        elif choice == "6":
            print("GOOD BYE!")
            break

        else:
            print("invalid choice")