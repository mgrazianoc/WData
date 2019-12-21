import a_data_processing.YouTube.api
import a_data_processing.YouTube.writer
import a_data_processing.YouTube.filters

import argparse
import logging


def configuring_logging():
    # setting up logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatting = logging.Formatter(
        "%(name)s:%(asctime)s:%(levelname)s:%(message)s")
    
    # creating specific file handler on g_logs
    file_handler = logging.fileHandler("/g_logs/youtube_api.log")
    file_handler.setFormatter(formatting)
    logger.addHandler(file_handler)
    
    # creating stream handler, simple format
    cmd_handler = logging.StreamHandler()
    logger.addHandler(cmd_handler)
    
# ---------------------------------------------------------------------------------------------------------------------


# this function is intend to construct the YouTube API when it is called by WData, ex: routine on system tasks
def construct():
    configuring_logging()
    logger("Starting YouTube API construct")
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
        category = input()
        entries = {"task": task,
                   "category": category,
                   "country": country,
                   "output": "a_data_processing\output\YouTube"}
        logger(f"Starting process on {entries['task']}, category {entries['category']} for country {entries['country']}")
    else:
        task = "categories"
        entries = {"task": task,
                   "country": country,
                   "output": "a_data_processing\output\YouTube"}
        logger(f"Starting process on {entries['task']} for country {entries['country']}")
        
    main(None, entries)


def main(main_parser, wdata_parser=None):
    if wdata_parser is None:
        raw_data = a_data_processing.YouTube.api.api_manager(main_parser)
        logger("Download of Raw Data completed")
        final_api_data = a_data_processing.YouTube.filters.filter_manager(raw_data, main_parser)
        logger("Data munging completed")
        a_data_processing.YouTube.writer.write_file(final_api_data, main_parser)
        logger("Data file written")
    else:
        raw_data = a_data_processing.YouTube.api.api_manager(wdata_parser)
        logger("Download of Raw Data completed")
        final_api_data = a_data_processing.YouTube.filters.filter_manager(raw_data, wdata_parser)
        logger("Data munging completed")
        a_data_processing.YouTube.writer.write_file(final_api_data, wdata_parser)
        logger("Data file written")

        
if __name__ == "__main__":
    configuring_logging()
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
        default='a_data_processing\output\YouTube'
    )
    parser.add_argument(
        '--name', '-n',
        help='optional file name which the data will be written',
        type=str,
        nargs=1,
        default='standard'
    )
    args = parser.parse_args()
    main(args)
