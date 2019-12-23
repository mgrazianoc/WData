from wdata_config.parser import command_line_parse
from wdata_config.manager import wdata_manager
import wdata_config.parser as parser



def main(tasks):
    wdata_manager(tasks)


if __name__ == "__main__":
    args = command_line_parse()
    main(args)

