#!/usr/bin/env python3

import os
import shutil
import configparser

lineSeperator = "-" * shutil.get_terminal_size().columns

def printCheatDocList(docsPath):
    parser = configparser.ConfigParser()
    cheats = []

    # Get all files in cheat docs dir
    for c in os.listdir(docsPath):
        # Skip "non ini files"
        if not c.endswith(".ini"): continue

        parser.read(docsPath + c)
        
        cheat = {
            "name": parser.get("cheat", "name"),
            "description": parser.get("cheat", "description")
        }

        cheats.append(cheat)

    cheatsStr = "".join(f"{c['name']}\t=> {c['description']}\n" for c in cheats)

    print(f"{lineSeperator}\nList of available cheat docs:\n\n{cheatsStr}")

    return

def parseAndPrintIniDoc(docPath=str):
    parser = configparser.ConfigParser()

    # Read ini file
    parser.read(docPath)

    # Print "about"
    sections = parser.sections()
    sections.remove("cheat")

    about = f"""{lineSeperator}
Cheat: {parser.get("cheat", "name")}
Description: {parser.get("cheat", "description")}
Sections: {sections}
Source: {docPath}
{lineSeperator}"""
    
    print(about)

    # Print contect
    for section in parser.sections():
        if section == "cheat": continue
        print(f"\n[{section}]")
        for key, value in parser.items(section):
            print(f"{key} => {value}")
    
    return
