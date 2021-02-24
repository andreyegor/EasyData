import csv
import Analyzer
way_to_keyboard_key_file = r"main\test_files\key_example.csv"
way_to_mouse_key_file = r"main\test_files\mkey_example.csv"

keyboard_key_file = open(way_to_keyboard_key_file, newline='')
mouse_key_file = open(way_to_mouse_key_file, newline='')

analysed_keyboard = Analyzer.Analysis(
    csv.reader(keyboard_key_file))
analysed_mouse = Analyzer.Analysis(csv.reader(mouse_key_file))
keyboard_key_file.close()
mouse_key_file.close()
print("Keyboard\n"+"-"*8)
print(analysed_keyboard.GetKeysCount())
print("Mouse\n"''+"-"*5)
print(analysed_mouse.GetKeysCount())
