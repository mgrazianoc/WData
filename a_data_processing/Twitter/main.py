import a_data_processing.Twitter.api as api
import a_data_processing.Twitter.filters as filters
import a_data_processing.Twitter.writer as writer
import argparse


def construct():
    print("Follow these instructions to use YouTube API")
    main(None)


def main(parser, wdata_parser = None):
    if wdata_parser is None:
        raw_data = api.api_manager()
        data = filters.filter_manager(raw_data)
        writer.write_file(data)
    else:
        raw_data = Twitter.api.api_manager()
        data = Twitter.filters.filter_manager(raw_data)
        Twitter.writer.write_file(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)

