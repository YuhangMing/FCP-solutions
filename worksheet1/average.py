#! /usr/bin/env python

#!/usr/bin/env python
#
# Filename      : averages.py
# Author        : Yuhang Ming
# Date          : Feb 2021
# Description   : Command line script to display averages of some numbers.

from averages import mode

import sys
import math
import argparse

def compute_mean(vals):
    sum = 0.
    num = len(vals)
    for v in vals:
        sum = sum + v
    avg_mean = sum / num
    print("Mean: ", avg_mean)

def compute_median(vals):
    num = len(vals)
    # Buble sorting
    for i in range(num-1):
        for j in range(num-i-1):
            if vals[j] > vals[j+1] : 
                vals[j], vals[j+1] = vals[j+1], vals[j]
    half = math.ceil(num/2.)
    print("Median: ", vals[half-1])

def compute_mod(vals):
    val_dict = {}
    for v in vals:
        if v in val_dict.keys():
            val_dict[v] = val_dict[v] + 1
        else:
            val_dict[v] = 1
    max_count = max(val_dict.values())
    print("Mod: ", end=' ')
    for val, count in val_dict.items():
        if count == max_count:
            print(val, ", ", end=' ')
    print("")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take averages of a set of integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='*',
                        help='integers to be averaged')
    parser.add_argument('--mean', dest='mean', action='store_true', default=False, 
                        help='take the mean')
    parser.add_argument('--mode', dest='mod', action='store_true', default=False, 
                        help='take the mode')
    parser.add_argument('--median', dest='median', action='store_true', default=False, 
                        help='find the median')
    parser.add_argument('--file', dest='file_name', default="", 
                        help='take the average from a file')
    args = parser.parse_args()

    if len(args.file_name) > 0 and len(args.integers) > 0:
        print("ERROR: expected one non-flag input when -file is specified")
        exit(1)

    elif len(args.file_name) > 0 and len(args.integers) == 0:
        print("Reading from ", args.file_name)
        with open(args.file_name) as f:
            array = []
            for line in f: # read rest of lines
                array.append([int(x) for x in line.split()])
        vals = [j for sub in array for j in sub]
        if len(vals) == 0:
            print("ERROR: no integers given.")
            exit(1)
    
    elif len(args.file_name) == 0 and len(args.integers) > 0:
        print("Reading from command line.")
        vals = args.integers
        if len(args.integers) > 8:
            print("ERROR: expected max 8 integer data points.")
            exit(1)
    
    else:
        print("ERROR: no file or integers given.")
        exit(1)

    if not args.mean and not args.mod and not args.median:
        compute_mean(vals)
        compute_median(vals)
        compute_mod(vals)

    if args.mean:
        compute_mean(vals)

    if args.median:
        compute_median(vals)

    if args.mod:
        compute_mod(vals)



    mode(vals)
