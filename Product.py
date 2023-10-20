class Product:

    def __init__(self, type, noi, ppi, discount):
        self.type = type
        self.noi = noi
        self.ppi = ppi 
        self.discount = discount
        

    def getTotalPrice(self):
        if self.discount == "yes":
            return self.noi * self.ppi * 0.90
        else:
            return self.noi * self.ppi
        
    def __str__(self):
        return f""" Your Order details are as follows:
{self.type}: price per item: {self.ppi}: number of Items: {self.noi}, discount: {self.discount} : price : {self.getTotalPrice()}
"""
    
        

