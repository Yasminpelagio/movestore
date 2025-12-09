class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'image': product.image.url if product.image else "",
                'quantity': 1
            }
        else:
            self.cart[product_id]['quantity'] += 1

        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def get_items(self):
        return self.cart.values()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
