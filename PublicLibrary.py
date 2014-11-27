# Public Library for Codefellows Python Coding Challenge

class Library(object):
    def __init__(self):
        self.shelfs = []

    def addShelf(self, shelf):
        self.shelfs.append(shelf)
        
    def report(self):
        return [s.getBooks() for s in self.shelfs]

class Shelf(object):
    def __init__(self):
        self.books = []

    def getBooks(self):
        return [b.name for b in self.books]

class Book(object):
    def __init__(self, name):
        self.name = name
        self.shelf = None
        
    def enshelf(self, shelf):
        self.shelf = shelf
        shelf.books.append(self)

    def unshelf(self):
        if self.shelf:
            self.shelf.books.remove(self)
            self.shelf = None
        else:
            print("Not On A Shelf!")

if __name__ == "__main__":

    library = Library()
    shelfs = [Shelf(), Shelf()]
    for s in shelfs:
        library.addShelf(s)
    
    books, names = [], ["Harry Wizard", "Lord of The Jewlry", "Discplanet", "Adventures of Blueberry Wing", "Game of Crowns"]
    for n in names:
        books.append(Book(n))

    for i, b in enumerate(books):
        if i>2:
            b.enshelf(shelfs[0])
        else:
            b.enshelf(shelfs[1])

    print(library.report())
    print(shelfs[0].getBooks())
    print(shelfs[1].getBooks())
    
