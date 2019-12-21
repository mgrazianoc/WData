import subprocess
from a_data_processing.YouTube.main import construct as youtube_construct
from a_data_processing.Twitter.main import construct as twitter_construct
from a_data_processing.Yahoo.Yahoo_Weather.main import construct as yahoo_weather_construct

def wdata_manager(args):
    if args.youtube is True:
        youtube_construct()
    elif args.twitter is True:
        twitter_construct()
    elif args.yahoo is True:
        yahoo_weather_construct()
    elif args.xlsx is True:
        pass
    elif args.vector_dict is True:
        pass
    elif args.create is True:
        pass
    elif args.change is True:
        pass
    elif args.display is True:
        pass
    elif args.icon is True:
        pass
    elif args.open is True:
        pass
