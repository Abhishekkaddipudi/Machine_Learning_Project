import sys

class HousingException(Exception):
    def __init__(self, error_message:Exception,err_details:sys) -> None:
       Exception(error_message)
       self.error_message=HousingException.get_detailed_eror_message(error_message=error_message,err_details=err_details)


    @staticmethod
    def get_detailed_eror_message( error_message:Exception,err_details:sys)-> str:

        """
        error_message: Exception object
        error_detail: object of sys module
        
        """
        _,_,exec_tb=err_details.exc_info()
        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename
        error_message=f"Error Occured in Script: [{file_name}] as line numbver: [{line_number}] error message: [{error_message}]"
     
        return error_message
    
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
        