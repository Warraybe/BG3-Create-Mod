# Baldur's Gate 3 - Create New Subclass Mod script  

This is a simple script that will create the folder and file structure for a new subclass mod for classes included in Baldur's Gate 3.

## Usage  

Run create_subclass.py and enter information as needed.

## Arguments  

**Mod author name** - Name of the Mod Author. This is shown in BG3MM metadata.
___
 
**Base class** - Base class that you are adding a subclass to.
Acceptable arguments: barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard
___

**Subclass name** - Name for the new subclass. This is shown in game, and used for BG3MM metadata.
___

Files are generated with new UUIDs, and Handles. Handles are only created for the Subclass name and a descrption placeholder, and are linked to ClassDescriptions. UUIDs are set for meta, ClassDescriptions, and Progressions and linked. Progressions only has the initial entry for subclass creation, and not for all levels where the subclass obtains new features.

Subclasses created using this are set to up with [BG3 Community Library](https://github.com/BG3-Community-Library-Team/BG3-Community-Library) and [Compatibility Framework](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework) as requirements.

Recommend installing [ImprovedUI ReleaseReady](https://www.nexusmods.com/baldursgate3/mods/366) so that the interface shows new subclasses easier.

## Folder and File structure
- ModauthornameSubclassname  
  - Localization  
    - English  
      - ModauthornameSubclassname.xml  
  - Mods  
    - ModauthornameSubclassname
      - ScriptExtender
        - Lua
          - BootstrapClient.lua
          - BootstrapServer.lua
          - InitCompatibilityFramework
            - InitCompatibilityFramework.lua 
        - Config.json
      - meta.lsx  
  - Public  
    - ModauthornameSubclassname  
      - ActionResourceDefinitions
      - Assets  
        - Textures  
          - Icons  
      - CharacterCreationPresets  
      - ClassDescriptions  
        - ClassDescriptions.lsx  
      - Content  
        - UI  
          - [PAK]_UI  
      - GUI  
      - Lists   
      - Progressions  
        - Progressions.lsx  
      - Stats
        - Data  
        - Generated  
