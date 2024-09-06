class ShoppingModel:
    
    def __init__(self, db):
        self.config_database = db
        self.db = self.config_database.get_db()
        self.shopping_collection = self.db.shopping
    
    ################################################################################    
    def buy_product(self, user, quantity, price_total, date, product):
        shopping = {
            'user': user,
            'quantity': quantity,
            'price_total': price_total,
            'date': date,
            'product': product
        }
        
        self.shopping_collection.insert_one(shopping)
    
    ################################################################################
    def get_all_shopping_for_user(self, user_id):
        return list(self.shopping_collection.find({"user._id": user_id}))
    
    ################################################################################
    def get_all_shoppings(self):
        return list(self.shopping_collection.find())
    
    ################################################################################
    def delete_shopping(self, shopping_id):
        self.shopping_collection.delete_one({"_id": shopping_id})
        
    def update_shopping(self, shopping_id, field, value):
        self.shopping_collection.update_one({'_id': shopping_id}, {'$set': {field: value}})