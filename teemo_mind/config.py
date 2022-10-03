"""Tell how Teemo need to be set up.
    """
import json
import os
import argparse

def new_config():
    config_object = {}
    with open(os.path.join("teemo_sketches", "config_base.json"), "r") as base_conf:
        config_object = json.load(base_conf)
    print("Could you describe the environnement? Teemo doesn't want to progress in the dark...", end="\n\n")
    choice = 4
    print(config_object)
    while choice not in ['0', '1', '2']:
        choice = input("Are we on Linux, MacOS or Windows? [0, 1 or 2]")
    if choice == '0':
        config_object = config_object["Linux"]
    if choice == '1':
        config_object = config_object["MacOS"]
    else:
        config_object = config_object["Windows"]
    os.system(config_object["clear_console"])

    with open("config.json", "w+") as config_file:
        json.dump(config_object, config_file, indent=6)
    print("Armed and ready.")

def config():
    if os.path.exists("config.json"):
        print("Configuration detected! If you want to change my inventory just delete the configuration file! -said teemo")
    else:
        print("No configuration detected! Tell me how to setup my inventory! -said teemo")
        new_config()
