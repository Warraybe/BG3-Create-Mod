from class_info import main_classes
from create_files import create_subclass_files
from create_folders import create_folders
from create_uuids import create_subclass_uuids


def create_subclass_mod():
    mod_info = {"mod_author": input("Mod author name: ").title(), "main_class": ""}
    while mod_info["main_class"] not in main_classes.keys():
        mod_info["main_class"] = input("Main class: ").lower()
        if mod_info["main_class"] not in main_classes.keys():
            print(f"Please enter a class from {', '.join([*main_classes])}")
    mod_info["subclass"] = input("Subclass name: ").title()

    mod_info[
        "mod_name"
    ] = f'{mod_info["mod_author"].replace(" ", "")}{mod_info["subclass"].replace(" ", "")}'

    uuids = create_subclass_uuids(mod_info["main_class"])
    create_folders(mod_info)
    create_subclass_files(mod_info, uuids)
