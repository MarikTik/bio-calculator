#!/usr/bin/env python3
import sys
from json import dump
from pathlib import Path

default_links_path = "data/links/links.txt"

def main():
     if len(sys.argv) == 1:
          links_file_dir = ""
          links_file_path = default_links_path   
     elif len(sys.argv) == 2:
          links_file_dir = sys.argv[1]
     elif len(sys.argv) == 3:
          links_file_dir = sys.argv[1]
          links_file_path = sys.argv[2]
     else:
          print("Usage: python3 parse_links.py [links_dir] [links_path]")
          sys.exit(1)
     
     with open(links_file_path) as links_file:
          entries = filter(lambda str: str[0].isalpha(), links_file.readlines())
          entries = map(lambda str: str.strip(), entries)

          header = ""
          json = dict()
          for entry in entries:
               if entry.startswith("https://"):
                    json[header] = entry
                    header = ""
               else:
                    header += entry
     if links_file_dir == "":
          links_file_dir = Path(links_file_path).parent

     with open(Path.joinpath(links_file_dir, "links.json"), "w") as json_file:
          dump(json, json_file, indent=4)

if __name__ == '__main__':
     main()
         