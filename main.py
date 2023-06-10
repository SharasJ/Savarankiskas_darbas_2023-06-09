# Pirma uzduotis:

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} successfully."

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount} successfully."
        else:
            return "Insufficient funds. Withdrawal failed."

    def get_balance(self):
        return self.balance


account = BankAccount("1234567890")

print(account.deposit(1000))

print(account.withdraw(500))

balance = account.get_balance()
print("Account Balance:", balance)


# Antra uzduotis:

class Figure:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Rectangle(Figure):
    pass


class RightTriangle(Figure):
    def calculate_area(self):
        return 0.5 * self.length * self.width


rectangle = Rectangle(5, 10)
triangle = RightTriangle(3, 4)

print("Stačiakampio informacija:")
print("Plotas:", rectangle.calculate_area())
print("Perimetras:", rectangle.calculate_perimeter())
print()

print("Stačiojo trikampio informacija:")
print("Plotas:", triangle.calculate_area())
print("Perimetras:", triangle.calculate_perimeter())




# trecia uduotis


import logging


logging.basicConfig(filename='rezultatai.log', level=logging.INFO)


def apskaiciuoti_plota_ir_perimetra(ilgis, plotis):
    plotas = ilgis * plotis
    perimetras = 2 * (ilgis + plotis)
    return plotas, perimetras


def ivesti_staciakampio_parametrus():
    ilgis = float(input("Įveskite stačiakampio ilgį: "))
    plotis = float(input("Įveskite stačiakampio plotį: "))
    return ilgis, plotis



if __name__ == '__main__':
    ilgis, plotis = ivesti_staciakampio_parametrus()
    plotas, perimetras = apskaiciuoti_plota_ir_perimetra(ilgis, plotis)


    print("Stačiakampio plotas:", plotas)
    print("Stačiakampio perimetras:", perimetras)


    logging.info("Stačiakampio plotas: %s", plotas)
    logging.info("Stačiakampio perimetras: %s", perimetras)

# ketvirta uzduotis:

import tkinter as tk

def convert_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{celsius:.2f} °C")

def convert_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    result_label.config(text=f"{fahrenheit:.2f} °F")

# Sukuriame pagrindinį langą
root = tk.Tk()
root.title("Temperatūros konverteris")

# Sukuriame temperatūros įvedimo laukelį
entry = tk.Entry(root)
entry.pack()

# Sukuriame mygtukus
celsius_button = tk.Button(root, text="Celsius → Fahrenheit", command=convert_to_fahrenheit)
celsius_button.pack()

fahrenheit_button = tk.Button(root, text="Fahrenheit → Celsius", command=convert_to_celsius)
fahrenheit_button.pack()

# Sukuriame rezultato teksto etiketę
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

#penkta uzduotis:

from PIL import Image, ImageEnhance

def apply_contrast(image_path, output_path, contrast_factor):
    # Užkrauname nuotrauką
    image = Image.open(image_path)

    # Sukuriame kontrasto pakeitimo objektą
    enhancer = ImageEnhance.Contrast(image)

    # Pakeičiame kontrastą
    enhanced_image = enhancer.enhance(contrast_factor)

    # Išsaugome atnaujintą nuotrauką
    enhanced_image.save(output_path)

# Pagrindinė programa
if __name__ == "__main__":
    # Nuotraukos kelias ir pavadinimas
    image_path = r"C:\Users\Jolanta\Documents\Savarankiskas_darbas_2023-06-10\1_0x0_790x520_0x520_how_to_cool_down_your_car.jpg"

    # Atsakymo nuotraukos kelias ir pavadinimas
    output_path = r"C:\Users\Jolanta\Documents\Savarankiskas_darbas_2023-06-10\1_0x0_790x520_0x520_how_to_cool_down_your_car_contrast.jpg"

    # Kontrasto faktorius (1.0 - nesikeičia, >1.0 - didėja kontrastas, <1.0 - mažėja kontrastas)
    contrast_factor = 1.5

    # Taikome kontrastą ir išsaugome atnaujintą nuotrauką
    apply_contrast(image_path, output_path, contrast_factor)