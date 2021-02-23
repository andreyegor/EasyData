import csv
way_to_keyboard_key_file = r"test_files\key_example.csv"
way_to_mouse_key_file = r"test_files\mkey_example.csv"
keyboard_keys_pop = ('e', '')
mouse_keys_pop = ('ouse_ke', '')


def AddKey(key, keys):
    try:
        keys[key] += 1
    except:
        keys[key] = 1


def SymmetricSlice(dict, slice=1):
    out_dict = {}
    for dict_key in dict:
        out_dict[dict_key[slice:slice*-1]] = dict[dict_key]
    return out_dict


def Out(dict):
    for dict_key in dict:
        print(str(dict_key)+': ' + str(dict[dict_key]))


def CountKeys(this_file, pop_objects):
    keys = {}
    line_1_old = []
    wrong_file_format_error = "Error: wrong file format"
    for line in this_file:
        line_1 = line[1][1:-1].split(",")
        if(line_1_old != line_1):

            for old_key in line_1_old:
                if old_key not in line_1:
                    AddKey(old_key, keys)
            line_1_old = line_1

    for key in line_1:
        AddKey(key, keys)

    for pop_object in pop_objects:
        if keys.pop(pop_object, wrong_file_format_error) == wrong_file_format_error:
            print(pop_object)
            print(wrong_file_format_error)
    return(keys)


keyboard_key_file = open(way_to_keyboard_key_file, newline='')
mouse_key_file = open(way_to_mouse_key_file, newline='')
csv_keyboard_key_file = csv.reader(keyboard_key_file)
csv_mouse_key_file = csv.reader(mouse_key_file)
keyboard_keys = SymmetricSlice(
    CountKeys(csv_keyboard_key_file, keyboard_keys_pop))
mouse_keys = SymmetricSlice(CountKeys(csv_mouse_key_file, mouse_keys_pop))
mouse_key_file.close()
keyboard_key_file.close()
print("Keyboard\n"+"-"*8)
print(keyboard_keys)
print("Mouse\n"''+"-"*5)
mouse_keys
