def run():
    import os

    print('hello world!')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    k = int(input("How many decimal places you want: "))

    #here you go>>>

    i = b**2
    i = i-4*a*c
    i = i**0.5

    x = -b+i
    x = x/(2*a)
    #or
    y = -b-i
    y = y/(2*a)

    try:
        print(f"{round(x,k)} or {round(y,k)}")
    except:
        print(f"{x} or {y}")
        
    os.system('pause')

for i in range(3):
    run()

print("Dont be Lazy man")

#coded by Devil-prog
