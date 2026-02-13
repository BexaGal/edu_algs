need = int(input("1 - volume\n2 - density\n3 - mass\nEnter option: "))
if need == 1:
    dens = int(input("Density: "))
    mass = int(input("Mass: "))
    print("Volume = " + str(mass/dens))
    exit(0)
elif need == 2:
    volume = int(input("Volume: "))
    mass = int(input("Mass: "))
    print("Density = " + str(volume/mass))
    exit(0)
elif need == 3:
    volume = int(input("Volume: "))
    dens = int(input("Density: "))
    print("Mass = " + str(volume*dens))
    exit(0)
else:
    print("No such option")
