from levels import Challenge

def add_verify(f):
    execfile(f)
    return add(2,3) == 5
add_challenge = Challenge(Name="Add",
                          Story="This is your boss. Add!",
                          Objective="Write a function named ``add\" of two arguments",
                          Level=1,
                          XP = 5,
                          Verify = add_verify)
