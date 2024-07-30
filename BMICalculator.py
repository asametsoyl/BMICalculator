import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(
    padx=30,
    pady=30
)

def calculate_bmi():
    boy = height_input.get()
    kilo = weight_input.get()

    if boy == "" or kilo == "":
        result_label.config(text="Lütfen geçerli bir değer giriniz!")
    else:
        try:
            bmi = float(kilo)  / (float(boy) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=f"Sizin vücut indexsiniz: {bmi}")
            result_label.config(text=result_string)
        except:
            result_label.config(text="Lütfen geçerli bir değer giriniz!")
#weight
weightinput_label = tkinter.Label(
    text=("Kilonuzu Giriniz(kg)")
)
weightinput_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()

#height
heightinput_label = tkinter.Label(
    text="Boyunuzu Giriniz(cm)"
)
heightinput_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()

#button
calculate_button = tkinter.Button(text="Hesapla",command=calculate_bmi)
calculate_button.pack()

#sonuç
result_label = tkinter.Label()
result_label.pack()

#index
def write_result(bmi):
    result_string = f"Sizin vücut indexsiniz: {round(bmi,2)}. Siz:"
    if bmi <= 16:
        result_string += "Çok zayıfsın"
    elif bmi > 16 and bmi <= 17:
        result_string += "Biraz zayıfsın"
    elif bmi > 17 and bmi <= 18.5:
        result_string += "Zayıfsın"
    elif bmi > 18.5 and bmi <= 25:
        result_string += "Normalsiniz"
    elif bmi > 25 and bmi <= 30:
        result_string += "Şişmansınız"
    elif bmi > 30 and bmi <= 35:
        result_string += "Obez seviye 1"
    elif bmi > 35 and bmi <=40:
        result_string += "Obez seviye 2"
    else:
        result_string += "Obez seviye 3"
    return result_string


window.mainloop()