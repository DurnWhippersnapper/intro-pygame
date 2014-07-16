from levels import Level

from levels.level1.add import add_challenge
from levels.level1.mult import mult_challenge

challenges = [add_challenge, mult_challenge]

level1 = Level(XP=10,
               Story="This is level 1",
               Challenges = challenges)
