import Twitter.api
import Twitter.filters
import Twitter.writer
import argparse


def main(parser):
    raw_data = Twitter.api.api_manager()
    data = Twitter.filters.filter_manager(raw_data)
    Twitter.writer.write_file(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)

