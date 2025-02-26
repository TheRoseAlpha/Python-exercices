# Functions
def celsius_in_fahrenheit(temp_cel):
    temp_far = (temp_cel *(9/5)) + 32
    print(f"{temp_cel:.2f}°C = {temp_far:.2f} F")
# celsius_in_fahrenheit(10)


def fahrenheit_in_celsius(temp_far):
    temp_cel = ((temp_far - 32)*(5/9))
    print(f"{temp_far:.2f} F = {temp_cel:.2f}°C")
# fahrenheit_in_celsius(10)


def celsius_a_kelvin(temp_cel):
    temp_kel = temp_cel + 273.15
    print(f"{temp_cel:.2f}°C = {temp_kel:.2f} K")
# celsius_a_kelvin(10)


def kelvin_in_celsius(temp_kel):
    temp_cel = temp_kel - 273.15
    print(f"{temp_kel:.2f} K = {temp_cel:.2f}°C")
# kelvin_in_celsius(10)




# Temperature converter begin
print("Temperature Converter")
temperature = float(input("Enter the temperature: "))


while True:
    print("Choose the convertion: \n"
        "1. Celsius to Fahrenheit\n"
        "2. Fahrenheit to Celsius\n"
        "3. Celsius to Kelvin\n"
        "4. Kelvin to Celsius\n")
    convertion_type = int(input("Enter your choice (1-4): "))
    try:
        if convertion_type not in range(1, 5):
            raise Exception
        else:
            break
    except Exception:
        print("Wrong choice")


if convertion_type == 1:
    celsius_in_fahrenheit(temperature)
elif convertion_type == 2:
    fahrenheit_in_celsius(temperature)
elif convertion_type == 3:
    celsius_a_kelvin(temperature)
elif convertion_type == 4:
    kelvin_in_celsius(temperature)