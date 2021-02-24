class Analysis:
    text = None
    keys_count = None
    good_lines = None

    def __init__(self, text, pop_objects=[], auto_count=True):
        self.text = text
        self.pop_objects = pop_objects
        self.GoodLines()
        if auto_count:
            self.CountKeys()
            self.SymmetricSlice(self.keys_count)
            self.PopObjects()

    def CountKeys(self):
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
        out = []
        for line in self.text:
            line = line[1][1:-1].split(",")
            out.append(line)
        self.good_lines = out
        return out

    def PopObjects(self):
        wrong_file_format_error = "Error: wrong file format"
        out = self.keys_count
        for pop_object in self.pop_objects:
            out.pop(pop_object, wrong_file_format_error)
        self.keys_count = out
        return out

    def SymmetricSlice(self, in_dict, slice=1):
        out = {}
        for key in in_dict:
            out[key[slice:slice*-1]] = in_dict[key]
        in_dict = out
        return out

    def AddKey(self, key, keys):
        try:
            keys[key] += 1
        except:
            keys[key] = 1

    def GetKeysCount(self):
        return self.keys_count
