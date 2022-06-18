class gellany_stackoverflow():
    
# init method or constructor
    def __init__(self, file = None):
                  
                 self.file = file
          

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



gellany_stackoverflow().sha256()
gellany_stackoverflow(file = 'text.txt').sha256()
