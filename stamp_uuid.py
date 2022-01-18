import uuid
import datetime
import json


def write_to_file(stamp_uuid_db):
    
        with open("stamp_uuid.json", "w") as f:
            # write the new stamp_uuid_db to the file
            json.dump(stamp_uuid_db, f)
        
def read_from_file():
    with open("stamp_uuid.json", "r") as f:
        stamp_uuid_db = json.load(f)
    return stamp_uuid_db


def generate_stamp_uuid():
    # generate a dictionary having the timestamp in a string format including milliseconds as the key and uuid as the value
    stamp_uuid = {
        datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f") : str(uuid.uuid4()),
    }
    # read the file
    stamp_uuid_db = read_from_file()
    # add a new dictionary to the json file
    stamp_uuid_db.append(stamp_uuid)
    # write to the file
    write_to_file(stamp_uuid_db)
    return stamp_uuid_db