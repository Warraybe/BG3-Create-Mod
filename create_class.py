from create_uuids import create_class_uuids
from create_folders import create_folders
from create_files import create_class_files


def create_class_mod():
    mod_info = {
        "mod_author": input("Mod author name: ").title(),
        "class_name": input("Class name: ").title(),
        "subclass_names": [],
    }
    has_subclass = input("Feature subclasses (y/n): ").lower()
    if has_subclass == "y":
        mod_info["subclass_level"] = int(input("Level for subclass choice: "))
        input_names = input("Subclass name(s) (comma separated): ").title()
        mod_info["subclass_names"] = [name.strip() for name in input_names.split(",")]

    mod_info[
        "mod_dir"
    ] = f'{mod_info["mod_author"].replace(" ", "")}{mod_info["class_name"].replace(" ", "")}'

    uuids = create_class_uuids(mod_info["subclass_names"])
    create_folders(mod_info)
    create_class_files()
