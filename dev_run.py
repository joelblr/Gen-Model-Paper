import pickle
import storage
from pathlib import Path


dirs = storage.Directory_Route()


# to unpack the cache-data
try :
    with open(dirs.CACHE_DIR / "cache_data.pkl", "rb") as f1 :
        cache_obj = pickle.load(f1)
# or to create from scratch
except FileNotFoundError as e :
    cache_obj = storage.CacheData()
# display the current data
finally :
    print("\nUnpacking\n")
    cache_obj.print_instance_fields()


def get_input_from_gui() :
    inputs = {
        "std": input("Enter the STD: "),
        "from_yr": int(input("Enter the from-year: ")),
        "to_yr": int(input("Enter the to-year: ")),
        "dir_name": input("Enter the DIRNAME: "),
    }
    print(f"GUI: {inputs}")
    return inputs


req_body = get_input_from_gui()
cache_obj.update_client_req(req_body)




# at the close of app/ when updating
print("\nPacking\n")
with open(dirs.CACHE_DIR / "cache_data.pkl", "wb") as f2 :
    cache_obj.print_instance_fields()
    pickle.dump(cache_obj, f2)
