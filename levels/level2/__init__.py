from levels import Level

from levels.level2.mult import mult_challenge

challenges = [mult_challenge]

level2 = Level(Name='Level 2',
               neededXP=15,
               Story="This is level 2",
               Challenges = challenges)
