print("Enter pH Value: ");
ph = input();
ph_float = float(ph)
if (ph_float < 7.5 and ph_float >= 3):
    print("Liquid is Acidic");
elif(ph_float < 3):
    print("Warning: Liquid is strongly Acidic");
else:
    print("No Acidity , pH value is: ", ph)