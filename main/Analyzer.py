class Analysis:
    text = None
    keys_count = None

    def __init__(self, text, pop_objects=[], auto_count=True):
        self.text = text
        self.pop_objects = pop_objects
        if auto_count:
            self.CountKeys()
            self.SymmetricSlice()

    def CountKeys(self):

        keys = {}
        line_1_old = []

        for line in self.text:
            line_1 = line[1][1:-1].split(",")
            if(line_1_old != line_1):

                for old_key in line_1_old:
                    if old_key not in line_1:
                        self.AddKey(old_key, keys)
                line_1_old = line_1

        for key in line_1:
            self.AddKey(key, keys)

        out = self.PopObjects(keys)
        self.keys_count = out
        return(out)

    def PopObjects(self, keys):
        wrong_file_format_error = "Error: wrong file format"
        for pop_object in self.pop_objects:
            keys.pop(pop_object, wrong_file_format_error)
        return(keys)

    def SymmetricSlice(self, slice=1):
        out = {}
        for key in self.keys_count:
            out[key[slice:slice*-1]] = self.keys_count[key]
        self.keys_count = out
        return out

    def AddKey(self, key, keys):
        try:
            keys[key] += 1
        except:
            keys[key] = 1

    def GetKeysCount(self):
        return self.keys_count
