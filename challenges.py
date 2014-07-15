from collections import namedtuple
Puzzle = namedtuple('Puzzle', ['Name',
                               'Story',
                               'Objective',
                               'Level',
                               'XP',
                               'Verify'])
challenges = []


def add_verify(f):
    execfile(f)
    return add(2,3) == 5
add_challenge = Puzzle(Name="Add",
                       Story="This is your boss. Add!",
                       Objective="Write a function named ``add"" of two arguments",
                       Level=1,
                       XP = 5,
                       Verify = add_verify)
challenges.append(add_challenge)


def mult_verify(f):
    execfile(f)
    return mult(2,3) == 6
mult_challenge = Puzzle(Name="Multiply",
                        Story="This is your boss. Multiply!",
                        Objective="Write a function named ``mult"" of two arguments",
                        Level=1,
                        XP = 5,
                        Verify = mult_verify)
challenges.append(mult_challenge)
