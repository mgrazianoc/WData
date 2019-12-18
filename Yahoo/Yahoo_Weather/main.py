import Yahoo.Yahoo_Weather.api
import Yahoo.Yahoo_Weather.writer
import argparse

# for now, this API only works with Brazil. The reason for that is some issues with translation on the Yahoo API


def main(parser):
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
