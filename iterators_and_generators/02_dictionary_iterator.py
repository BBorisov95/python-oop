class dictionary_iter:

     def __init__(self, dictionary: dict):
         self.dict_tuple = tuple(dictionary.items())
         self.i = 0

     def __iter__(self):
         return self

     def __next__(self):
         if self.i < len(self.dict_tuple):
             i = self.i
             self.i += 1
             return self.dict_tuple[i]
         else:
             raise StopIteration()