from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random
from random import randint

def check (input, output):
    by_slot_param1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    by_slot_number1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    slot = 0
    for line in input:
        item=line.replace('\n','').split('\t')
        slot = int(item[1])
        duration = int(item[6])
        by_slot_param1[slot] = by_slot_param1[slot]*float(by_slot_number1[slot])/(by_slot_number1[slot]+1) + float(duration)/(by_slot_number1[slot]+1)
        by_slot_number1[slot] = by_slot_number1[slot]+1

    for i in range(0,12):
        output.write(str(i)+"\t"+str(by_slot_param1[slot])+"\t"+str(by_slot_number1[slot])+"\n")
    
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
