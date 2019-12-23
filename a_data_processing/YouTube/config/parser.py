import argparse
import os
from wdata_config.loggers import create_info_log as create_info_log


logger = create_info_log(__name__)


# function to handle direct call from terminal with argparse
def parsing_to_api():
    directory = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--task', '-t',
        help='options: category data with -d category, or videos data with -v videos',
        type=str,
        nargs=1,
        default='trends'
    )
    parser.add_argument(
        '--category', '-ct',
        help='category which the API will bring data. Ex: -c 3',
        type=int,
        nargs=1,
        default=0
    )
    parser.add_argument(
        '--country', '-c',
        help="the ISO 3166-1 Alpha 2 country code which the API will bring data. Ex: BR",
        type=str,
        nargs=1,
        default="BR"
        )
    parser.add_argument(
        '--output_dir', '-o',
        help='Path to save the outputted files in',
        type=str,
        nargs=1,
        default=f'{directory}\a_data_processing\output\YouTube'
    )
    parser.add_argument(
        '--name', '-n',
        help='optional file name which the data will be written',
        type=str,
        nargs=1,
        default='standard'
    )
    parser.add_argument(
        '--routine', '-r',
        help='basically, use to mark if the call is a routine programmed',
        type=str,
        nargs=1,
        default='No'
    )
    args = parser.parse_args()
    
    # the reason to parse argparse as keywords it's because not always this API will be called from terminal
    
    return{
        "task": args.task,
        "category": args.category,
        "country": args.country,
        "name": args.name,
        "output":f'{directory}\a_data_processing\output\YouTube',
        "routine":args.routine
        }

    
# this here is for when WData is called first from terminal
def construct():
    directory = os.getcwd()
    logger.info("Starting YouTube API construct")
    print("Follow these instructions to use YouTube API")
    
    print("Which task will the API use? Choose a character:")
    print("[t] - trends videos information")
    print("[c] - categories' list information")
    task = input()

    print("Which country the data will be Fetch? Use ISO 3166-1 Alpha 2 code")
    country = input()

    if task == "t":
        task = "trends"
        print("Which category of videos will the API fetch? Choose a number:")
        print("\t [0] - All\n"
              "\t [10] - Music \n"
              "\t [20] - Gaming \n"
              "\t [25] - News & Politics")
        category = int(input())
        logger.info(f"Starting process on {task}, category {category} for country {country}")
        
        return{
            "task": task,
            "category": category,
            "country": country,
            "output":f'{directory}\a_data_processing\output\YouTube',
            "routine":'No'
        }
    else:
        task = "categories"
        logger.info(f"Starting process on {task} for country {country}")
        
        return{
            "task": task,
            "country": country,
            "output":f'{directory}\a_data_processing\output\YouTube',
            "routine":'No'
        }