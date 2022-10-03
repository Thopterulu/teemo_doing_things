import os
import time
from teemo_heart.voice_lines import BAN_EXIT

def writer_tool(text: str):
    list_chars = list(text)
    for a_char in list_chars:
        print(a_char, end='', flush=True)
        time.sleep(0.01)
    print()

class Engine:
    def __init__(self, env: dict) -> None:
        self.env = env

    def main_loop(self):
        os.system(self.env["clear_console"])
        self.main_loop_choices()

    def main_loop_choices(self):
        choice = 0
        writer_tool("Hello, I'm Teemo! A yordle that play with shrooms. What do you want me to do?")
        time.sleep(0.3)
        writer_tool("""
We can:
1. Plant new mushrooms.
2. Use a mushroom. (Not implemented yet.)
3. Uproot some mushrooms. (Not implemented yet.)
4. Say goodbye !""")
        while choice not in ['1', '2', '3', '4']:
            choice = input()
        if choice == '1':
            pass
        if choice == '2':
            pass
        if choice == '3':
            pass
        if choice == '4':
            self.exit()

    def plant_shrooms(self):
        # shrooms accessible are in a json file with the link/ action to make in order to download/install them
        # you can only install if the configuration is full

    def exit(self):
        writer_tool(BAN_EXIT)
        return
