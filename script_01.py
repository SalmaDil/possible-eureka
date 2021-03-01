#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='An example python script, ready for extensions.')
parser.add_argument('--jens', action = 'store_true')
parser.add_argument('--hendrik', action = 'store_true')
parser.add_argument('--name')

args = parser.parse_args()

print("Hello, Loosolab!")


if(args.mario):
    print("Hello, Mario!")

if(args.jens):
    print("Hello, Jens!")
if(args.hendrik):
    print("Hello, Hendrik!")
if (args.name):
	print("Hello, {0}!".format(args.name))

