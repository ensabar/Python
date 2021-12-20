
def Fibonacci(it):
    fibonacci = 0
    for i in it:
        fibonacci += i
    return fibonacci




def main():
   for f in range (8):
        print(Fibonacci(f))


if __name__ == "__main__":
    main()