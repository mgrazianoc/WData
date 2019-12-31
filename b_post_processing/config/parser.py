import argparse
import os


def parsing_to_wdpp():
    parse = argparse.ArgumentParser()
    
    parse.addArgument(
    "--xlsx", "-x",
    help="create Excel samples from data",
    action="store_true"
    )
    parse.addArgument(
    "--vector_list", "-v",
    help="format default WData data into a vector_list form",
    action="store_true"
    )
    

def construct(task):
    if task == "xlsx":
        print("Follow these instructions to import a sample to Excel")
        print("From which API the data will be samples?")
        print("[1] YouTube")
        print("[2] Twitter")
        print("[3] YahooWeather")
        api = input()