import b_post_processing.config.parser as parser

def main():
    pass



def wdata_call_pp(task):
    if task == "xlsx":
        parser.construct("xlsx")
    elif task == "vector_list":
        parser.construct("vector_list")


if __name__ == "__name__":
    main()