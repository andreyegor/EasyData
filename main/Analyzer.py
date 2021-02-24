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
