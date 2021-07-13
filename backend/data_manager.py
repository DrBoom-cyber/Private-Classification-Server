import os

#Recieves output configuration which is pairs of paths and resolution_keys
class DataManager():
    def __init__(self, data_path, output_config, hash_length = 10):
        self.data_path = data_path
        self.output_config = output_config

        self.hash_length = hash_length
        self.data_map = self.generate_hashes()

    def request_item(self):
        pass

    def resolve_item(self, item_hash, resolution_key):
        pass

    def generate_hashes(self):
        data_map = {}
        for path in os.list_dir(self.data_path):
            data_map[os.urandom(self.hash_length)] = path
        return data_map
