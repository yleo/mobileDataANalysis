from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random
from random import randint

def check_phone_u_id (input, output):

    bs = {}
    number_call = 0;
    duration_ave = 0;
    duration = 0;
    interarr_duration = 0;
    bs1 = 0;
    bs2 = 0;
    user_call_in_switch = []
    bs_current = 0;
    bs_previous = 0;
    switch_number = 0;
    switch_duration = 0;
    call_in_switch = 0;
    call_in_switch_ave = 0;
    interswitch_duration = 0;
    switch_previous = 0;
    t_current = 0;
    t_previous=0;
    u_current = 0;
    u_previous = 0;
    u_begin = 0;
    u_end = 0;
    maxi = 0;
    random_switch = 0;
    bs = {}
    best 
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[0]);
        u_current = item[1];
        bs_current = int(item[2]);
        duration = int(item[4]);
        if (u_previous == u_current):
            if (not bs_current in bs):
                bs[bs_current] = 1
        else:
            maxi = -1
            best_bs = 0
            for i in bs:
                if (bs[i]>maxi):
                    maxi = bs[i]
                    best_bs = i
            if (maxi>0):
                output.write(str(best_bs)+'\n')
        t_previous = t_current;
        bs_previous = bs_current;
        u_previous = u_current;

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
