
# begin
first_rider_age = int(input(f"What is the age of the first rider?"))
first_rider_height = int(input(f"What is the height of the first?"))

# check for the first rider
if first_rider_height >= 36 and first_rider_age >= 18:
    print("\nYou are eligible to ride with yourself or a second person.")
    second_rider_input = True
elif first_rider_height >= 36 and first_rider_age < 18:
    print("\nYou are eligible to ride but only with a second person to accompany you.")
    second_rider_input = True
elif first_rider_height < 36:
    print("\nYou are not eligible to ride, bozo.")
    second_rider_input = False
else: print("error")

# check for the second rider if true.
if second_rider_input == True:
    second_rider = input("Is there a second rider? (yes/no)")
    if second_rider.lower() == "yes":
        second_rider_age = int(input("What is the age of the second rider?"))
        second_rider_height = int(input("What is the height of the second rider?"))
    if second_rider.lower() == "no":
        print("Enjoy your ride!")
else:
    print()        

if second_rider_age >= 18 and second_rider_height >= 36:
    print("The second rider is eligible to ride by themselves or with a second person.")
elif second_rider_age < 18 and second_rider_height >= 36:
    print("The second rider is eligible to ride but only with a second person to accompany you.")
elif second_rider_age < 36:
    print("The second rider is not eligible to ride")
else: print("error")

# final check for both riders
if (second_rider_input and second_rider == "yes" and second_rider_height < 36) and first_rider_height < 36:
    print("\nNeither of you will be able to ride. womp womp.")