import argparse
import json
import os

from teemo_heart.ascii import teemo
from teemo_mind.config import config
from teemo_mind.menu import main_menu
from teemo_mind.engine import Engine
parser = argparse.ArgumentParser()




if __name__ == "__main__":
    print(teemo, end="\n\n\n")
    config()
    print("hop hop hop!")
    with open("config.json", "r") as config:
        env = json.load(config)
    teemo = Engine(env)
    teemo.main_loop()
