from class_info import base_classes
from create_description import create_description
from create_folders import create_folders
from create_localization import create_localization
from create_meta import create_meta
from create_progression import create_progression
from create_sciptextender_files import create_scriptextender_files
from create_uuids import create_uuids

mod_author = input("Mod author name: ").title()
base_class = ""
while base_class not in base_classes.keys():
    base_class = input("Base class: ").lower()
    if base_class not in base_classes.keys():
        print(f"Please enter a class from {', '.join([*base_classes])}")
subclass = input("Subclass name: ").title()

mod_dir = f'{mod_author.replace(" ", "")}{subclass.replace(" ", "")}'
mod_info = {"mod_author": mod_author, "subclass": subclass,
            "main_class": base_class, "mod_name": mod_dir, "mod_dir": mod_dir}
uuids = create_uuids(base_class)
create_folders(mod_info)
create_meta(mod_info, uuids)
create_scriptextender_files(mod_info, uuids)
create_localization(mod_info, uuids)
create_description(mod_info, uuids)
create_progression(mod_info, uuids)
