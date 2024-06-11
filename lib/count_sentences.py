#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # This uses the setter method
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith("?")
    def is_exclamation(self):
        return self.value.endswith("!")
      
    def count_sentences(self, sentence):
        count  = []
        split_word = self.value.str.split('?', '.', '!')
        return split_word
        
        
        
      
edd = MyString("edd?")    
print(edd.is_sentence())
print(edd.is_question())
print(edd.is_sentence())
        
        
      
   
    
  
