from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random
from random import randint

def get_date_hour (timestamp):
    start_time = 1366020000;
    day = int((timestamp-start_time)/(3600*24))
    hour = int((timestamp-day*3600*24)/7200))
    return (day, hour)


def check_phone_u_id (input, output):

    bs = {}
    number_call = 0;
    duration_ave = 0;
    duration = 0;
    interarr_duration = 0;
    bs1 = 0;
    bs2 = 0;
    number_calls = [0,0,0,0,0,0,0,0,0,0,0,0]
    number_calls_in = [0,0,0,0,0,0,0,0,0,0,0,0]
    number_calls_out = [0,0,0,0,0,0,0,0,0,0,0,0]
    duration_calls = [0,0,0,0,0,0,0,0,0,0,0,0]
    duration_calls_number = [0,0,0,0,0,0,0,0,0,0,0,0]
    bs_current = 0;
    t_current = 0;
    u_current = 0;
    time_var = 1388530800;
    period = 7200
    day = 0
    hour = 0
    hour2 = 0
    in_out = 0
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[0]);
        u_current = item[1];
        bs_current = int(item[2]);
        in_out = int(item[3]);
        duration = int(item[4]);
        day, hour = get_date(t_current)
        hour2 = int(hour/2)
        durations_calls[hour2]=durations_calls[hour2]*(float(duration_calls_number[hour2])/(duration_calls_number[hour2]+1))+duration*(float(duration_calls_number[hour2])/(duration_calls_number[hour2]+1))
        duration_calls_number[hour2]=duration_calls_number[hour2]+1
        number_calls[hour2]=number_calls[hour2]+1
        if (in_out==1):
            number_calls_in[hour2]=number_calls_in[hour2]+1
        else:
            number_calls_out[hour2]=number_calls_out[hour2]+1
        
        for i in range(0,12):
            output.write(str(i)+'\t'+str(number_calls[i])+'\t'+str(number_calls_in[i])+'\t'+str(number_calls_out[i])+'\t'+str(int(durations_calls[hour2]))+'\n')

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
