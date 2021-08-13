def dec(fun):
    return fun()


class Library:

    def __init__(self, listofbook, libraryname):
        self.librarname = libraryname
        self.book = listofbook
        self.bookowner = {}
        self.dic = {}

        stop = 0
        if stop == 0:
            for i in self.book:
                self.dic[i] = {"quantity": self.book.count(i)}
            stop += 1

    def display(self):
        for i in self.dic.keys():
            if self.dic[i]["quantity"] == 0:
                print(f"{self.dic[i]['quantity']} of book {i} is unavailable")
            else:
                print(f"{self.dic[i]['quantity']} of book {i} is available")

    def lenbook(self):
        user = input("Enter your name :")
        book = input("Enter the book name :")
        if user in self.bookowner.keys():
            print(f"{user} you already own a book name {self.bookowner[user]}")

        elif book not in self.dic.keys():
            print(f"{user} book name {book} is not in the list")
        elif self.dic[book]["quantity"] == 0:
            print(f"{user} the book name {book} is not in stock")
        else:
            print(f"the book name {book} is issued to {user}")
            self.dic.update({book: {"quantity": self.dic[book]["quantity"]-1}})
            self.bookowner[user] = book

    def addbook(self):
        book = input("enter the book name to add :").strip()
        if book in self.dic.keys():
            self.dic.update({book: {"quantity": self.dic[book]["quantity"]+1}})
            print(f"the quantity of {book} is increased")  
            
        elif book!=" ":
            self.dic[book]={"quantity":1}
            print(f"the book {book} is been added to the list")
              
        else:
            print(f"book name ' ' cannot be added")
    def returnbook(self):
        name = input("enter your name :")
        if self.bookowner.get(name) != None:
            print(f"hello {name} the book owner by you is {self.bookowner.get(name)} and it is succesfully return")
            self.dic.update({self.bookowner[name]: {
                            "quantity": self.dic[self.bookowner[name]]["quantity"]+1}})
        else:
            print(f"no book is owner by {name}")


sachin = Library(["python", "c++", "java", "python", "java"], "sachinlibrary")
while (True):
    a2 = {"1": "display", "2": "lenbook",
          "3": "addbook", "4": "returnbook", "q": "quit"}
    a = {"display": sachin.display, "lenbook": sachin.lenbook,
         "addbook": sachin.addbook, "returnbook": sachin.returnbook, "quit": quit}
    for i, j in a2.items():
        print(f"press {i} to {str(j)}")
    user = input("press the button :")
    if a2.get(user) == None:
        print(f"wrong button '{user}' pressed")
    else:
        dec(a[a2[user]])
