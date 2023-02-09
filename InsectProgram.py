def main():

    import InsectClass as i

    bug1 = i.Insect('mosquito', 2, 6)
    bug2 = i.Insect('housefly', 2, 6)

    

    bug1.lengthOfFlight()
    bug2.lengthOfFlight()

    print(f"The {bug1.nameOfInsect()} can fly up to {bug1.lengthOfFlight()}")
    print(f"The {bug2.nameOfInsect()} can fly up to {bug2.lengthOfFlight()}")

main()
