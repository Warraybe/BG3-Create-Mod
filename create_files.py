import os
import uuid

from class_info import base_classes


def create_meta(mod_info, uuids):
    meta_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="6" build="5" />
    <region id="Config">
        <node id="root">
            <children>
                <node id="Dependencies"/>
                <node id="ModuleInfo">
                    <attribute id="Author" type="LSWString" value="{mod_info["mod_author"]}"/>
                    <attribute id="CharacterCreationLevelName" type="FixedString" value=""/>
                    <attribute id="Description" type="LSWString" value="Adds the {mod_info['subclass']} subclass for {mod_info['main_class'].title()}."/>
                    <attribute id="Folder" type="LSWString" value="{mod_info["mod_name"]}"/>
                    <attribute id="GMTemplate" type="FixedString" value=""/>
                    <attribute id="LobbyLevelName" type="FixedString" value=""/>
                    <attribute id="MD5" type="LSWString" value=""/>
                    <attribute id="MainMenuBackgroundVideo" type="FixedString" value=""/>
                    <attribute id="MenuLevelName" type="FixedString" value=""/>
                    <attribute id="Name" type="FixedString" value="{mod_info['main_class'].title()} - {mod_info['subclass']}"/>
                    <attribute id="NumPlayers" type="uint8" value="4"/>
                    <attribute id="PhotoBooth" type="FixedString" value=""/>
                    <attribute id="StartupLevelName" type="FixedString" value=""/>
                    <attribute id="Tags" type="LSWString" value="Subclass"/>
                    <attribute id="Type" type="FixedString" value="Add-on"/>
                    <attribute id="UUID" type="FixedString" value="{uuids['mod_uuid']}"/>
                    <attribute id="Version64" type="int64" value="36028797018963968"/>
                    <children>
                        <node id="PublishVersion">
                            <attribute id="Version64" type="int64" value="36028797018963968"/> 
                        </node>
                        <node id="Scripts"/>
                            <node id="TargetModes">
                                <children>
                                    <node id="Target">
                                        <attribute id="Object" type="FixedString" value="Story"/>
                                    </node>
                                </children>
                            </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>"""

    meta_file = os.path.join(
        os.path.abspath(f"{mod_info['mod_name']}\\Mods\\{mod_info['mod_name']}"),
        "meta.lsx",
    )

    with open(meta_file, "w") as f:
        f.write(meta_content)


def create_scriptextender_files(mod_info, uuids):
    content = f"""{{
    "RequiredVersion": 14,
    "ModTable": "{mod_info['mod_name']}",
    "FeatureFlags": [
        "Lua"
    ]
}}"""

    file_path = os.path.abspath(
        f"{mod_info['mod_name']}\\Mods\\{mod_info['mod_name']}\\ScriptExtender"
    )

    with open(os.path.join(file_path, "Config.json"), "w") as f:
        f.write(content)

    file_path = os.path.abspath(
        f"{mod_info['mod_name']}\\Mods\\{mod_info['mod_name']}\\ScriptExtender\\Lua"
    )

    with open(os.path.join(file_path, "BootstrapServer.lua"), "w") as f:
        f.write("")

    with open(os.path.join(file_path, "BootstrapClient.lua"), "w") as f:
        f.write('Ext.Require("InitCompatibilityFramework.lua")\n')

    framework_content = f"""modGuid = "{uuids['mod_uuid']}"

if Ext.Mod.IsModLoaded("67fbbd53-7c7d-4cfa-9409-6d737b4d92a9") then
  local subClasses = {{
    {mod_info['mod_name']} = {{
      modGuid = modGuid,
      subClassGuid = "{uuids['subclass']}",
      class = "{mod_info['main_class'].lower()}",
      subClassName = "{mod_info['mod_name']}"
    }},
  }}

  local function OnStatsLoaded()
    Mods.SubclassCompatibilityFramework.Api.InsertSubClasses(subClasses)
  end

  Ext.Events.StatsLoaded:Subscribe(OnStatsLoaded)
end"""

    with open(os.path.join(file_path, "InitCompatibilityFramework.lua"), "w") as f:
        f.write(framework_content)


def create_localization(mod_info, uuids):
    localization_content = f"""<?xml version="1.0" encoding="utf-8"?>
<contentList>	
    <content contentuid="{uuids['subclass_name']}" version="1">{mod_info['subclass']}</content>
    <content contentuid="{uuids['subclass_description']}" version="1">Placeholder</content>
</contentList> """

    localization_file = os.path.join(
        os.path.abspath(f"{mod_info['mod_name']}\\Localization\\English"),
        mod_info["mod_name"].replace(" ", "") + ".xml",
    )
    with open(localization_file, "w") as f:
        f.write(localization_content)


def create_description(mod_info, uuids):
    description_content = f"""<?xml version="1.0" encoding="UTF-8"?>
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
</save>\n\n"""

    file_path = os.path.abspath(
        f"{mod_info['mod_name']}\\Public\\{mod_info['mod_name']}\\ClassDescriptions"
    )

    with open(os.path.join(file_path, "ClassDescriptions.lsx"), "w") as f:
        f.write(description_content)


def create_progression(mod_info, uuids):
    progression_content = f"""<?xml version="1.0" encoding="UTF-8"?>
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
</save>\n"""

    file_path = os.path.abspath(
        f"{mod_info['mod_name']}\\Public\\{mod_info['mod_name']}\\Progressions"
    )

    with open(os.path.join(file_path, "Progressions.lsx"), "w") as f:
        f.write(progression_content)


def create_subclass_files(mod_info, uuids):
    create_meta(mod_info, uuids)
    create_scriptextender_files(mod_info, uuids)
    create_localization(mod_info, uuids)
    create_description(mod_info, uuids)
    create_progression(mod_info, uuids)
