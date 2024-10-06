# Star Wars Lucker
Star Wars Rebellion - an epic 2-player board game where Galatic Imperium clashes with Rebel Alliance to gain control over the galaxy.

Winning battles is not the only means to victory.
Individual leaders undertake missions to gain the support of star systems, sabotage enemy units and more. The missions might be opposed by enemy leaders. In such a scenario success is determined by dice roll. 

This petty project aims to calculate probability of mission success so the players can freely accuse their opponents of winning the game by sheer luck with statistical evidence.

## About missions
Each mission is attempted in one of systems. In such case opponent may add one of his free leaders to the system. If there are any opponent's leaders in the system the mission is opposed.

Each mission has a determining skill (3 distinct skills in the game) and each leader has 0-3 points for a given skill. Each player then rolls the dice. Number of dice player throws is equal to the sum of all skills of all player's leader present in the system. Dice throw reveals a number of successes player achieved. If mission attempting player rolls more successes than opposing player the mission is successful.

Dice are not a usual playing dice. Although they are 6-sided dice the values (number of success) are uncommon.
Following table shows probabilty distribution:

| Probability | Number of successes |
|-------------|---------------------|
| 1/3         | 0                   |
| 1/2         | 1                   |
| 1/6         | 2                   |

Additionally some leaders have advantage on specific missions which gives them extra 2 successes.

## So how lucky was the opponent to actually convert Chewbacca to the dark side?
To calculate the probabilty run `lucky.py` script.

Example call of 1 dice for atemptee with advantage against 2 dice of opposing player:
```
./star_wars_lucker/lucky.py 1 2 -a
```
Output: Missions success probability: 0.712962962962963

For detailed info about calculation see:
```
./star_wars_lucker/lucky.py --help
```

### Precalculated tables
Alternatively you can look into the precalculated tables `out.csv` and `out_advantage.csv`.
These contain probabilities of success for each combination of 0 to 10 dice thrown.
