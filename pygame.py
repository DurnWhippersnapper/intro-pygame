#! /usr/bin/python3

import sys
import argparse
import colorama
from player import Player
from levels import levels

def createParser():
    parser = argparse.ArgumentParser(description='Learn Programming by climbing the corporate ladder')
    subcommands = parser.add_subparsers(title="Commands",
                                        description="Use these commands to interact with the game",
                                        metavar="<command>")

    s = subcommands.add_parser("list-challenges", aliases=['l'], help='List the challenges at the current level')
    s.set_defaults(func=Player.list_challenges)

    s = subcommands.add_parser("challenge-info", aliases=['i', 'info'], help='Get info about the specified challenge')
    s.add_argument('challenge_name', help="The title of the challenge")
    s.set_defaults(func=Player.challenge_info)

    s = subcommands.add_parser("solve-challenge", aliases=['solve'], help='Solve a challenge')
    s.add_argument('challenge_number', help="Challenge Number", type=int)
    s.add_argument('solution', help="Puzzle solution script", type=open)
    s.set_defaults(func=Player.solve_challenge)

    return parser

if __name__ == "__main__":
    colorama.init(autoreset=True)

    parser = createParser()

    #TODO read in from config file
    dummy_player = Player()

    args = parser.parse_args()
    if len(sys.argv) == 1:
        #TODO better default help function for beginners
        parser.print_help()
    else:
        args.func(dummy_player, args)
