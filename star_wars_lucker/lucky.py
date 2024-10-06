#!/usr/bin/env python3

from argparse import ArgumentParser
from star_wars_lucker.calc import leader_victory_prob


def main():
    parser = ArgumentParser(description='Calculate the probability of mission success.')
    
    # Adding arguments
    parser.add_argument('n_leader_dice', type=int, help='Number of dice the leader has')
    parser.add_argument('n_opposer_dice', type=int, help='Number of dice the opposer has')
    parser.add_argument('-a', '--leader_advantage', action='store_true', help='Additional advantage for the leader')
    
    # Parse arguments
    args = parser.parse_args()
    
    leader_advantage = 2 if args.leader_advantage else 0

    # Call the function with the parsed arguments
    result = leader_victory_prob(args.n_leader_dice, args.n_opposer_dice, leader_advantage)
    
    # Print the result
    print(f'Missions success probability: {result}')


if __name__ == '__main__':
    main()
