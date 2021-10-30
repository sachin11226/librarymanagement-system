def dec(fun):
    return fun()


class Library:

    def __init__(self, listofbook, libraryname):
        self.librarname = libraryname
        self.book = listofbook
        self.bookowner = {}
        self.dic = {}
        self.id = 100
        self.setbook = set(listofbook)

        for i in self.setbook:
            self.dic[str(self.id)] = {'book': i,
                                      "quantity": self.book.count(i)}
            self.id += 1

    def display(self):
        print("-------------------LIST OF BOOKS------------------")
        print("book id\t\tquantity\t\tTitle")
        for i in self.dic.keys():
            if self.dic[i]["quantity"] == 0:
                print(
                    f" {i}\t\t  {self.dic[i]['quantity']}\t\t{self.dic[i]['book']}-[unavailable]")
            else:
                print(
                    f" {i}\t\t  {self.dic[i]['quantity']}\t\t{self.dic[i]['book']}-[available]")

    def lenbook(self):
        user = input("Enter your name :")
        book = input("Enter the book id :")
        if user in self.bookowner.keys():
            print(
                f"{user} you already own a book name {self.dic[self.bookowner[user]]['book']}")

        elif book not in self.dic.keys():
            print(f"{user} book name {book} is not a valid id ")
        elif self.dic[book]["quantity"] == 0:
            print(
                f"{user} the book name {self.dic[book]['book']} is not in stock")
        else:
            print(
                f"the book name {self.dic[book]['book']} is issued to {user}")
            self.dic.update(
                {book: {'book': self.dic[book]["book"], "quantity": self.dic[book]["quantity"]-1}})
            self.bookowner[user] = book

    def addbook(self):
        book = input("enter the book name to add :").strip()
        if book in self.setbook:
            for i, j in self.dic.items():
                if book in j.values():
                    self.dic.update(
                        {i: {'book': self.dic[i]['book'], "quantity": self.dic[i]["quantity"]+1}})
            print(f"the quantity of {book} is increased")

        elif book != " ":
            self.dic[str(self.id)] = {'book': book, 'quantity': 1}
            self.id += 1
            self.setbook.add(book)
            print(f"the book {book} is been added to the list")

        else:
            print(f"book name ' ' cannot be added")

    def returnbook(self):
        name = input("enter your name :")
        bookid = input("enter book id :")
        if self.bookowner.get(name) != None and self.bookowner[name] == bookid:
            print(
                f"hello {name} the book owner by you is {self.dic[bookid]['book']} and it is succesfully return")
            self.dic.update({bookid: {'book': self.dic[bookid]['book'],
                            "quantity":self.dic[bookid]['quantity']+1}})
        elif self.bookowner[name] != bookid:
            print(f"{name} you enter wrong bookid {bookid}")
        else:
            print(f"no book is owner by {name}")

booklist=["python", "c++", "java", "python", "java"]
with open("book.txt","r") as f:
    content=f.readlines()
    for i in content:
        i = i.replace("\n","")
        booklist.append(i)
booklist.sort()
print(booklist)

sachin = Library(booklist,"sachinlibrary")

while (True):
    print("")
    a2 = {"1": "display", "2": "lenbook",
          "3": "addbook", "4": "returnbook", "q": "quit"}
    a = {"display": sachin.display, "lenbook": sachin.lenbook,
         "addbook": sachin.addbook, "returnbook": sachin.returnbook, "quit": quit}
    for i, j in a2.items():
        print(f"press {i} to {str(j)}")
    user = input("press the button :").lower()
    if a2.get(user) == None:
        print(f"wrong button '{user}' pressed")
    else:
        dec(a[a2[user]])
