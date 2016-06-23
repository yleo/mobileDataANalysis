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
    user_interswitch = []
    yep = 0
    go = 0
    time_var = 1366020000;
    period = 7200;
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[0]);
        u_current = item[1];
        bs_current = int(item[2]);
        duration = int(item[4]);
        if (u_previous == u_current):
            number_call = number_call+1
            #switch number et duration
            if (t_current > time_var and t_current < time_var+period):
                go = go+1
                if (t_previous > time_var and t_previous < time_var+period):
                    user_interswitch.append(t_current-t_previous);
            if (bs_current != bs_previous):
                 if (t_current > time_var and t_current < time_var+period and t_previous > time_var and t_previous < time_var+period):
                    yep = 1
            t_previous = t_current;
        else:
            if (yep == 1 and go >= 2):
                random_switch = randint(0,len(user_interswitch)-1);
                output.write(str(user_interswitch[random_switch])+'\n')
            user_interswitch = []
            yep = 0
            go = 0
            u_end = t_previous;
            number_call = 1;
            switch_number = 0;
            call_in_switch_ave = 0;
            call_in_switch = 1;
            switch_previous = 0;
            t_previous = t_current;
            if (t_current > time_var and t_current < time_var+period):
                go = go+1
        bs_previous = bs_current;
        u_previous = u_current;

    if (yep == 1 and go >= 2):
        random_switch = randint(0,len(user_interswitch)-1);
        output.write(str(user_interswitch[random_switch])+'\n')

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
