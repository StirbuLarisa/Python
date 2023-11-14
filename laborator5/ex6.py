class LibraryItem:
    def __init__(self, title, num_copies):
        self.title = title
        self.num_copies = num_copies
        self.checked_out_copies = 0

    def display_info(self):
        return f"{self.title}  - Available copies: {self.num_copies - self.checked_out_copies}"

    def check_out(self):
        if self.checked_out_copies < self.num_copies:
            self.checked_out_copies += 1
            return f"{self.title} checked out successfully."
        else:
            return f"All copies of {self.title} are currently checked out."

    def return_item(self):
        if self.checked_out_copies > 0:
            self.checked_out_copies -= 1
            return f"{self.title} returned successfully."
        else:
            return f"All copies of {self.title} are currently available."

class Book(LibraryItem):
    def __init__(self, title, num_copies, author):
        super().__init__(title, num_copies)
        self.author = author

    def display_info(self):
        return f"{super().display_info()} - Author: {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, num_copies, director):
        super().__init__(title, num_copies)
        self.director = director

    def display_info(self):
        return f"{super().display_info()} - Director: {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, num_copies, issue_date):
        super().__init__(title, num_copies)
        self.issue_date = issue_date

    def display_info(self):
        return f"{super().display_info()} - Issue Date: {self.issue_date}"

book = Book("Carte retete", 5, "Maria Popescu")
dvd = DVD("Muzica 2007", 3, "Vali Vijelie")
magazine = Magazine("National Geographic", 10, "Ianuarie 2023")

print(book.display_info())
print(book.check_out())
print(book.return_item())

print(dvd.display_info())
print(dvd.check_out())

print(magazine.display_info())
print(magazine.check_out())
