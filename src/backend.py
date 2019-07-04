#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6.4

import classes
import os
import config


def load_words():

    import pickle

    with open('src/words.pckl', 'rb') as f:
        all_words = pickle.load(f)

    return all_words


def load_player():
    import pickle

    # name = input('what's your name?\n')
    name = 'Sid'
    if os.path.exists('src/players/{}.sav'.format(name)):
        with open('src/players/{}.sav'.format(name), 'rb') as f:
            player = pickle.load(f)
    else:
        print("player doesn't exist")
        player_class = input("what's your class?\n")
        player = classes.PlayerCharacter(player_name=name,
                                         player_class=player_class)
    config.player = player
    return


def save_player():
    import pickle

    player = config.player

    if not os.path.exists('src/players/'):
        os.mkdir('src/players')
    with open('src/players/{}.sav'.format(player.name), 'wb') as f:
        pickle.dump(player, f, protocol=-1)

    return