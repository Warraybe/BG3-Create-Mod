from create_subclass import create_subclass_mod

mod_type = input("Type of mod (class/subclass): ").lower()

if mod_type == "subclass":
    create_subclass_mod()
elif mod_type == "class":
    pass
else:
    print("No mod created.")
