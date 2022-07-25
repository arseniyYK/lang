import subprocess
import time
import functions
import json

try:
	from termcolor import colored
except:
	print("Termcolor module not installed. Installing...")
	time.sleep(0.5)
	subprocess.run("pip3 install termcolor", shell=True)
	print("Dependencies successfully installed.")
	time.sleep(1)
	functions.clear()
	from termcolor import colored



data = []
version = "0.0.0"

with open("data.json", "r") as f:
    data = json.load(f)
    version = data["version"]


def main():
    while True:
        functions.clear()

        print(colored(f" --- lang v{version} ---", "green"))
        print("1. Learn words")
        print("2. View words")
        print("3. Add words (WIP)")
        print("4. Settings")
        print("Type exit to quit.")

        usrinput = input(colored(" ==> ", "cyan"))

        if usrinput == "1":
            functions.learn_words()

        elif usrinput == "2":
            functions.view_words()

        elif usrinput == "3":
            functions.add_words()

        elif usrinput == "4":
            functions.settings_change()

        elif usrinput == "exit" or usrinput == "quit":
            exit()

        elif usrinput == "clear":
            pass

        else:
            print(colored("error", "red") + f": {usrinput}: invalid option.")


main()
