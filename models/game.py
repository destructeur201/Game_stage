class Game:
    
    title: str
    studio: str
    year: int
    price: float
    stock: int
    new: bool

    def __init__(self, title = "", studio = "", year = 1987, price = 0.0, stock = 0, new = False):
        
        self.title = title
        self.studio = studio
        self.year = year
        self.price = price
        self.stock = stock
        self.new = new

    def json(self):
        return {
            'title': self.title,
            'studio': self.studio,
            'year': self.year,
            'price': self.price,
            'stock': self.stock,
            'new': self.new
        }
