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
    hour = int(timestamp-day*3600*24-start_time)/7200
    second = int(timestamp-day*3600*24-hour*7200-start_time)
    return (day, hour, second)

def check_phone_u_id (input, output):

    user_status = 0
    user_times = 0
    user_times_min = 0
    user_times_max = 0
    number_call = 0;
    number_switch = 0
    bs_current = 0;
    bs_previous = 0;
    t_current = 0;
    t_previous=0;
    u_current = 0;
    u_previous = 0;
    random_number = 0;
    dayp = 0
    hourp = 0
    secondp = 0
    origin = 1800
    for line in input:
        item=line.replace('\n','').split('\t')
        if (len(item[1])==10):
            t_current = int(item[1]);
            u_current = item[0];
            bs_current = int(item[2]);
            duration = int(item[4]);
            day, hour, second = get_date_hour(t_current);
            dayp, hourp, secondp = get_date_hour(t_previous);
            if (u_previous == u_current and (day, hour) == (dayp, hourp)):
                number_call = number_call + 1
                if (bs_current != bs_previous):
                    number_switch = number_switch+1
                if (user_status == 5 and second < origin):
                    user_status = 0
                elif (user_status == 0 and second > origin):
                    if (bs_current == bs_previous):
                        user_status = 1
                    else:
                        random_number = randint(secondp,second);
                        if (secondp>=origin):
                            user_status = 2
                            user_times = random_number;
                            user_times_min = secondp;
                            user_times_max = second;
                        else:
                            user_status = 3
                elif (user_status == 1):
                    if (bs_current != bs_previous):
                        user_status = 2;
                        user_times = randint(secondp,second);
                        user_times_min = secondp;
                        user_times_max = second;
                elif (user_status == 3):
                    if (bs_current != bs_previous):
                        user_status = 4;
                        user_times = randint(secondp,second);  
                        user_times_min = secondp;
                        user_times_max = second;
            else:
                if u_previous != 0:
                    if (number_call>=2 and number_switch>=1):
                        output.write(str(dayp)+"\t"+str(hourp)+"\t"+str(user_status)+"\t"+str(user_times)+"\t"+str(user_times_min)+"\t"+str(user_times_max)+"\t"+str(number_call)+"\t"+str(number_switch)+"\n")
                user_status=5
                user_times=-1
                user_times_max=-1
                user_times_min=-1
                if (user_status == 5 and second < origin):
                    user_status = 0
                    number_call = 1
                    number_switch = 0
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
