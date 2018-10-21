from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    total, i = 0, 0
    while i < num_rolls:
        roll = dice()
        if roll == 1 or total == 1:
            total = 1
            i += 1
        else:
            total += roll
            i += 1
    return total
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    tens, ones = score // 10, score % 10
    return max(2 * tens - ones, 1)
    # END PROBLEM 2

def time_trot():
    def g(rolls, turn):
        if turn % 5 == rolls:
            return True
        return False
    return g

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def is_swap(player_score, opponent_score):
    """
    Return whether the current player's score has the same absolute
    difference between its last two digits as the opponent's score.
    """
    # BEGIN PROBLEM 4
    player_score_adj, opponent_score_adj = player_score % 100, opponent_score % 100
    player_diff = abs((player_score_adj // 10) - (player_score_adj % 10))
    opponent_diff = abs((opponent_score_adj // 10) - (opponent_score_adj % 10))

    if player_diff == opponent_diff:
        return True
    else:
        return False
    # END PROBLEM 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    player = 1  # Which player is about to take a turn, 0 (first) or 1 (second)
    time_trot, turn = time_trot(), 0
    # BEGIN PROBLEM 5
    def turn(strategy, score, opponent_score):
        rolls = strategy(score, opponent_score)
        score = take_turn(rolls, opponent_score, dice)
        if is_swap(score, opponent_score):
            score, opponent_score = opponent_score, score
        return score, opponent_score, rolls
    
    while score0 < goal and score1 < goal:
        player = other(player)
        
        if player == 0:
            score0, score1, rolls = turn(strategy0, score0, score1)
            if time_trot(rolls, turn):
                score0, score1, rolls = turn(strategy0, score0, score1)
                turn += 2
                continue
        
        else:
            score1, score0, rolls = turn(strategy1, score1, score0)
            if time_trot(rolls, turn):
                score1, score0, rolls = turn(strategy1, score1, score0)
                turn += 2
                continue
        
        turn += 1
    # END PROBLEM 5
    return score0, score1

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy    

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    def averaged(*args):
        i, total = 0, 0
        while i < num_samples:
            total += fn(*args)
            i += 1
        return total / num_samples
    return averaged

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    averaged_roll = make_averaged(roll_dice)
    top_score, top_rolls = 0, 0
    for i in range(1, 11):
        result = averaged_roll(i, dice)
        if result > top_score:
            top_score, top_rolls = result, i
        elif result == top_score:
            top_rolls = min(top_rolls, i)
    return top_rolls

    # END PROBLEM 9

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2