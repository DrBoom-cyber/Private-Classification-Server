import os
import ntpath

#Recieves output configuration which is pairs of paths and resolution_keys
class DataManager():
    def __init__(self, data_path, output_config, hash_length = 10):
        self.data_path = data_path
        self.output_config = output_config

        self.hash_length = hash_length
        self.data_map = self.generate_hashes()

        self.available_items = self.data_map.keys()
        self.in_use = []

    def request_item(self):
        item_key = self.available_items.pop()
        self.in_use.append(item_key)
        return {
            'image_url' : self.data_map[item_key],
            'item_key' : item_key,
            'options' : self.output_config.keys()
        }

    def resolve_item(self, item_key, resolution_key):
        if item_key in self.data_map.keys():
            item = self.data_map[item_key]
        else:
            raise KeyError(f'Invalid item key, no data item exists with key {item_key}')
        if resolution_key in self.output_config.keys():
            os.rename(item, os.path.join(self.output_config[resolution_key], ntpath.basename(item)))
        else:
            raise KeyError(f'Invalid resolution key, no output item exists with key {resolution_key}')

    def generate_hashes(self):
        data_map = {}
        for path in os.listdir(self.data_path):
            data_map[os.urandom(self.hash_length)] = path
        return data_map
