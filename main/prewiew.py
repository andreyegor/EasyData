import csv


class Analysis:
    text = None
    keys_count = None
    good_lines = None

    def __init__(self, text, pop_keys=[''], auto_count=True):
        """Сlass for get information from HeadCraken statistics

        Args:
            text (str): text from file
            pop_keys (list, optional): keys that are not a button. Defaults to [''].
            auto_count (bool, optional): Folse to manual work. Defaults to True.
        """

        self.text = text
        self.pop_keys = pop_keys
        self.GoodLines()
        if auto_count:
            self.CountKeys()
            self.keys_count = self.PopKeys(self.keys_count)
            self.keys_count = self.SymmetricSlice(self.keys_count)

    def CountKeys(self):
        """This function counts button presses using the self.good lines array,
            you can only use this function after self.GoodLines()
        """
        keys = {}
        old_line = []
        for line in self.good_lines:
            if(old_line != line):
                for old_key in old_line:
                    if old_key not in line:
                        self.AddKey(old_key, keys)
                old_line = line
        out = keys
        self.keys_count = out
        return(out)

    def GoodLines(self):
        """This function converts data of the format "{a, b, c}\n {a, b, c}"
            into a two-dimensional list [[a, b, c], [a, b, c]]

        Returns:
            list: two-dimensional list [[a, b, c], [a, b, c]]
        """
        out = []
        for line in self.text:
            line = line[1][1:-1].split(",")
            out.append(line)
        out[0] = []
        self.good_lines = out
        return out

    def PopKeys(self, in_dict):
        """Pop keys from pop.pop_keys

        Args:
            in_dict (dict): Your dictionary

        Returns:
            [type]: Dictionary without keys from self.pop_keys
        """
        out = in_dict
        wrong_file_format_error = "Error: wrong file format"
        for pop_object in self.pop_keys:
            out.pop(pop_object, wrong_file_format_error)
        return out

    def SymmetricSlice(self, in_dict, slice_length=1):
        """This function slise first and last parts of keys in dictionary by slice_length symbols.

        Args:
            in_dict (dict): Your dictionary
            slice_length (int, optional): Quantity symbols. Defaults to 1.

        Returns:
            dict: Dictionary without first and last symbols.
        """
        out = {}
        for key in in_dict:
            out[key[slice_length:slice_length*-1]] = in_dict[key]
        return out

    def AddKey(self, key, keys):
        """Create key in keys or increments the counter value of this key

        Args:
            key (str): Your key
            keys (dict): Your dictionary
        """
        try:
            keys[key] += 1
        except:
            keys[key] = 1

    def GetKeysCount(self):
        """Return self.keys_count"""
        return self.keys_count


# Constants
DEFAULT_LANG = 'RU'
LANG_RESOURSES = {
    'EN': {
        'Chainge language': "To change the language, enter EN, for English, RU for Russian",
        'Exit': "To exit the program enter EXIT",
        'Chainge language sucsess': "Language changed successfully",
        'Way to the file': "Please enter the way to the file",
        'File found': "File found",
        'File not found': "File not found",
        'Directory': "This is the way to the folder, not the file",
        'Please wait': "Please wait",
        'Pressing count': "Pressing count:",
        'File analyzed': "File analyzed",
        'Error': "Error"
    },

    'RU': {
        'Chainge language': "Для того, чтобы поменять язык, введите EN, для английского языка, RU для русского",
        'Exit': "Для того чтобы выйти из программы введите EXIT",
        'Chainge language sucsess': "Язык успешно изменен",
        'Way to the file': "Пожалуйста введите путь к файлу",
        'File found': "Файл найден",
        'File not found': "Файл не найден",
        'Directory': "Это путь к папке, а не к файлу",
        'Please wait': "Пожалуйста подождите",
        'Pressing count': "Количество нажатий:",
        'File analysed': "Файл проанализирован",
        'Error': "Ошибка"
    }
}
DEFAULT_KEYBOARD_WAY = r"test_files\key_example.csv"
DEFAULT_MOUSE_WAY = r"test_files\mkey_example.csv"

# Get language
try:
    res = open('res', 'r')
    read = res.read()
    res.close()
    if read in LANG_RESOURSES.keys():
        LANG = read
except:
    LANG = DEFAULT_LANG

# Input logic
print(LANG_RESOURSES[LANG]['Chainge language'])
print(LANG_RESOURSES[LANG]['Exit'])
while True:
    print(LANG_RESOURSES[LANG]['Way to the file'])
    line = input()
    if line in LANG_RESOURSES.keys():
        LANG = line
        print(LANG_RESOURSES[LANG]['Chainge language sucsess'])
    elif line == 'EXIT':
        break
    else:
        try:
            tfile = open(line, newline='')
            analysed = Analysis(
                csv.reader(tfile))
            tfile.close()
            print(LANG_RESOURSES[LANG]['Pressing count'])
            print(analysed.GetKeysCount())
        except FileNotFoundError:
            print(LANG_RESOURSES[LANG]['File not found'])
        except IsADirectoryError:
            print(LANG_RESOURSES[LANG]['Directory'])
        except:
            print(LANG_RESOURSES[LANG]['Error'])
    print(LANG_RESOURSES[LANG]['Exit'])
res = open('res', 'w')
res.write(LANG)
res.close()
