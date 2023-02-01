with open("Titanic.csv") as f:
    with open("predictions/Titanic2.csv","w") as f2:
        for i in f:
            i = i.replace("\n","")
            if ",," not in i:
                f2.write(i)
                f2.write("\n")
            