import Yahoo.Yahoo_Weather.api
import Yahoo.Yahoo_Weather.writer
import argparse

# for now, this API only works with Brazil. The reason for that is some issues with translation on the Yahoo API


def construct():
    print("Follow these instructions to use YouTube API")
    print("Which country the data will be Fetch? Use ISO 3166-1 Alpha 2 code")


def main(parser, wdata_parser=None):
    data = Yahoo.Yahoo_Weather.api.api_manager(parser)
    Yahoo.Yahoo_Weather.writer.write_file(data, parser)

    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--country", "-c",
        help="country which states will be search for",
        nargs=1,
        type=str,
        default='BR'
    )
    parser.add_argument(
        "--task", "-t",
        help="task which will be made. -t weather or -t woeid",
        nargs=1,
        type=str,
        default='woeid'
    )
    args = parser.parse_args()
    main(args)
