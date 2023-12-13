'''
>>> LOGFILE_STANDARD
'logging_formatter-standard.txt'
>>> LOGFILE_CSV
'logging_formatter-csv.txt'
>>> LOGFILE_JSON
'logging_formatter-json.txt'

These lines reset the log files to empty for each test run.
>>> truncate_file(LOGFILE_STANDARD)
>>> truncate_file(LOGFILE_CSV)
>>> truncate_file(LOGFILE_JSON)

>>> my_logger.name
'root'
>>> my_logger.warning("There's a loose board right there.")
>>> my_logger.error("Auxiliary disk full")
>>> my_logger.info("Vancouver Island is 460 km in length.")

>>> print_file(LOGFILE_STANDARD)
WARNING:root:There's a loose board right there.
ERROR:root:Auxiliary disk full
INFO:root:Vancouver Island is 460 km in length.

>>> print_file(LOGFILE_CSV)
root,WARNING,There's a loose board right there.
root,ERROR,Auxiliary disk full
root,INFO,Vancouver Island is 460 km in length.

>>> print_file(LOGFILE_JSON)
{"logger":"root", "level":"WARNING", "message":"There's a loose board right there."}
{"logger":"root", "level":"ERROR", "message":"Auxiliary disk full"}
{"logger":"root", "level":"INFO", "message":"Vancouver Island is 460 km in length."}
'''

LOGFILE_STANDARD = 'logging_formatter-standard.txt'
LOGFILE_CSV = 'logging_formatter-csv.txt'
LOGFILE_JSON = 'logging_formatter-json.txt'

def truncate_file(path):
    # Make sure a file is empty.
    with open(path, 'w'): pass

def print_file(path):
    print(open(path).read(), end="")

# Write your code here:
import logging

my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)

# standard logfile output
log_file_standard_handler = logging.FileHandler(LOGFILE_STANDARD)
log_file_standard_handler.setLevel(logging.INFO)

# csv logfile output
log_file_csv_handler = logging.FileHandler(LOGFILE_CSV)
log_file_csv_handler.setLevel(logging.INFO)

# json logfile output
log_file_json_handler = logging.FileHandler(LOGFILE_JSON)
log_file_json_handler.setLevel(logging.INFO)

my_logger.addHandler(log_file_standard_handler)
my_logger.addHandler(log_file_csv_handler)
my_logger.addHandler(log_file_json_handler)


fmt_standard = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
# WARNING:root:There's a loose board right there.
log_file_standard_handler.setFormatter(fmt_standard)

fmt_csv = logging.Formatter('root,%(levelname)s,%(message)s')
# root,WARNING,There's a loose board right there.
log_file_csv_handler.setFormatter(fmt_csv)

fmt_json = logging.Formatter('{"logger":"root", "level":"%(levelname)s", "message":"%(message)s"}')
# {"logger":"root", "level":"WARNING", "message":"There's a loose board right there."}
log_file_json_handler.setFormatter(fmt_json)



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2020 Aaron Maxwell. All rights reserved.
