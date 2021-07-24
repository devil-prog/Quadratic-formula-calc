##########################ON WORKING##########################
#with Gui coming soon
import os

class app:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)    

    def calculate(self, k):
        i = self.b**2
        i = i-4*self.a*self.c
        i = i**0.5

        x = -self.b+i
        x = x/(2*self.a)
        #or
        y = -self.b-i
        y = y/(2*self.a)

        try:
            print(f"{round(x,k)} or {round(y,k)}")
        except:
            print(f"{x} or {y}")

def run():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    a = app(a,b,c)
    a.calculate(2)
    
for i in range(3):
    run()
    os.system('pause')

print("Dont be Lazy man")
os.system('pause')

#coded by Devil-prog
