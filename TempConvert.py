def fehrToCel(f):
    return (f-32)*(5/9)

def main():
    while True:
        try:
            fehr = int(input("Enter degree fehrenheit: "))

        except ValueError:
            print("Enter numbers only!! Jack\n")
            # exit()
        else:
            break

    print(f"{fehr} to Celcius: ",round(fehrToCel(fehr)))

if __name__ == "__main__":
    main()