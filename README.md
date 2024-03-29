# Baldur's Gate 3 - Create New Class/Subclass Mod script  

This is a simple script that will create the folder and file structure for a new custom class or subclass mod for classes included in Baldur's Gate 3.

## Usage  

Run **create_mod.py** and enter information as needed.

Custom class mod creation still WIP and will not function. At this time only Subclass feature works.

##  Class Mod Arguments 
**Mod author name** - Name of the Mod Author. This is shown in BG3MM metadata.

**Class name** - Name for the new class. This is shown in game, and used for BG3MM metadata.

**Feature subclasses** - y/n. Does the new class have subclasses.

**Subclass level** - What level do subclasses become available. 

**Subclass name(s)** - Comma separated list of subclasses to add. This is shown in game.

##  Subclass Mod Arguments  

**Mod author name** - Name of the Mod Author. This is shown in BG3MM metadata.
 
**Main class** - Main class that you are adding a subclass to.  
Acceptable arguments: barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard

**Subclass name** - Name for the new subclass. This is shown in game, and used for BG3MM metadata.

Files are created for subclass injection and linked via [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) using BG3 Community Library and Compatibility Framework.

## Requirements and Recommendations  
Custom classes are created not requiring any dependencies.

Subclasses created are set to up with [BG3 Community Library](https://github.com/BG3-Community-Library-Team/BG3-Community-Library),  [Compatibility Framework](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework), and [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) as requirements.

Recommend installing [ImprovedUI ReleaseReady](https://www.nexusmods.com/baldursgate3/mods/366) so that the interface shows new classes and subclasses easier. Also recommend installing ImprovedUI Assets from the optional files for ImprovedUI ReleaseReady to use a custom class icon.

## Folder and File structure
Files are generated with UUIDs, and Handles. Handles are only created for the Class/Subclass name(s) and a description placeholder, and are linked to ClassDescriptions. UUIDs are set for meta, ClassDescriptions, and Progressions and linked. Progressions only has the initial entry for class/subclass creation, and not for all levels where the class/subclass obtains new features.

- Modauthorname**Subclass**name / Modauthorname**Class**name
  - Localization  
    - English  
      - Modauthorname**Subclass**name.xml / Modauthorname**Class**name.xml
  - Mods  
    - Modauthorname**Subclass**name / Modauthorname**Class**name
      - ScriptExtender 
        - Lua
          - BootstrapClient.lua
          - BootstrapServer.lua
          - InitCompatibilityFramework
            - InitCompatibilityFramework.lua **(Subclass only)**
        - Config.json
      - meta.lsx  
  - Public  
    - Modauthorname**Subclass**name / Modauthorname**Class**name  
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
