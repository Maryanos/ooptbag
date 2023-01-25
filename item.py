class Item():

    def __init__(self):
        self.name = None
        self.description = None

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.item_description = item_description

    def set_name(self, item_name):
        self.item_name = item_name


