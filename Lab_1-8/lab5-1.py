class book:
    def __init__(self, title, author, year): # type: ignore
        self.title = title
        self.author = author
        self.year = year    
        pass
    def get_info(self):
        return "Book's name: {}, Author: {}, Year published: {}".format(self.title, self.author, self.year) # type: ignore
war_and_peace = book("War_and_peace", "Leo_Tolstoy", 1869)
print(war_and_peace.get_info())