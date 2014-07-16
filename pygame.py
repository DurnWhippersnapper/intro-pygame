#! /usr/bin/python3

import sys
import argparse
import colorama
from player import Player
from levels import levels

def createParser():
    parser = argparse.ArgumentParser(description='Learn Programming by climbing the corporate ladder')
    subcommands = parser.add_subparsers(title='Commands',
                                        description='Use these commands to interact with the game',
                                        metavar='<command>')

    s = subcommands.add_parser('list-challenges', aliases=['l'], help='List the challenges at the current level')
    s.set_defaults(func=Player.printCurrentChallenges)

    s = subcommands.add_parser('challenge-info', aliases=['i', 'info'], help='Get info about the specified challenge')
    s.add_argument('challenge_name', help='The title of the challenge')
    s.set_defaults(func=Player.printChallengeInfo)

    s = subcommands.add_parser('solve-challenge', aliases=['solve'], help='Solve a challenge')
    s.add_argument('challenge_name', help='Challenge Name')
    s.add_argument('solution', help='Puzzle solution script', type=open)
    s.set_defaults(func=Player.solveChallenge)

    s = subcommands.add_parser('status', help = 'Print your current status')
    s.set_defaults(func=Player.printStatus)

    return parser

def printNewUserIntro():
    intromessage = """
        Hello, and welcome to PyGame. This is a command-line driven game, 
        so all of your interactions will be in the terminal (which is what 
        you're using now). To view the current challenges, you can type
            ./pygame.py list-challenges
        To solve a challenge, create a script file with your solution in it,
        then call
            ./pygame.py solve-challenge <challenge name> <solution script file>
        
        You can also try
            ./pygame.py status
        to see your status at any time. Feel free to use
            ./pygame.py --help
        to see all of the other actions.

        You can go ahead and use the list-challenges option to see your current
        challenges
    """
    print(intromessage)

if __name__ == '__main__':
    colorama.init(autoreset=True)

    parser = createParser()

    player = Player()

    if player.newuser:
        printNewUserIntro()
    else:
        args = parser.parse_args()
        if len(sys.argv) == 1:
            #TODO better default help function for beginners
            parser.print_help()
        else:
            args.func(player, args)

    player.saveToSaveFile()
