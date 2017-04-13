from time import *
import os

def init_log(ID):
    filename = "runlog_" + str(ID) + ".log"
    program_log = open(filename, 'w')
    program_log.write("Log File for {} in program {}\n{}\n"
                      .format(ID, os.path.basename(__file__), "/" * 100))
    write_to_log(program_log, "Log Started")
    return program_log

def write_to_log(log, string):
    logtime = strftime("[%H:%M:%S %d/%m/%Y] ", gmtime())
    log.write(logtime + string + '\n')
    
def close_log(log):
    write_to_log(log, "Log Ended")
    log.close()
    
'''#Test case   
log = init_log(0)
write_to_log(log, "Error 1")
write_to_log(log, "Error 2")
write_to_log(log, "Error 3")
write_to_log(log, "Error 4")
close_log(log)'''