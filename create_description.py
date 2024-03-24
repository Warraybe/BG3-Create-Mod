import os


def create_description(mod_info, uuids):
    description_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="7" build="406"/>
    <region id="ClassDescriptions">
        <node id="root">
            <children>
                <node id="ClassDescription"> {mod_info['subclass']}
                    <attribute id="CharacterCreationPose" type="guid" value="0f07ec6e-4ef0-434e-9a51-1353260ccff8"/>
                    <attribute id="DisplayName" type="TranslatedString" handle="{uuids['subclass_name']}" version="1"/>
                    <attribute id="Description" type="TranslatedString" handle="{uuids['subclass_description']}" version="1"/>
                    <attribute id="LearningStrategy" type="uint8" value="1"/>
                    <attribute id="Name" type="FixedString" value="{mod_info['mod_name']}"/>
                    <attribute id="PrimaryAbility" type="uint8" value="1"/> 4 is for int. order goes from Str, Dex, Con, Int, Wis, and Cha.
                    <attribute id="ProgressionTableUUID" type="guid" value="{uuids['subclass_progression']}"/>
                    <attribute id="ParentGuid" type="guid" value="{uuids['base_class']}"/>
                    <attribute id="SoundClassType" type="FixedString" value="{mod_info['main_class'].title()}"/>
                    <attribute id="SpellCastingAbility" type="uint8" value="6"/>
                    <attribute id="UUID" type="guid" value="{uuids['subclass']}"/>
                </node>	                		
            </children>
        </node>
    </region>
</save>\n\n'''

    file_path = os.path.abspath(
            f"{mod_info['mod_dir']}\\Public\\{mod_info['mod_dir']}\\ClassDescriptions"
        )

    with open(os.path.join(file_path, "ClassDescriptions.lsx"), "w") as f:
        f.write(description_content)
