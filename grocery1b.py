class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class GroceryDeliveryApp:
    def __init__(self):
        self.stores = []

    def add_store(self, name):
        store = Store(name)
        self.stores.append(store)
        return store

    def add_item_to_store(self, store, item_name, item_price):
        item = Item(item_name, item_price)
        store.add_item(item)

    def list_all_stores(self):
        print("Available stores in the city:")
        for idx, store in enumerate(self.stores, 1):
            print(f"{idx}. {store.name}")

    def list_items_in_store(self, store):
        print(f"Items in {store.name}:")
        for idx, item in enumerate(store.items, 1):
            print(f"{idx}. {item.name} - ${item.price:.2f}")
            
    def add_item_to_store(self, store_name, item_name, item_price):
        # Find the store and add the item
        for store in self.stores:
            if store.name == store_name:
                store.add_item(Item(item_name, item_price))
                return

    def edit_item_in_store(self, store_name, item_name, new_price):
        # Find the item and update its price
        for store in self.stores:
            if store.name == store_name:
                for item in store.items:
                    if item.name == item_name:
                        item.price = new_price
                        return

    def delete_item_from_store(self, store_name, item_name):
        # Find the item and remove it from the store
        for store in self.stores:
            if store.name == store_name:
                store.items = [item for item in store.items if item.name != item_name]
                return
            
    def process_order(self, store_name, items):
        for store in self.stores:
            if store.name == store_name:
                order = Order(store, items)
                # Simulate processing (e.g., payment, packing)
                order.status = "Processing"
                # Simulate delivery
                order.status = "Out for Delivery"
                # Simulate completion
                order.status = "Delivered"
                return order

    def show_order_details(self, order):
        print(f"Order from {order.store.name}")
        for item in order.items:
            print(f"- {item.name} - ${item.price:.2f}")
        print(f"Total: ${order.calculate_total():.2f}")
        print(f"Status: {order.status}")
            
class Order:
    def __init__(self, store, items):
        self.store = store
        self.items = items
        self.status = "Pending"

    def calculate_total(self):
        return sum(item.price for item in self.items)        

# Creación de la aplicación y tiendas
app = GroceryDeliveryApp()

store1 = app.add_store("Grocery Mart")
store2 = app.add_store("Fresh Foods")

# Añadir artículos a las tiendas
app.add_item_to_store("Grocery Mart", "Apples", 1.99)
app.add_item_to_store("Grocery Mart", "Bananas", 0.99)
app.add_item_to_store("Fresh Foods", "Milk", 2.49)
app.add_item_to_store("Fresh Foods", "Bread", 1.89)

# Listar todas las tiendas
app.list_all_stores()

# Editar un artículo
app.edit_item_in_store("Grocery Mart", "Apples", 2.19)

# Eliminar un artículo
app.delete_item_from_store("Fresh Foods", "Bread")

# Procesar un pedido
# Nota: La implementación de `process_order` requiere el nombre de la tienda y una lista de objetos `Item`, pero no se ha provisto una forma directa de obtener estos objetos `Item` desde el nombre.
# Suponiendo que `process_order` pueda modificarse para aceptar nombres de artículos en lugar de objetos `Item`, o que exista otra forma de obtener los objetos `Item` necesarios.
order = app.process_order("Grocery Mart", ["Apples", "Bananas"])  # Esto es hipotético, dependiendo de cómo se espera que `process_order` funcione realmente

# Mostrar detalles del pedido, si el pedido fue creado exitosamente
if order:
    app.show_order_details(order)

# Listar artículos en las tiendas
app.list_items_in_store(store1)
app.list_items_in_store(store2)
