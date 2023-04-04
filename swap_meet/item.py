import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if round(self.condition) == 1.0:
            return "Are you sure you really want this...?"
        elif round(self.condition) == 2.0:
            return "Fair condition, but will require fixing up."
        elif round(self.condition) == 3.0:
            return "Good condition."
        elif round(self.condition) == 4.0:
            return "Great condition! Gently used for sure."
        elif round(self.condition) == 5.0:
            return "Mint condition, item is in excellent shape!"
        else:
            return "Not sure how to grade this item...(º～º)"