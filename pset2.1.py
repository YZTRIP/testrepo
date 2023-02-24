def main():
    Amount_due = 50
    while True:
        Amount_in = int(input("Please put in: "))
        if Amount_in == 25 or Amount_in == 10 or Amount_in == 5:
            Amount_due -= Amount_in
            if Amount_due > 0:
                print("Amount Due:", Amount_due)
            else:
                break
        else:
            print("Amount Due: 50")
    while Amount_due <= 0:
        print(f"Change Owed:", abs(Amount_due))

main()