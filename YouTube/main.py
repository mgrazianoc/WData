import YouTube.api
import YouTube.writer
import YouTube.filters

import argparse


def main(parser):
    raw_data = YouTube.api.api_manager(parser)
    final_api_data = YouTube.filters.filter_manager(raw_data, parser)
    YouTube.writer.write_file(final_api_data, parser)
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--task', '-t',
        help='options: category data with -d category, or videos data with -d videos',
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
        default='/output'
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
