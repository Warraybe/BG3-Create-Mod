import os
import uuid

import class_info


def create_subclass_uuids(class_name):
    uuid_list = {
        "mod_uuid": uuid.uuid4(),
        "main_class": class_info.main_classes[class_name.lower()]["uuid"],
        "subclass": uuid.uuid4(),
        "subclass_name": os.urandom(19).hex()[:37],
        "subclass_description": os.urandom(19).hex()[:37],
        "subclass_progression": uuid.uuid4(),
    }

    return uuid_list


def create_class_uuids(subclasses=None):
    uuid_list = {
        "mod_uuid": uuid.uuid4(),
        "main_class": uuid.uuid4(),
        "class_name": os.urandom(19).hex()[:37],
        "class_description": os.urandom(19).hex()[:37],
        "class_progression": uuid.uuid4(),
    }

    if subclasses:
        for subclass in subclasses:
            uuid_list[subclass] = uuid.uuid4()
            uuid_list[subclass + "_name"] = os.urandom(19).hex()[:37]
            uuid_list[subclass + "_description"] = os.urandom(19).hex()[:37]

    return uuid_list
