from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random
from random import randint

def get_date_hour (timestamp):
    start_time = 1388530800;
    day = int((timestamp-start_time)/(3600*24))
    hour = int((timestamp-start_time-day*3600*24)/3600)
    return (day, hour)


def check_phone_u_id (input, output):

    number_call = {};
    number_call_in = {};
    number_call_out = {};
    outcome = 0
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[1]);
        day, hour = get_date_hour(t_current)
        outcome = int(item[3])
        if (not (day,hour) in number_call):
            number_call[(day,hour)] = 0
            number_call_in[(day,hour)] = 0
            number_call_out[(day,hour)] = 0
        number_call[(day,hour)] = number_call[(day,hour)] + 1
        if (outcome == 1):
            number_call_in[(day,hour)] = number_call_in[(day,hour)] + 1
        else:
            number_call_out[(day,hour)] = number_call_out[(day,hour)] + 1
            
    for day, hour in number_call:
        output.write(str(day)+'\t'+str(hour)+'\t'+str(number_call[(day,hour)])+"\t"+str(number_call_in[(day,hour)])+"\t"+str(number_call_out[(day,hour)])+'\n')

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input",
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="input file name")
    parser.add_argument("-o", "--output",
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help="output")
       
    args = parser.parse_args()
    ids_dumped = check_phone_u_id(args.input,args.output)
    
    args.input.close()
    args.output.close()

if __name__ == "__main__":
    main()
