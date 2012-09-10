#!/usr/bin/python

import sys
import random
import string

lines = open(sys.argv[1]).readlines()
print lines

for line_no in xrange(len(lines)):
    if random.random() < len(lines)*.1:
        new_line = random.choice(string.lowercase)*10 + '\n'
        print 'changing line %s from %s to %s' % (line_no, lines[line_no], new_line)
        lines[line_no] = new_line

if not lines:
    new_line = random.choice(string.lowercase)*10 + '\n'
    print 'appending %s' % new_line
    lines.append(new_line)
else:
    new_line = random.choice(string.lowercase)*10 + '\n'
    place = random.randrange(0,len(lines))
    print 'inserting %s at line %s' % (new_line, place)
    lines.insert(place, new_line)

with open(sys.argv[1], 'wb') as out:
    out.writelines(lines)

print lines
