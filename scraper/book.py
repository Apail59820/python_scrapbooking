class Book:
    def __init__(self, title, price, availability, rating):
        self.title = title
        self.price = price
        self.availability = availability
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "rating": self.rating
        }

    def __str__(self):
        return "Titre: {}\nPrix: {}\nDisponibilite: {}\nNotes: {}".format(self.title, self.price, self.availability, self.rating)