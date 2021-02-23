import csv

import Analyzer
way_to_keyboard_key_file = r"test_files\key_example.csv"
way_to_mouse_key_file = r"test_files\mkey_example.csv"
keyboard_keys_pop = ('e', '')
mouse_keys_pop = ('ouse_ke', '')

keyboard_key_file = open(way_to_keyboard_key_file, newline='')
mouse_key_file = open(way_to_mouse_key_file, newline='')
analysed_keyboard = Analyzer.Analysis(
    csv.reader(keyboard_key_file), keyboard_keys_pop)
analysed_mouse = Analyzer.Analysis(csv.reader(mouse_key_file), mouse_keys_pop)
keyboard_key_file.close()
mouse_key_file.close()
print("Keyboard\n"+"-"*8)
print(analysed_keyboard.GetKeysCount())
print("Mouse\n"''+"-"*5)
print(analysed_mouse.GetKeysCount())
