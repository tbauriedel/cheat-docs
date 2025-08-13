#!/usr/bin/env python3

from argparse import ArgumentParser
from lib import parser
import os

def main():
    argparser = ArgumentParser()

    argparser.add_argument("--list", dest="list", action="store_true", required=False, help="list available cheat docs")
    argparser.add_argument("cheatdoc", nargs='?', help="the cheat doc you want to see")

    args = argparser.parse_args()

    # Print available cheat docs
    if args.list:
        argparser.print_help()
        parser.printCheatDocList(os.path.dirname(os.path.abspath(__file__)) + "/docs/")
        exit(0)            

    # Validate if requested cheat is available
    cheatDocPath = os.path.dirname(os.path.abspath(__file__)) + "/docs/" + args.cheatdoc + ".ini"
    if not os.path.isfile(cheatDocPath):
        print("Cheat for '" + args.cheatdoc + "' not found. Cheat doc file does not exist")
        exit(1)
    
    parser.parseAndPrintIniDoc(cheatDocPath)

if __name__ == "__main__":
    main()