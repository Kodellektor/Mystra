# Mystra
A D&amp;D 5e Discord bot written in Python utilizing the [Discord.py](https://discordpy.readthedocs.io/en/stable/) wrapper. 

## Why Mystra?
 [Mystra](https://forgottenrealms.fandom.com/wiki/Mystra) is the goddess of Magic and Mysteries. Therefore she's the most appropriate deity to call upon when in doubt. Whether that doubt comes down to rule questions or simply finding out how much damage your rogue is going to dump on your DM's latest BBEG, you can ask Mystra and she will respond. (Otherwise feel free to open a ticket) Originally, I was planning on making Mystra a simple bot to handle dice rolling to maintain clarity in case someone couldn't reach [D&D Beyond](https://www.dndbeyond.com/). However, as I progress as a dev, I wanted to include additional features. 
## Upcoming features
I still have to completely finish the class that handles dice rolls to be able to apply multiple rolls(Advantage + Disadvantage) in addition to handling bonuses and automatic damage (i.e. +3, xdx + 4). Though while writing this it has ocurred to me that I have yet to handle some edge cases.

1. **Combat Tracker**: My party struggles with the myriad of things that need to be tracked in combat as they progress in experience. 
    To handle this I will:
    * Handle individual players and their assets
    * Keep track of the spells they take and spell slots expended (*We* don't really use spell materials, but adding them would be a good additional challenge)
    * Allow users to query and update their inventory
    * Use the embeds in discord.py to give brief explanations 

2. **Random Generators**: As a DM, this is a vital one. I'm actually super excited to see how to make these work. 
    What I'll focus on first:
    * Taverns: We all love a good place to bunker down after an adventure.
        * Tavern Keeper
        * Notable NPCs
        * Menu (Food & Drink) + Prices
        * Room Cost
        * Quests?
    * Shops: Both magical and secular.
        * Merchant NPC
        * Fellow Shoppers
        * Type of Inventory:
            * Magical
            * Consumable
            * Equipable
            * Secular
            * Etc...
    * Loot Tables:
        * Utilizing all the 5e loot tables though they should be categorized by:
            * CR
            * Rarity
            * Value
            * Context (Location, Monster, Combat Aftermath)
    * Encounter Tables:
        * These would be fantastic for keeping the party on their toes.
            * Should be able to import monster stat sheets. Would be cool if it sent a monster image to a channel.
    * Map Generator:
        * This one seems very difficult with python only, I'll have to revisit this one later.
3. **Music/Ambiance**: This one will be a challenge as I'm not too familiar with copyright free fantasy music and ambiance platforms.

4. **More?**
### What is Mystra built on?
1. **[Discord.py](https://discordpy.readthedocs.io/en/stable/)**: The API wrapper used to facilitate bot development by taking advantage of the python library [asyncio](https://docs.python.org/3/library/asyncio.html). 

2. **[Python](https://www.python.org/)**: I know I know, but I love the language. This project is also a great way for me to start implementing OOP design patterns so can't complain.

3. **[Discord](https://discord.com/company)**: My friends and I began playing on Discord during the pandemic and it's hard to migrate to another platform when Discord makes it so easy to love it.

4. **GitHub**: I've uploaded my code to GitHub to experience the pain of not knowing a Git command that could've saved me hours of hair tearing. 

5. **GNULinux**: Currently using a Fedora 38 image to familiarize myself with developing on a Linux machine.

6. **Some DataBase I'll decide on later**: Though currently looking into PostgreSQL.



