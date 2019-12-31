import subprocess
from a_data_processing.YouTube.main import wdata_call_p
from b_post_processing.wdata_pp import wdata_call_pp
from cmd import Cmd

def wdata_manager(args):
    try:
        if args.shell is True:
            cmd_manager()
        elif args.youtube is True:
            wdata_call_p()
    except AttributeError:
        print("No input found")
        cmd_manager()

        
def cmd_manager():
    print("Initiating interactive WData shell")
    print("Try typing in 'help' for help")
    
    class WData_shell(Cmd):
        
        def do_help(self, arg):
            pass
        
        def do_process(self, arg):
            wdata_call_p()
        
        def do_post_process(self, arg):
            pass
        
        def do_analysis(self, arg):
            pass
        
        def do_data_base(self, arg):
            pass
        
        def do_post_analysis(self, arg):
            pass
    
    shell = WData_shell()
    shell.cmdloop()