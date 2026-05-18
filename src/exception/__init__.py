import sys
import logging
def error_message_detail(error:Exception,error_detail:sys)->str:
    _, _, exc_tb = error_detail.exc_info()
    #getting the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number=exc_tb.tb_lineno
    error_message=f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    #logging the error message
    logging.error(error_message)
    return error_message
class Myexpection(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self)->str:
        return self.error_message
        