import math


class Printer:
    def __init__(self, paper_size, border_style):
        self.paper_size = paper_size
        self.stock = 5
        if border_style == "plain":
            self.top_edge = "-"
            self.corner = "+"
            self.left_edge = "|"
            self.right_edge = "|"
        elif border_style == "fancy":
            self.top_edge = "~"
            self.corner = "*"
            self.left_edge = "{"
            self.right_edge = "}"
        else:
            raise ValueError("Expected 'plain' or 'fancy'")

    def restock(self):
        self.stock = 5

    def print(self, string):
        words = string.split()[::-1]
        lines = []
        while words:
            line = ""
            while words:
                if len(line) + bool(line) + len(words[-1]) <= self.paper_size:
                    line += " " * bool(line) + words.pop()
                elif len(words[-1]) > self.paper_size:
                    word = words.pop()
                    words.append(word[self.paper_size - 1:])
                    words.append(word[:self.paper_size - 1] + "-")
                else:
                    break
            lines.append(line + " " * (self.paper_size - len(line)))
        num_pages = math.ceil(len(lines) / self.paper_size)
        if num_pages > self.stock:
            print("Not enough paper")
            return False
        for page in range(num_pages):
            print(self.corner + self.top_edge * self.paper_size + self.corner)
            for line in lines[page * self.paper_size:(page + 1) * self.paper_size]:
                print(self.left_edge + line + self.right_edge)
            print(self.corner + self.top_edge * self.paper_size + self.corner)
            print()
        self.stock -= num_pages
        return True

    def print_diagnostic_page(self):
        self.print(f"Regular printer with {self.stock} pages")


class DeluxePrinter(Printer):
    def __init__(self, paper_size):
        super().__init__(paper_size, "fancy")

    def charge_credits(self):
        print(f"You have been charged 10 credits for a full restock")

    def print(self, string):
        success = super().print(string)
        if not success:
            self.charge_credits()
            self.restock()
            super().print(string)

    def print_diagnostic_page(self):
        self.print(f"Deluxe printer with {self.stock} pages")


printer = Printer(20, "plain")
printer.print("Once upon a midnight dreary, while I pondered, weak and weary")

deluxe_printer = DeluxePrinter(8)
deluxe_printer.print("Two households, both alike in dignity\nIn fair Verona, where we lay our scene")
deluxe_printer.print("From ancient grudge break to new mutiny\nWhere civil blood makes civil hands unclean")
deluxe_printer.print("The fearful passage of their death- marked love\nAnd the continuance of their parents' rage")
