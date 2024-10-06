from collections import defaultdict
from typing import Dict


MISSION_DICE_DIST = {
    0.0: 1/3,
    1.0: 1/2,
    2.0: 1/6,
}


def one_side_distribution(n_dice: int, advantage: int = 0) -> Dict[float, float]:
    dist = {0.0: 1.0}
    for _ in range(n_dice):
        next_dist = defaultdict(lambda: 0.0)
        for prev_v, prev_p in dist.items():
            for dice_v, dice_p in MISSION_DICE_DIST.items():
                v = prev_v + dice_v
                p = prev_p * dice_p
                next_dist[v] += p
        dist = next_dist

    return {
        k + advantage: v for k, v in dist.items()
    }
                


def leader_victory_prob(n_leader_dice: int, n_opposer_dice: int, leader_advantage: int = 0) -> float:
    leader_distribution = one_side_distribution(n_leader_dice, leader_advantage)
    opposer_distribution = one_side_distribution(n_opposer_dice)

    prob = 0

    for l_v, l_p in leader_distribution.items():
        for o_v, o_p in opposer_distribution.items():
            if l_v > o_v:
                prob += l_p * o_p
    return prob
