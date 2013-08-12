#!/usr/bin/python
import sys

nums = [int(x) for x in sys.stdin.readline().split(' ')]
print 2 * nums[0] + 2 * nums[1] + 2 * nums[2] + nums[3] * (3 / 2.) + nums[4]
