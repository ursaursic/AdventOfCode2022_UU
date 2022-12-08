"""
This is main. Tons of fun! Thanks to Levi for inspiring comments and suggestions. :D
"""

import sys
from day1 import main as day_1
from day2 import main as day_2
from day3 import main as day_3
from day4 import main as day_4
from day5 import main as day_5
from day6 import main as day_6
from day7 import main as day_7
from day8 import main as day_8

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print('Yaou cunt, just one please!')
        sys.exit(-1)

    mains = [day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8]
    day_denumerator = int(sys.argv[1])-1

    if day_denumerator > len(mains) or day_denumerator < 0:
        print('Ya cunt, cannot even count! Stupiiid.....')
        print('You need to chooooooose, from 1 tooooooo')
        print(len(mains))
        print('yeah.....')
        sys.exit(-2)

    mains[day_denumerator]()