import os
import uuid

import class_info


def create_subclass_uuids(class_name):
    uuid_list = {
        "mod_uuid": uuid.uuid4(),
        "base_class": class_info.base_classes[class_name.lower()]['uuid'],
        "subclass": uuid.uuid4(),
        "subclass_name": os.urandom(19).hex()[:37],
        "subclass_description": os.urandom(19).hex()[:37],
        "subclass_progression": uuid.uuid4(),
    }

    return uuid_list
