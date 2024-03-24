import json
import os


def create_scriptextender_files(mod_info, uuids):
    content = f'''{{
    "RequiredVersion": 14,
    "ModTable": "{mod_info['mod_dir']}",
    "FeatureFlags": [
        "Lua"
    ]
}}'''

    file_path = os.path.abspath(f"{mod_info['mod_dir']}\\Mods\\{mod_info['mod_dir']}\\ScriptExtender")

    with open(os.path.join(file_path, "Config.json"), "w") as f:
        f.write(content)

    file_path = os.path.abspath(
        f"{mod_info['mod_dir']}\\Mods\\{mod_info['mod_dir']}\\ScriptExtender\\Lua")

    with open(os.path.join(file_path, "BootstrapServer.lua"), "w") as f:
        f.write("")

    with open(os.path.join(file_path, "BootstrapClient.lua"), "w") as f:
        f.write('Ext.Require("InitCompatibilityFramework.lua")\n')

    framework_content = f'''modGuid = "{uuids['mod_uuid']}"

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
end'''

    with open(os.path.join(file_path, "InitCompatibilityFramework.lua"),
              "w") as f:
        f.write(framework_content)
