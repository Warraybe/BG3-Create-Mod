def create_class():
    mod_info = {
        "mod_author": input("Mod author name: ").title(),
        "class_name": input("Class name: ").title(),
    }
    has_subclass = input("Feature subclasses (y/n): ").lower()
    if has_subclass == "y":
        mod_info["subclass_level"] = int(input("Level for subclass choice: "))
        input_names = input("Subclass names (comma separated): ").title()
        mod_info["subclass_names"] = [name.strip() for name in input_names.split(",")]

    mod_info[
        "mod_dir"
    ] = f'{mod_info["mod_author"].replace(" ", "")}{mod_info["class_name"].replace(" ", "")}'
