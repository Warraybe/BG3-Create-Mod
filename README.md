# Baldur's Gate 3 - Create New Class/Subclass Mod script  

This is a simple script that will create the folder and file structure for a new custom class or subclass mod for classes included in Baldur's Gate 3.

## Usage  

Run create_mod.py and enter information as needed.

Class mod creation still WIP and will not function. At this time only Subclass feature works.

##  Subclass Mod Arguments  

**Mod author name** - Name of the Mod Author. This is shown in BG3MM metadata.
 
**Base class** - Base class that you are adding a subclass to.
Acceptable arguments: barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard

**Subclass name** - Name for the new subclass. This is shown in game, and used for BG3MM metadata.

Files are generated with new UUIDs, and Handles. Handles are only created for the Subclass name and a descrption placeholder, and are linked to ClassDescriptions. UUIDs are set for meta, ClassDescriptions, and Progressions and linked. Progressions only has the initial entry for subclass creation, and not for all levels where the subclass obtains new features.

Files are also created for subclass injection and linked via [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) using BG3 Community Library and Compatibility Framework.

## Requirements and Recommendations  
Custom classes are created not requiring any dependencies.

Subclasses created using this are set to up with [BG3 Community Library](https://github.com/BG3-Community-Library-Team/BG3-Community-Library) and [Compatibility Framework](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework) as requirements.

Recommend installing [ImprovedUI ReleaseReady](https://www.nexusmods.com/baldursgate3/mods/366) so that the interface shows new classes and subclasses easier. Also recommend installing ImprovedUI Assets from the optional files for ImprovedUI ReleaseReady to use a custom class icon.

## Folder and File structure
- ModauthornameSubclassname / ModauthornameClassname
  - Localization  
    - English  
      - ModauthornameSubclassname.xml / ModauthornameClassname.xml
  - Mods  
    - ModauthornameSubclassname / ModauthornameClassname
      - ScriptExtender
        - Lua
          - BootstrapClient.lua
          - BootstrapServer.lua
          - InitCompatibilityFramework
            - InitCompatibilityFramework.lua (Subclass only)
        - Config.json (Subclass only)
      - meta.lsx  
  - Public  
    - ModauthornameSubclassname / ModauthornameClassname  
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
