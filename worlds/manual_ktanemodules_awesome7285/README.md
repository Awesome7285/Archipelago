# Keep Talking and Nobody Explodes Modded Archipelago Manual
Built upon Manual Stable [v20250813](https://github.com/ManualForArchipelago/Manual/releases/tag/manual_stable_20250813)

## Prerequisites
You will need a copy of [Keep Talking and Nobody Explodes](https://store.steampowered.com/app/341800/Keep_Talking_and_Nobody_Explodes/) and whatever mods you wish to play with installed. It is recommended to subscribe to the complete collection and enable demand based module loading.

## How it Works
- Depending on YAML settings, modules are randomly chosen to be added to your seed.
- Each module counts as both an item and a location. You need to receive the module's item to complete its location by solving it.
- You may solve these modules however you like, this manual is intended to be used as a way to learn new modules.

## Options
- total_modules: How many module items/locations you want in your game.
- starting_modules: How many module items you start with.
- completion_percentage: The percentage of modules needed to be obtained in order to goal. Example: if total_modules is set to 50 and completion_percentage is set to 80, then you need to solve 80% of the 50 modules which is equal to 40.
- module_vetos: Use this to remove modules from being added to your game. If you're looking to learn some simpler modules, I'd use this option to veto extreme modules.
- module_forces: Use this to force modules in your game. Modules added here will result in one less random module being added. You can use this option to create a game with only forced modules and remove random modules entirely if the length is equal to total_modules.
- _seed: The randomizer seed. Change this if you want the same random modules as a previously made seed.

## How to Play
- Installing the .apworld, generating a YAML and connecting via the manual client is the same as normal.
- Open Keep Talking and Nobody Explodes with mods installed.
- Load modules in freeplay via the mod selector.
- Click off the location checks once a module has been solved.