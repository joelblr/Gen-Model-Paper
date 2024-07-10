# Define the data storage class
class FormData :
    def __init__(self) :
        self.data = {}

    def update_data(self, key, value) :
        self.data[key] = value


from pathlib import Path
class Directory :

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\Figma\build\assets\frame0")

    def relative_to_assets(path: str) -> Path :
        return Directory.ASSETS_PATH / Path(path)
