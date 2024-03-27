import os


def create_folders(mod_info):
    cwd = os.getcwd()

    folders = [
        os.path.join(cwd, mod_info["mod_dir"]),
        os.path.join("Localization", "English"),
        os.path.join(f"Mods\\{mod_info['mod_dir']}\\ScriptExtender", "Lua"),
        os.path.join("Public", mod_info["mod_dir"]),
    ]
    public_folders = [
        "ActionResourceDefinitions",
        ["Assets", "Textures", "Icons"],
        "CharacterCreationPresets",
        "ClassDescriptions",
        ["Content", "UI", "[PAK]_UI"],
        ["Content", "[PAK]_CharacterVisuals"],
        "GUI",
        "Lists",
        "Progressions",
        "RootTemplates",
        ["Stats", "Generated", "Data"],
        "Tags",
    ]

    for folder in folders:
        os.makedirs(os.path.join(folders[0], folder), exist_ok=True)
        if "Public" in folder:
            for sub_folder in public_folders:
                if isinstance(sub_folder, list):
                    os.makedirs(
                        os.path.join(os.path.join(folders[0], folder), *sub_folder),
                        exist_ok=True,
                    )
                else:
                    os.makedirs(
                        os.path.join(os.path.join(folders[0], folder), sub_folder),
                        exist_ok=True,
                    )
