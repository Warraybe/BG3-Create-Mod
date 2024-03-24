import os


def create_localization(mod_info, uuids):
    localization_content = f"""<?xml version="1.0" encoding="utf-8"?>
<contentList>	
    <content contentuid="{uuids['subclass_name']}" version="1">{mod_info['subclass']}</content>
    <content contentuid="{uuids['subclass_description']}" version="1">Placeholder</content>
</contentList> """

    localization_file = os.path.join(
        os.path.abspath(
            f"{mod_info['mod_dir']}\\Localization\\English"
        ),
        mod_info['mod_dir'].replace(" ", "") + ".xml",
    )
    with open(localization_file, "w") as f:
        f.write(localization_content)
