print("Enter population: ");
pop = input();
print("Enter land area: ");
land = input();
r = range (10000000,35000000);
pop_float = float(pop);
land_float = float(land);
land_d = pop_float / land_float
if (pop_float < 10000000):
    print ("Population is:" , pop_float);
    if (land_d > 100):
        print ("Desely Populated");
    else:
        print ("Sparsely Popolated");
elif (pop_float in r):
    print ("Population is:" , pop_float);
    if (land_d > 100):
        print ("Desely Populated");
    else:
        print ("Sparsely Popolated");
else:
    if (land_d > 100):
        print ("Desely Populated");
    else:
        print ("Sparsely Popolated");
