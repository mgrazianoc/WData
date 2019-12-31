from a_data_processing.YouTube.api import api_manager 
from a_data_processing.YouTube.writer import write_file 
from a_data_processing.YouTube.filters import filter_manager 
from wdata_config.decorators import func_logger 
from wdata_config.decorators import func_time_logger 
from wdata_config.loggers import create_info_log 

import a_data_processing.YouTube.config.parser as parser
    

@func_logger
@func_time_logger
def main(*args, **kwargs):
    logger = create_info_log(__name__)
    
    raw_data = api_manager(**kwargs)
    logger.info("Download of Raw Data completed")
        
    final_api_data = filter_manager(raw_data, **kwargs)
    logger.info("Data munging completed")
        
    write_file(final_api_data, **kwargs)
    logger.info("Data file written")


    
# this is just to handle WData calls
def wdata_call_p():
    kwargs = parser.construct()
    main(**kwargs)

    
if __name__ == "__main__":
    kwargs = parser.parsing_to_api()
    main(**kwargs)

    