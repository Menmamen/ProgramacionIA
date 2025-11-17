# Python exercises for AI Programming Course: Piedra Papel Tijera Lagarto Spock
# Exercises solved by Carmen Montalvo Luque, 11/2025

# =====================================================
# Ejercicio Lagarto–Spock
#
# Partiendo del código disponible en fichero adjunto añade la funcionalidad
# necesaria para ofrecer la variante lagarto, Spock del juego piedra, papel o tijeras.
#
# Usa las diferentes situaciones de juego, junto con su resultado, del archivo
# victories.xml que se adjunta.
#
# Sustituye el diccionario Victories por alguna referencia que permita acceder
# al contenido de victories.xml.
#
# Recomiendo usar el módulo xml.etree.ElementTree para procesar el archivo victories.xml.
# =====================================================

import random
import xml.etree.ElementTree as ET
from enum import IntEnum
from statistics import mode
import os


# -----------------------------------------------------
# Load XML victory rules
# -----------------------------------------------------
# This function loads the XML file and returns a dictionary:
# { "Rock": { "Scissors": "Rock smashes Scissors", ... } }
# It also keeps a reverse structure for lookup by GameAction enum.

def load_victories(path):
    tree = ET.parse(path)
    root = tree.getroot()

    victories = {}     # string → string → text
    for v in root.findall("victory"):
        choice = v.attrib["choice"]
        against = v.attrib["against"]
        text = v.text.strip()

        if choice not in victories:
            victories[choice] = {}
        victories[choice][against] = text

    return victories


# -----------------------------------------------------
# GameAction extended with Lizard and Spock
# The enum order corresponds to menu options
# -----------------------------------------------------
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


NUMBER_RECENT_ACTIONS = 5


# -----------------------------------------------------
# assess_game: determines game result from XML
# -----------------------------------------------------
# Logic:
#   - If same choice → tie
#   - If user_action beats computer_action according to XML → victory
#   - If computer beats user → defeat

def assess_game(user_action, computer_action):
    user_name = user_action.name
    comp_name = computer_action.name

    # Tie
    if user_action == computer_action:
        print(f"User and computer picked {user_name}. Draw game!")
        return GameResult.Tie

    # User wins?
    if comp_name in VICTORY_RULES[user_name]:
        print(f"{VICTORY_RULES[user_name][comp_name]}. You won!")
        return GameResult.Victory

    # Else user loses
    print(f"{VICTORY_RULES[comp_name][user_name]}. You lost!")
    return GameResult.Defeat


# -----------------------------------------------------
# get_computer_action:
# AI picks a winning move based on user's recent history
# -----------------------------------------------------

def get_computer_action(user_actions_history, game_history):
    # no history → random choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()

    else:
        # AI counters the user's most frequent recent move
        most_frequent_user_choice = mode(user_actions_history[-NUMBER_RECENT_ACTIONS:])
        computer_action = get_winner_action(most_frequent_user_choice)

    print(f"Computer picked {computer_action.name}.")
    return computer_action


# -----------------------------------------------------
# User input
# -----------------------------------------------------

def get_user_action():
    choices = [f"{action.name}[{action.value}]" for action in GameAction]
    user_selection = int(input(f"\nPick a choice ({', '.join(choices)}): "))
    return GameAction(user_selection)


# -----------------------------------------------------
# Random AI
# -----------------------------------------------------
def get_random_computer_action():
    return GameAction(random.randint(0, len(GameAction) - 1))


# -----------------------------------------------------
# get_winner_action:
# finds an action that beats the given action
# using the XML victory rules
# -----------------------------------------------------
# Example:
#   user picks Rock → computer picks something that defeats Rock
#   Those entries are found in VICTORY_RULES such that:
#       VICTORY_RULES[x]["Rock"] exists

def get_winner_action(game_action):
    target = game_action.name

    # Find an action that beats “target”
    for winner, defeats in VICTORY_RULES.items():
        if target in defeats:     # e.g., VICTORY_RULES["Paper"]["Rock"]
            return GameAction[winner]

    # Should not happen with correct XML
    return get_random_computer_action()


def play_another_round():
    return input("\nAnother round? (y/n): ").lower() == 'y'


# -----------------------------------------------------
# MAIN
# -----------------------------------------------------

def main():
    game_history = []
    user_actions_history = []

    while True:
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError:
            print(f"Invalid selection. Pick a choice in range [0, {len(GameAction)-1}]!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history)
        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)

        if not play_another_round():
            break


# -----------------------------------------------------
# Load XML once when file is executed
# -----------------------------------------------------

# “lagartoSpock” folder (user provided)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
XML_PATH = os.path.join(SCRIPT_DIR, "victories.xml")

# Load all victory rules from XML
VICTORY_RULES = load_victories(XML_PATH)


if __name__ == "__main__":
    main()
