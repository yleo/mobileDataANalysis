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
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[0]);
        u_current = item[1];
        bs_current = int(item[2]);
        duration = int(item[4]);
        if (u_previous == u_current):
            number_call = number_call+1
            #switch number et duration
            user_call_in_switch.append(t_current-t_previous);
            if (bs_current != bs_previous):
                switch_duration = switch_duration*(float(switch_number)/(switch_number+1))+float(t_current-t_previous)/(switch_number+1);
                if (switch_previous!=0):
                    interswitch_duration = interswitch_duration*(float(switch_number)/(switch_number+1))+float(t_current-switch_previous)/(switch_number+1);
                switch_previous = t_current;
                call_in_switch_ave = call_in_switch_ave*(float(switch_number)/(switch_number+1))+float(call_in_switch)/(switch_number+1);
                call_in_switch = 1
                switch_number = switch_number + 1;
            else:
                call_in_switch = call_in_switch + 1;
            t_previous = t_current;
        else:
            if (len(user_call_in_switch)>0):
                random_switch = randint(0,len(user_call_in_switch)-1);
                output.write(str(user_call_in_switch[random_switch])+'\n')
            user_call_in_switch = []
            u_end = t_previous;
            number_call = 1;
            switch_number = 0;
            call_in_switch_ave = 0;
            call_in_switch = 1;
            switch_previous = 0;
            t_previous = t_current;
        bs_previous = bs_current;
        u_previous = u_current;

    if (len(user_call_in_switch)>0):
        random_switch = randint(0,len(user_call_in_switch)-1);
        output.write(str(user_call_in_switch[random_switch])+'\n')

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
