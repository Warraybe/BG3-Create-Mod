from class_info import base_classes
from create_files import create_subclass_files
from create_folders import create_folders
from create_uuids import create_subclass_uuids

mod_type = input("Type of mod (class/subclass): ").lower()
mod_author = input("Mod author name: ").title()
base_class = ""
while base_class not in base_classes.keys():
    base_class = input("Base class: ").lower()
    if base_class not in base_classes.keys():
        print(f"Please enter a class from {', '.join([*base_classes])}")
subclass = input("Subclass name: ").title()

mod_dir = f'{mod_author.replace(" ", "")}{subclass.replace(" ", "")}'
mod_info = {
    "mod_author": mod_author,
    "subclass": subclass,
    "main_class": base_class,
    "mod_name": mod_dir,
    "mod_dir": mod_dir,
}
uuids = create_subclass_uuids(base_class)

if mod_type == "subclass":
    create_folders(mod_info)
    create_subclass_files(mod_info, uuids)
elif mod_type == "class":
    pass
else:
    print("No mod created.")
