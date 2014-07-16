from levels import Challenge

def mult_verify(f):
    execfile(f)
    return mult(2,3) == 6
mult_challenge = Challenge(Name="Multiply",
                           Story="This is your boss. Multiply!",
                           Objective="Write a function named ``mult\" of two arguments",
                           Level=1,
                           XP = 5,
                           Verify = mult_verify)
