import argparse


def command_line_parse():

    # basic parser functionality
    parser = argparse.ArgumentParser(
        prog="WData",
        description="A Python Web Scrapping Data Manipulation software.",
        epilog="Where do we start?"
    )
    parser.add_argument(
        "--version", "-v",
        help="show WData version",
        action="version",
        version="WData alpha"
    )
    parser.add_argument(
        "--icon", "-i",
        help="create a icon shortcut to WData in a specific directory",
        action="store_false",
        default=False
    )
    parser.add_argument(
        "--open", "-o",
        help="open WData folder on system to work with its files",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "--shell",
        help="initiate WData interactive shell",
        action="store_true",
        default=False
    )
    
    # creating a fork for WData different tasks
    sub_parser = parser.add_subparsers(
        title="WData tools",
        description="Try [task] -h for more help options!"
    )
    

# ---------------------------------------------------------------------------------------------------------------------

    # process task
    process = sub_parser.add_parser(
        "process",
        help="initiate WData process data tools, such as APIs")

    process.add_argument(
        "--youtube", "-y",
        help="initiate YouTube API",
        action="store_true"
    )

    process.add_argument(
        "--twitter", "-t",
        help="initiate twitter API",
        action="store_true"
    )

    process.add_argument(
        "--yahoo", "-yh",
        help="initiate Yahoo Weather API",
        action="store_true"
    )

# ---------------------------------------------------------------------------------------------------------------------

    post_process = sub_parser.add_parser(
        "post_process",
        help="initiate post process data tools, such as export do xlsx and extra data munging options"
    )

    post_process.add_argument(
        "--xlsx", "-x",
        help="export a data sample from output files to xlsx (Excel) format",
        action="store_true"
    )

    post_process.add_argument(
        "--vector_dict", "-v",
        help="transform default API outputs in a vector dictionary form",
        action="store_true"
    )

# ---------------------------------------------------------------------------------------------------------------------

    analsysis = sub_parser.add_parser(
        "analysis",
        help="interface to initiate R scripts for data analysis"
    )

# ---------------------------------------------------------------------------------------------------------------------

    # routine tasks
    routine = sub_parser.add_parser(
        "routine",
        help="routine tool allows to create, change or see available WData system routines"
    )
    routine.add_argument(
        "--create", "-c",
        help="create routines for WData",
        action="store_true"
    )
    routine.add_argument(
        "--change", "-ch",
        help="change routines running in WData",
        action="store_true"
    )
    routine.add_argument(
        "--display", "-d",
        help="display WData routines running as well as their logs",
        action="store_true"
    )

    args = parser.parse_args()

# ---------------------------------------------------------------------------------------------------------------------

    # post analysis tasks

    post_analysis = sub_parser.add_parser(
        "post_analysis",
        help="post analysis interface for reports usage"
    )

    return args
