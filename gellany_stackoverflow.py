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
        
      
      def Zoos(self) :
            name = self.input  

            z = 0
            o = 0

            for char in name :
                if char == "z":
                    z += 1
                elif char == "o":
                    o += 1

            #print(z)
            #print(o)

            if isinstance(name, str) and len(name) <= 20 and o/2 == z:
                print("Yes")
            else:
                print("No")        # Writing output to STDOUT
                
      def split_houses(self):
        
            number = int(self.input)
            live = self.input

            if number >= 1 and number <= 20 and len(live) == number and not "HH" in live :
                print("YES")
                print(live.replace(".","B"))
            else :
                print("NO")
                
                
      def toggle_String(self) :
        
            name = self.input

            string = ""

            for i in name : 
                if i.islower() == True :
                   string += i.upper()   
                else :
                   string += i.lower()

            print(string)
            
      def palindromic_String(self):
        
            name = self.input  

            upper = 0
            lower = 0

            for s in name :
                if s.isupper() == True:
                    upper += 1
                else :
                    lower += 1

            if lower > 0  and name == name[::-1]:
                print("YES")
            else :
                print("NO")
                
        def Factorial(self) :
            
            n = int(input())
            fact = 1

            for i in range(1,n+1):
                fact = fact * i

            print (fact)
            
        def join(self):
            
            def solve (N, ch):
                return "".join(ch)

            N = int(input())
            ch = input().split()

            out_ = solve(N, ch)
            print (out_)
   
        def string-split-and-join(self):
            def split_and_join(line):
            return line.replace(" ", "-")

       def format_string(self):
        
           def print_full_name(first, last):
                 print("Hello {0} {1}! You just delved into python.".format(first,last))
            
       def replace_specifi_position_character(self):
        
           def mutate_string(string, position, character):
                string = string[:position] + character + string[position+1:]
                return string

    
gellany_stackoverflow().sha256()
gellany_stackoverflow(file = 'text.txt').sha256()
