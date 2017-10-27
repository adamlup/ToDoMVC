class Todo():

    all_todo_items = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_done = False

    def __str__(self):
        return 'item name -->', str(self.name), 'item status -->', str(self.is_done), 'item description -->', str(self.description)