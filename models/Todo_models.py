class Todo():

    all_todo_items = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_done = False