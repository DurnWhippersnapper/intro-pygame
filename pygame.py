import sys
import argparse
import colorama
from challenges import challenges

def list_challenges(args):
    level_challenges = [c for c in challenges if c.Level == dummy_player.current_level]
    column_width = max(len(c.Name) for c in level_challenges)
    for challenge in level_challenges:
        if challenge in dummy_player.completed:
            color = colorama.Fore.GREEN
        else:
            color = colorama.Fore.RED
        print(color + "%s\t%dXP" % (challenge.Name.ljust(column_width), challenge.XP))

def challenge_info(args):
    for challenge in challenges:
        if challenge.Level == dummy_player.current_level and challenge.Name == args.challenge_name:
            #TODO prettier printing
            print(challenge.Story)
            break
    else:
        print("No challenge named ``%s'' on level %d" % (args.challenge_name, dummy_player.current_level))

def solve_challenge(args):
    print("Hey")

class Player:
    def __init__(self):
        self.completed = []
        self.current_level = 1

if __name__ == "__main__":
    colorama.init(autoreset=True)

    dummy_player = Player()
    dummy_player.completed.append(challenges[0])

    parser = argparse.ArgumentParser(description='Learn Programming by climbing the corporate ladder')
    subcommands = parser.add_subparsers(title="Commands",
                                        description="Use these commands to interact with the game",
                                        metavar="<command>")

    s = subcommands.add_parser("list-challenges", aliases=['l'], help='List the challenges at the current level')
    s.set_defaults(func=list_challenges)

    s = subcommands.add_parser("challenge-info", aliases=['i', 'info'], help='Get info about the specified challenge')
    s.add_argument('challenge_name', help="The title of the challenge")
    s.set_defaults(func=challenge_info)

    s = subcommands.add_parser("solve-challenge", aliases=['s'], help='Solve a challenge')
    s.add_argument('challenge_number', help="Challenge Number", type=int)
    s.add_argument('solution', help="Puzzle solution script", type=open)
    s.set_defaults(func=solve_challenge)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        #TODO better default help function for beginners
        parser.print_help()
    else:
        args.func(args)
