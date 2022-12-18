#!/usr/bin/python3
import argparse
import subprocess
import sys
#  import os

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5fc953305eacb0eaf79e16df8198096b7e06f4f45b7103e0160c7606cfe467b8fa983dddbdb4bfeb26498acf450792305d1dd1dcea2373a784'

useragent = "https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py"
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A {useragent}'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')


f = open("input.txt", 'w')
f.write(output)

print(output)
print(output, end='')
# print('\n'.join(output.split('\n')[:10]), file=sys.stderr)

# this script works to create a new file called input.txt in the current directory
# still need to figure out:
#   1. How to get input for different days in adventofCode
#   2. get ./get_input script to work from different directory?
#       - watch jonathanpaulson use it in one of his videos
