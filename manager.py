import json
from typing import Any


class Manager:
    """
    manager: it is a layer between the database and the controller
    which is used to serialize and deserialize the data and to:
    - Create item as player
    - modify an element as a player
    - save this element in a database

    """

    def __init__(self, item_type: Any):
        """
        main constructors which initializes:
        - item_type (Any): instance of a class
        
        """
        self.item_type = item_type
        self.items = {}

    def load_from_json(self, path: str):
        """
        serve as the instance to store the data
        Args:
        param1 (str): relative path of jason data
        Returns:
        items (dict): dictionary of data having:
        - key --(item.id)--: id of the item (player or tournament)
        - value --(item)--: the associated data .

        """
        with open(path) as json_data:
            data_dict = json.load(json_data)
            for item_data in data_dict:
                item = self.item_type(**item_data)
                self.items[item.id] = item