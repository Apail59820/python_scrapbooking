class Product:
    def __init__(self, title, price, source):
        self.title = title
        self.price = price
        self.source = source
    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "source": self.source,
        }

    def __str__(self):
        return "Titre: {}\nPrix: {}\nSource: {}".format(self.title, self.price, self.source)