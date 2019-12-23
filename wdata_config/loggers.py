import logging
import os


def create_info_log(name_logging):

    # setting up logger
    logger = logging.getLogger(name_logging)
    logger.setLevel(logging.INFO)
    formatting = logging.Formatter(
        "%(name)s:%(asctime)s:%(levelname)s:%(message)s")

    # creating specific file handler on g_logs
    directory = os.getcwd()
    file_handler = logging.FileHandler(f"{directory}/g_logs/youtube_api.log")
    file_handler.setFormatter(formatting)
    logger.addHandler(file_handler)

    # creating stream handler, simple format
    cmd_handler = logging.StreamHandler
    return logger