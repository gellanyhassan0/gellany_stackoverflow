class gellany_stackoverflow():
    
# init method or constructor
    def __init__(self, file = None, string = None, number = None, n = None, input = None):
                  
                 self.file = file
                 self.string = string
                 self.number = number
                 self.n = n
                 self.input = input
          

    def sha256(self):

       #https://stackoverflow.com/a/72667770/19362910

       import hashlib
         
       try:
           for f in range(0,10):

              int_bytes = bytes((str(f)+'\n'), 'utf-8')
              print(int_bytes)
              readable_hash = hashlib.sha256(int_bytes).hexdigest()
              print(readable_hash)

       except: 
            with open(self.file, "rb") as f: 
              for int_bytes in f:
                   int_bytes = bytes((str(f)+'\n'), 'utf-8')
                   print(int_bytes)
                   readable_hash = hashlib.sha256(int_bytes).hexdigest()
                   print(readable_hash)
                
    def string_nospace(self):
            
            #https://stackoverflow.com/a/72675960/19362910
            
            s = self.string
            i = 0
            sample = []
            for i in range(0, len(s), 1):

                          try :
                             a = s[i:i+3]
                             b = s[i:i+4]
                             c = s[i:i+5]
                             d = s[i:i+6]


                             sample.append(a)
                             sample.append(b)
                             sample.append(c) 
                             sample.append(d)



                          except Exception:
                                          pass

            for number in sample :
               if sample.count(number) > 1 and number in ["red", "blue", "green", "yellow"]:
                           print(number)
                    
    def stringtocsv(self):
               
               #https://stackoverflow.com/questions/72682079/read-txt-file-into-pandas-dataframe
                
               import csv
               import pandas as pd
               import io

               colnames = ['time', 'name', 'id', 'password']

               file = open(self.file)
               lines = file.read()
               print(lines)
               new_line = lines.replace('"name":', ',').replace('"id":', ',').replace('"password":', ',').replace(' ,', '').replace(' {', '').replace('}', '')
               print(new_line)

               TESTDATA= new_line
               df = pd.read_csv(io.StringIO(TESTDATA), names=colnames)
               print(df) 
   
    def fizzBuzz(self):
                n = self.number
                for i in range(1,n+1):
                        if i % 3 == 0 and i % 5 == 0:
                            print("FizzBuzz")
                        elif i % 3 == 0 and i % 5 != 0:
                            print("Fizz")
                        elif i % 5 == 0 and i % 3 != 0:
                            print("Buzz")
                        else:
                            print(i)


    
    def reverse_words_order_and_swap_cases(self):
        sentence = self.sentence
        newstring ='' 
        for a in sentence:
             if (a.isupper()) == True :
                newstring += (a.lower())
             elif (a.islower()) == True :
                newstring += (a.upper())
             elif (a.isspace()) == True :
                newstring += a 
             elif (a.isnumeric()) == True:
                newstring += a
             elif a == '"' or a == '.' :
                newstring += a
             else:
                 newstring += a
        #print(newstring)        

        string = newstring.split()
        words = list(reversed(string))
        print(" ".join(words))       
    
    def nested_input(self):
        n = self.n
        list_score = []
        list_final = []
        for x in range(0,n):
                name = input()
                score = float(input())
                list_score.append(score)
                list_final.append([name, score])

        second_score = sorted(set(list_score))[1]
        for i in (sorted(list_final)):
            if second_score in i:
                print(i[0])
                
                
    def mean_input(self):

        n = self.n
        
        name = []
        for a in range(0,n+1):
                        name.append(input().split())
        #print(name)
        #print(''.join(name[-1]))
        last = ''.join(name[-1])
        average = []

        for i,sl in enumerate(name):
            if last in sl :
                #print(sl)
                lst = [float(z) for z in sl[1:4]]
                average.append(sum(lst)/3)

        print("%.2f" % (average)[0])            
      
    def regex_valid(self):
        
        import re
        for _ in range(self.n):
            try:
                re.compile(input())
                Output = True
            except re.error:
                Output = False

            print(Output)      
    
        
    
    def miniMaxSum(self):
            import math
            import os
            import random
            import re
            import sys
            arr = list(map(int, input().rstrip().split()))
            arr = sorted(arr)
            x = 0
            y = 0
            for i in arr[0:-1]:
               x += i
            for i in arr[1:]:
                y += i
            print(x, y)
            
    def score_words(words):
    
    score = 0
    arr = ['a', 'e', 'i', 'o', 'u', 'y']
    #print(words)
    for word in words:
         even_word = ""
         #print(word)
         for i in word:
              if i in arr :
                  even_word +=i
         if len(even_word) % 2 == 0:
            #print(even_word)
            score +=2
         else:
            score +=1
                
    return score     
      

    
gellany_stackoverflow().sha256()
gellany_stackoverflow(file = 'text.txt').sha256()
