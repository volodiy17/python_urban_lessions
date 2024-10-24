from product import Product

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        return open(self.__file_name, 'r', encoding="utf-8").read()

    def add(self, *products: 'Product'):
        file = open(self.__file_name, 'a', encoding="utf-8")
        for product in products:
            if str(product) not in self.get_products().splitlines():
                file.write(str(product) + '\n')
            else:
                print(f'{str(product)} уже есть в магазине')
        file.close()
        return

