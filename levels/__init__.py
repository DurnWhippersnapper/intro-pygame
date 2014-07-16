from collections import namedtuple
Challenge = namedtuple('Challenge', ['Name',
                                     'Story',
                                     'Objective',
                                     'Level',
                                     'XP',
                                     'Verify'])

Level = namedtuple('Level', ['XP',
                             'Story',
                             'Challenges'])

from levels.level1 import level1
from levels.level2 import level2
levels = [level1, level2]
