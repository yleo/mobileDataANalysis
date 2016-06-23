from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random
from random import randint

def check (input, output):
    by_slot_param1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    by_slot_param2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    by_slot_param3 = [0,0,0,0,0,0,0,0,0,0,0,0]
    by_slot_number1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    slot = 0
    duration = 0
    number_call = 0
    number_switch = 0
    ratio_switch = 0
    for line in input:
        item=line.replace('\n','').split('\t')
        if (len(item)==9):
            slot = int(item[1])
            duration = int(item[8])
            number_call = int(item[5])
            number_switch = int(item[7])
            ratio_switch = float(number_call)/float(number_switch)
            call_len = int(item[2])
            switch_len = int(item[6])
            if (ratio_switch>=5):
                by_slot_param1[slot] = by_slot_param1[slot]*float(by_slot_number1[slot])/(by_slot_number1[slot]+1) + float(call_len)/(by_slot_number1[slot]+1)
                by_slot_param2[slot] = by_slot_param2[slot]*float(by_slot_number1[slot])/(by_slot_number1[slot]+1) + float(switch_len)/(by_slot_number1[slot]+1)
                by_slot_param3[slot] = by_slot_param3[slot]*float(by_slot_number1[slot])/(by_slot_number1[slot]+1) + float(call_len*call_len)/(by_slot_number1[slot]+1)
                #by_slot_param1[slot] = by_slot_param1[slot]+number_call
                by_slot_number1[slot] = by_slot_number1[slot]+1
                

    for i in range(0,12):
        output.write(str(i)+"\t"+str(by_slot_param1[i])+"\t"+str(by_slot_param2[i])+"\t"+str(by_slot_param3[i]/by_slot_param1[i])+"\t"+str(by_slot_number1[i])+"\n")
    
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
    ids_dumped = check(args.input,args.output)
    
    args.input.close()
    args.output.close()

if __name__ == "__main__":
    main()
