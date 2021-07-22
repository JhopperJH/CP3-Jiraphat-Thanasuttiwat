def findV():
    s = int(input("Displacement(km) : "))
    t = int(input("Used time(hr) : "))
    if s >= 1 and t >= 1:
        print(f"Velocity = {s/t} km/hr")
    else:
        print("Displacement and Used time should equal to or more than 1")
        findV()
findV()