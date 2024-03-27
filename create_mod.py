from create_subclass import create_subclass_mod
from create_class import create_class_mod

mod_type = input("Type of mod (class/subclass): ").lower()

if mod_type == "subclass":
    create_subclass_mod()
elif mod_type == "class":
    create_class_mod()
else:
    print("No mod created.")
