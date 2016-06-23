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
    hour = int((timestamp-start_time-day*3600*24)/7200)
    return (day, hour)


def check_phone_u_id (input, output):

    bs = {}
    number_call = 0;
    duration_ave = 0;
    duration = 0;
    interarr_duration = 0;
    bs1 = 0;
    bs2 = 0;
    user_calls = {}
    user_calls_only = {}
    user_duration = {}
    user_bs = {}
    bs_current = 0;
    bs_previous = 0;
    t_current = 0;
    t_previous=0;
    u_current = 0;
    u_previous = 0;
    maxi = 0;
    random_call = 0;
    random_bs = 0;
    random_switch = 0;
    user_interswitch = [];
    go = 0;
    time_var = 1388530800;
    period = 7200
    day = 0
    hour = 0
    for line in input:
        item=line.replace('\n','').split('\t')
        t_current = int(item[1]);
        u_current = item[0];
        bs_current = int(item[2]);
        duration = int(item[4]);
        day, hour = get_date_hour(t_current)
        if (u_previous == u_current):
            number_call = number_call+1
            if ((day, hour) == get_date_hour(t_previous)):
                    if (not((day, hour) in user_calls)):
                        user_calls[(day, hour)] = []
                        user_duration[(day, hour)] = []
                        user_bs[(day, hour)] = []
                        user_calls_only[(day, hour)] = []
                    user_calls[(day, hour)].append(t_current-t_previous)
                    user_duration[(day, hour)].append(duration)
                    if (bs_current != bs_previous):
                        user_bs[(day, hour)].append(t_current-t_previous)
                    else:
                        user_calls_only[(day, hour)].append(t_current-t_previous)
        else:
            for day, hour in user_calls:
                if (len(user_calls[(day, hour)])>=2 and len(user_bs[(day, hour)])>=1 and len(user_calls_only[(day, hour)])>0):
                    random_switch = randint(0,len(user_bs[(day, hour)])-1);
                    random_call = randint(0,len(user_calls[(day, hour)])-1);
                    random_call_only = randint(0,len(user_calls_only[(day, hour)])-1);
                    #Day[0-364] / 2h-perriod [0-11] / Intervalle / Nombre Intervalles / Intervalle avec BS / Nombre Intervalle avec BS
                    output.write(str(day)+'\t'+str(hour)+'\t'+str(user_calls_only[(day, hour)][random_call])+'\t'+str(len(user_calls_only[(day, hour)]))+'\t'+str(user_calls[(day, hour)][random_call])+'\t'+str(len(user_calls[(day, hour)]))+'\t'+str(user_bs[(day, hour)][random_bs])+'\t'+str(len(user_bs[(day, hour)]))+'\t'+str(user_duration[(day, hour)][random_call])+'\n')
            user_calls = {}
            user_duration = {}
            user_bs = {}
        t_previous = t_current;
        bs_previous = bs_current;
        u_previous = u_current;
    
    for day, hour in user_calls:
        if (len(user_calls[(day, hour)])>=2 and len(user_bs[(day, hour)])>=1 and len(user_calls_only[(day, hour)])>0):
                    random_switch = randint(0,len(user_bs[(day, hour)])-1);
                    random_call = randint(0,len(user_calls[(day, hour)])-1);
                    random_call_only = randint(0,len(user_calls_only[(day, hour)])-1);
                    #Day[0-364] / 2h-perriod [0-11] / Intervalle / Nombre Intervalles / Intervalle avec BS / Nombre Intervalle avec BS
                    output.write(str(day)+'\t'+str(hour)+'\t'+str(user_calls_only[(day, hour)][random_call])+'\t'+str(len(user_calls_only[(day, hour)]))+'\t'+str(user_calls[(day, hour)][random_call])+'\t'+str(len(user_calls[(day, hour)]))+'\t'+str(user_bs[(day, hour)][random_bs])+'\t'+str(len(user_bs[(day, hour)]))+'\t'+str(user_duration[(day, hour)][random_call])+'\n')

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
