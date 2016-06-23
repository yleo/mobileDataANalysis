from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random

def check_phone_u_id (input, output):

    bs = {}
    number_call = 0;
    duration_ave = 0;
    duration = 0;
    interarr_duration = 0;
    bs1 = 0;
    bs2 = 0;
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
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[0]);
        u_current = item[1];
        bs_current = int(item[2]);
        duration = int(item[4]);
            
        if (u_previous == u_current):
            duration_ave = duration_ave*(float(number_call)/(number_call+1))+float(duration)/(number_call+1);
            #interarr_duration
            interarr_duration = interarr_duration*(float(number_call-1)/(number_call))+float(t_current-t_previous)/(number_call)
            #number of call
            number_call = number_call+1
            #switch number et duration
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
            if (not(bs_current in bs)):
                bs[bs_current] = 0
            bs[bs_current] = bs[bs_current] + 1
            t_previous = t_current;
        else:
            u_end = t_previous;
            for i in bs:
                if (i!=0):
                    if (bs[i]>maxi):
                        maxi = bs[i];
                        bs1 = i;
            if (u_previous != 0):
                output.write(str(u_previous)+"\t"+str(number_call)+"\t"+str(duration_ave)+"\t"+str(interarr_duration)+"\t"+str(switch_number)+"\t"+str(switch_duration)+"\t"+str(interswitch_duration)+"\t"+str(call_in_switch_ave)+"\t"+str(u_begin)+"\t"+str(u_end)+"\t"+str(bs1)+"\n");
            maxi = 0;
            bs1 = 0;
            number_call = 1;
            u_begin = t_current;
            duration_ave = duration;
            interarr_duration = 0;
            switch_number = 0;
            switch_duration = 0;
            interswitch_duration = 0;
            call_in_switch_ave = 0;
            call_in_switch = 1;
            u_end = 0;
            switch_previous = 0;
            t_previous = t_current;
            bs = {}
            bs[bs_current] = 1
        bs_previous = bs_current;
        u_previous = u_current;

    for i in bs:
        if (i!=0):
            if (bs[i]>maxi):
                maxi = bs[i];
                bs1 = i;

    output.write(str(u_current)+"\t"+str(number_call)+"\t"+str(duration_ave)+"\t"+str(interarr_duration)+"\t"+str(switch_number)+"\t"+str(switch_duration)+"\t"+str(interswitch_duration)+"\t"+str(call_in_switch_ave)+"\t"+str(u_begin)+"\t"+str(t_current)+"\t"+str(bs1)+"\n");

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
