import typing

# Define the data storage class
class CacheData :
    def __init__(self) :
        self.data = {}
        self.file_offsets = {} # cache table for csv
        # self.file_offsets: dict[str, dict[str, list[int]]] = {} # cache table for csv
        self.client_req = {} # input from GUI
        # self.client_req: dict[str, typing.Any] = {} # input from GUI


    def update_data(self, key, value) :
        self.data[key] = value


    def update_client_req(self, obj) :
        self.client_req = {}
        for key in obj :
            self.client_req[key] = obj[key]


    def print_instance_fields(self) :
        for attr, value in self.__dict__.items() :
            print(f"{attr}: {value}")


    def __getstate__(self) :
        state = self.__dict__.copy()
        del state['client_req']
        return state


from pathlib import Path
class Directory_Route :

    def __init__(self) :
        self.ASSETS_DIR = Path(__file__).parent / 'assets'
        self.CACHE_DIR = Path(__file__).parent / 'cache'
        self.MODEL_DIR = Path(__file__).parent / 'model'
        self.RESULT_DIR = Path(__file__).parent / 'model-paper'
        self.TEMPLATES_DIR = Path(__file__).parent / 'templates'


class Directory :

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\Admin\Desktop\\Figma\build\\assets\\frame0")

    def relative_to_assets(self, path: str) -> Path :
        return Directory.ASSETS_PATH / Path(path)
