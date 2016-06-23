from __future__ import absolute_import
import sys
import argparse
import datetime
import time
import random

def check_phone_u_id (graph,antennas,output, output2):

    antenna = {}
    antenna_id = 1
    date = ''
    date_epoch = ''

    for line in antennas:
        item=line.replace('\n','').split('\t')
        antenna[(item[1], item[2])] = int(item[0])
        antenna_id = int(item[0])

    for line in graph:
        item=line.replace('\n','').split('\t')
        if (len(item) == 6):
            do_not_push=0
            try:
                date = item[3].replace(".", "")
            except:
                do_not_push=1

            test_date = date.split(' ')
            do_not_push=0
            if len(test_date)<2:
                do_not_push=1
            else:
                try:
                    date_epoch = datetime.datetime.strptime(date,"%d/%m/%Y %I:%M:%S %p").strftime('%s')
                except ValueError, v:
                    do_not_push=1

            if (do_not_push==0):
                if (item[1]=="" or int(float(item[1])) == 0):
                    output.write(date_epoch+'\t'+str(item[0])+'\t0\t'+str(item[4])+'\t'+str(item[5])+'\n')
                else:
                    if (not ((item[1], item[2]) in antenna)):
                        antenna[(item[1], item[2])] = antenna_id
                        output2.write(str(antenna_id)+'\t'+str(item[1])+'\t'+str(item[2])+'\n')
                        antenna_id = antenna_id+1
                    output.write(str(item[0])+'\t'+date_epoch+'\t'+str(antenna[(item[1], item[2])])+'\t'+str(item[4])+'\t'+str(item[5])+'\n')

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--graph",
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="input file name")
    parser.add_argument("-a", "--antenna",
                        type=argparse.FileType('r'),
                        help="input file name")
    parser.add_argument("-o", "--output",
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help="output")
    parser.add_argument("-o2", "--output2",
                        type=argparse.FileType('w'),
                        help="output")

       
    args = parser.parse_args()
    ids_dumped = check_phone_u_id(args.graph,args.antenna, args.output,args.output2)
    
    args.graph.close()
    args.output2.close()
    args.output.close()
    args.antenna.close()

if __name__ == "__main__":
    main()
