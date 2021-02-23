class Analysis:
    text = None
    pop_objects = None
    keys_count = None

    def __init__(self, text, pop_objects=[]):
        self.text = text
        self.pop_objects = pop_objects
        self.keys_count = self.CountKeys()

    def CountKeys(self):

        keys = {}
        line_1_old = []
        wrong_file_format_error = "Error: wrong file format"
        for line in self.text:
            line_1 = line[1][1:-1].split(",")
            if(line_1_old != line_1):

                for old_key in line_1_old:
                    if old_key not in line_1:
                        self.AddKey(old_key, keys)
                line_1_old = line_1

        for key in line_1:
            self.AddKey(key, keys)

        for pop_object in self.pop_objects:
            keys.pop(pop_object, wrong_file_format_error)
        return(keys)

    def SymmetricSlice(self, slice=1):
        out_dict = {}
        for dict_key in self.keys_count:
            out_dict[dict_key[slice:slice*-1]] = self.keys_count[dict_key]
        self.keys_count = out_dict

    def AddKey(self, key, keys):
        try:
            keys[key] += 1
        except:
            keys[key] = 1
