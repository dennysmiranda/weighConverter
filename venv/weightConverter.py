weight = int(input("How much do you weight? "))
unit = input("L(bs) or K(bs): ")

if unit.upper() == "L":
    converter = weight * 0.45
    print(f'You weigh {converter} kilos.')

else:
    converter = weight / 0.45
    print(f'You weight {converter} pounds.')
