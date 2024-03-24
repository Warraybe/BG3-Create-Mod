import os
import uuid

from class_info import base_classes


def create_progression(mod_info, uuids):
    progression_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="6" build="5"/>
    <region id="Progressions">
        <node id="root">
            <children>
                <node id="Progression"> {mod_info['subclass']}
                    <attribute id="Level" type="uint8" value="{base_classes[mod_info['main_class']]['level']}"/>
                    <attribute id="Name" type="LSString" value="{mod_info['mod_author'].replace(" ", "")}{mod_info['subclass'].replace(" ", "")}"/>
                    <attribute id="ProgressionType" type="uint8" value="1"/>
                    <attribute id="PassivesAdded" type="LSString" value=""/>
                    <attribute id="Boosts" type="LSString" value=""/>
                    <attribute id="Selectors" type="LSString" value=""/>
                    <attribute id="TableUUID" type="guid" value="{uuids['subclass_progression']}"/>
                    <attribute id="UUID" type="guid" value="{uuid.uuid4()}"/>
                </node>
            </children>
        </node>
    </region>
</save>\n'''

    file_path = os.path.abspath(f"{mod_info['mod_dir']}\\Public\\{mod_info['mod_dir']}\\Progressions")

    with open(os.path.join(file_path, "Progressions.lsx"),
              "w") as f:
        f.write(progression_content)
