# ------------ Task Class ------------
class Task:
    def __init__(self, title, desc, due_date):
        self.title = title
        self.desc = desc
        self.due_date = due_date
        self.status = "incomplete"

    def mark_complete(self):
        self.status = "complete"

    def __str__(self):
        return f"{self.title} | {self.status} | due: {self.due_date}\n  {self.desc}"


# ------------ ToDoList Class ------------
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for t in self.tasks:
            print(t)
            print("-" * 30)

    def list_incomplete(self):
        for t in self.tasks:
            if t.status == "incomplete":
                print(t)
                print("-" * 30)

    def complete_task(self, title):
        for t in self.tasks:
            if t.title == title:
                t.mark_complete()
                print("Task completed!")
                return
        print("Task not found!")


# ------------ Main Program ------------
def todo_menu():
    todo = ToDoList()

    while True:
        print("\n--- ToDo Menu ---")
        print("1. Add task")
        print("2. Mark task complete")
        print("3. List all tasks")
        print("4. List incomplete tasks")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            date = input("Due date: ")
            todo.add_task(Task(title, desc, date))
            print("Added!")

        elif choice == "2":
            title = input("Which task to complete? ")
            todo.complete_task(title)

        elif choice == "3":
            todo.list_tasks()

        elif choice == "4":
            todo.list_incomplete()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

# todo_menu()     # run if needed




# ------------ Post Class ------------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"


# ------------ Blog Class ------------
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for p in self.posts:
            print(p)
            print("-" * 40)

    def posts_by_author(self, author):
        for p in self.posts:
            if p.author == author:
                print(p)
                print("-" * 40)

    def delete_post(self, title):
        for p in self.posts:
            if p.title == title:
                self.posts.remove(p)
                print("Post deleted")
                return
        print("Post not found")

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content
                print("Edited!")
                return
        print("Post not found")

    def latest_posts(self, n=3):
        for p in self.posts[-n:]:
            print(p)
            print("-" * 40)


# ------------ Main Program ------------
def blog_menu():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add post")
        print("2. List all posts")
        print("3. Posts by author")
        print("4. Delete post")
        print("5. Edit post")
        print("6. Show latest posts")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Author: ")
            blog.posts_by_author(author)

        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Title to edit: ")
            new_c = input("New content: ")
            blog.edit_post(title, new_c)

        elif choice == "6":
            blog.latest_posts()

        elif choice == "7":
            break

        else:
            print("Invalid choice!")

# blog_menu()   # run if needed







# ------------ Account Class ------------
class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"{self.holder} | {self.number} | balance: {self.balance}"


# ------------ Bank Class ------------
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)

    def find(self, number):
        for a in self.accounts:
            if a.number == number:
                return a
        return None

    def check_balance(self, number):
        acc = self.find(number)
        if acc:
            print(acc.balance)
        else:
            print("Account not found!")

    def deposit_money(self, number, amount):
        acc = self.find(number)
        if acc:
            acc.deposit(amount)
            print("Deposited!")
        else:
            print("Account not found!")

    def withdraw_money(self, number, amount):
        acc = self.find(number)
        if acc:
            if acc.withdraw(amount):
                print("Withdrawn!")
            else:
                print("Not enough money!")
        else:
            print("Account not found!")

    def transfer(self, from_acc, to_acc, amount):
        a1 = self.find(from_acc)
        a2 = self.find(to_acc)

        if not a1 or not a2:
            print("Account not found!")
            return

        if a1.withdraw(amount):
            a2.deposit(amount)
            print("Transfer done!")
        else:
            print("Not enough money for transfer!")

    def show_details(self, number):
        acc = self.find(number)
        if acc:
            print(acc)
        else:
            print("Account not found!")


# ------------ Main Program ------------
def bank_menu():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Add account")
        print("2. Check balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Show details")
        print("7. Exit")

        c = input("Choose: ")

        if c == "1":
            num = input("Account number: ")
            name = input("Holder name: ")
            bank.add_account(Account(num, name))

        elif c == "2":
            num = input("Account number: ")
            bank.check_balance(num)

        elif c == "3":
            num = input("Account: ")
            amt = float(input("Amount: "))
            bank.deposit_money(num, amt)

        elif c == "4":
            num = input("Account: ")
            amt = float(input("Amount: "))
            bank.withdraw_money(num, amt)

        elif c == "5":
            a = input("From: ")
            b = input("To: ")
            amt = float(input("Amount: "))
            bank.transfer(a, b, amt)

        elif c == "6":
            num = input("Account: ")
            bank.show_details(num)

        elif c == "7":
            break

# bank_menu()   # run if needed
