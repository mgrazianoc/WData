import a_data_processing.YouTube.api
import a_data_processing.YouTube.writer
import a_data_processing.YouTube.filters

import argparse


def main(main_parser, wdata_parser=None):
    if wdata_parser is None:
        raw_data = a_data_processing.YouTube.api.api_manager(main_parser)
        final_api_data = a_data_processing.YouTube.filters.filter_manager(raw_data, main_parser)
        a_data_processing.YouTube.writer.write_file(final_api_data, main_parser)
    else:
        raw_data = a_data_processing.YouTube.api.api_manager(wdata_parser)
        final_api_data = a_data_processing.YouTube.filters.filter_manager(raw_data, wdata_parser)
        a_data_processing.YouTube.writer.write_file(final_api_data, wdata_parser)


if __name__ == "__main__":

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
        default='C:/Users/maruc/OneDrive/Área de Trabalho/Data Science/YouTube/output'
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
else:
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
        print("[0] - All\n"
              "[10] - Music \n"
              "[20] - Gaming \n"
              "[25] - News & Politics")
        category = input()
        entries = {"task": task,
                   "category": category,
                   "country": country,
                   "output": "C:/Users/maruc/OneDrive/Área de Trabalho/Data Science/YouTube/output"}
    else:
        task = "categories"
        entries = {"task": task,
                   "country": country,
                   "output": "C:/Users/maruc/OneDrive/Área de Trabalho/Data Science/YouTube/output"}

    main(None, entries)
