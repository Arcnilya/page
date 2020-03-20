#!/usr/bin/env python3
import sys

USAGE = "{} something something".format(sys.argv[0])

def dostuff(args):
	arg = ArgParser()
	arg.add()
	arg.add()
	opts = arg.parseargs()
	print("dostuff({})".format(args))

def dothings(args):
	print("dothings({})".format(args))

commands = {
	'dostuff': dostuff, 
	'dothings': dothings, 
}

if len(sys.argv) < 2:
	exit(USAGE)

if not sys.argv[1] in commands.keys():
	exit(USAGE)

commands[sys.argv[1]](sys.argv[2:])

