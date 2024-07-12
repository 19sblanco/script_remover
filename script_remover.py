#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup

"""
This program removes Javascript from webpage

Input: an html file path
Output: an html file with [<script>, </script>] removed and everything in between them
"""

def main():
    file_path = ""
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    while True:
        if not file_path:
            file_path = input("Enter a file path\n")
        if not file_path.endswith(".html"):
            print("file extension must be .html")
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
                elements = soup.find_all("script")
                for e in elements:
                    e.decompose()

            with open("(1)" + file_path, "w", encoding="utf-8") as file:
                file.write(str(soup))

            print("Success!")
            break
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except PermissionError:
            print(f"Error: You don't have permission to access '{file_path}'.")
        except IOError as e:
            print(f"Error: An I/O error occurred: {e}")
        pass


main()
