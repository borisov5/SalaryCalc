import tkinter as tk

from calculations import employee_calculations, employer_calculations
from data_service import get_all_data, get_employer_data


def clear_window(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def before_calculations(window: tk.Tk):
    tk.Label(window, text='Основна месечна заплата', bg='#d4f1f9').grid(sticky='W', row=0, column=0)
    basic_monthly_salary = tk.Entry(window, width=8)
    basic_monthly_salary.grid(sticky='E', row=0, column=1)
    tk.Label(window, text='лв.', bg='#d4f1f9').grid(sticky='W', row=0, column=2)

    tk.Label(window, text='Професионален стаж', bg='#d4f1f9').grid(sticky='W', row=1, column=0)
    professional_experience = tk.Entry(window, width=4)
    professional_experience.insert(0, "0.6")
    professional_experience.grid(sticky='E', row=1, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=1, column=2)

    tk.Label(window, text='Години', bg='#d4f1f9').grid(sticky='W', row=2, column=0)
    years = tk.Entry(window, width=4)
    years.grid(sticky='E', row=2, column=1)

    tk.Label(window, text='Вноски за служителя:', bg='#d4f1f9').grid(sticky='W', row=3, column=0)

    tk.Label(window, text='Данък общ доход - ДОО', bg='#d4f1f9').grid(sticky='W', row=4, column=0)
    tk.Label(window, text='8.38', bg='#d4f1f9').grid(sticky='E', row=4, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=4, column=2)
    income_tax = 8.38

    tk.Label(window, text='Данък задължително пенсионно осигуряване - ДЗПО', bg='#d4f1f9').grid(sticky='W', row=5, column=0)
    tk.Label(window, text='2.20', bg='#d4f1f9').grid(sticky='E', row=5, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=5, column=2)
    additional_mandatory_pension_insurance = 2.2

    tk.Label(window, text='Здравно осигуряване - ЗО', bg='#d4f1f9').grid(sticky='W', row=6, column=0)
    tk.Label(window, text='3.20', bg='#d4f1f9').grid(sticky='E', row=6, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=6, column=2)
    health_insurance = 3.2

    tk.Label(window, text='Данък върху доходите на физически лица - ДДФЛ', bg='#d4f1f9').grid(sticky='W', row=7, column=0)
    tk.Label(window, text='10', bg='#d4f1f9').grid(sticky='E', row=7, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=7, column=2)
    personal_income_tax = 10

    tk.Label(window, text='Вноски за работодателя:', bg='#d4f1f9').grid(sticky='W', row=8, column=0)

    tk.Label(window, text='Данък общ доход - ДОД', bg='#d4f1f9').grid(sticky='W', row=9, column=0)
    tk.Label(window, text='10.92', bg='#d4f1f9').grid(sticky='E', row=9, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=9, column=2)
    employer_income_tax = 10.92

    tk.Label(window, text='Данък задължително пенсионно осигуряване - ДЗПО', bg='#d4f1f9').grid(sticky='W', row=10, column=0)
    tk.Label(window, text='2.80', bg='#d4f1f9').grid(sticky='E', row=10, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=10, column=2)
    employer_additional_mandatory_pension_insurance = 2.80

    tk.Label(window, text='Трудова злополука и професионална болест - ТЗПБ', bg='#d4f1f9').grid(sticky='W', row=11, column=0)
    tk.Label(window, text='0.40', bg='#d4f1f9').grid(sticky='E', row=11, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=11, column=2)
    accident_at_work_and_occupational_disease = 0.4

    tk.Label(window, text='Здравно осигуряване - ЗО', bg='#d4f1f9').grid(sticky='W', row=12, column=0)
    tk.Label(window, text='4.80', bg='#d4f1f9').grid(sticky='E', row=12, column=1)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=12, column=2)
    employer_health_insurance = 4.80

    def calculate():
        employee_args = employee_calculations(
            basic_monthly_salary.get(),
            professional_experience.get(),
            years.get(),
            income_tax,
            additional_mandatory_pension_insurance,
            health_insurance,
            personal_income_tax,
        )

        employer_args = employer_calculations(
            basic_monthly_salary.get(),
            professional_experience.get(),
            years.get(),
            employer_income_tax,
            employer_additional_mandatory_pension_insurance,
            accident_at_work_and_occupational_disease,
            employer_health_insurance,
        )

        if employee_args and employer_args:
            after_calculations(window)
            print("Въведените данни са правилни")
        else:
            print("Въведените данни са грешни")
            tk.Label(window, text='Въведените данни са грешни').grid(row=14)

    tk.Button(
        window,
        text="Изчисли",
        bg='green',
        fg='black',
        command=lambda: calculate()
    ).grid(row=13)


def after_calculations(window: tk.Tk):
    clear_window(window)

    data = get_all_data()

    employer_data = get_employer_data()

    tk.Label(window, text='Основна месечна заплата', bg='#d4f1f9').grid(sticky='W', row=0, column=0)
    tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=0, column=2)

    tk.Label(window, text='Осигурителен доход', bg='#d4f1f9').grid(sticky='W', row=1, column=0)
    tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=1, column=2)

    tk.Label(window, text='Професионален стаж', bg='#d4f1f9').grid(sticky='W', row=2, column=0)
    tk.Label(window, text='%', bg='#d4f1f9').grid(sticky='W', row=2, column=2)

    tk.Label(window, text='Години', bg='#d4f1f9').grid(sticky='W', row=3, column=0)

    tk.Label(window, text='Вноски за служителя:', bg='#d4f1f9').grid(row=4, column=0)

    tk.Label(window, text='Данък общ доход - 8.38%', bg='#d4f1f9').grid(sticky='W', row=5, column=0)
    tk.Label(window, text='Данък задължително пенсионно осигуряване - 2.20%', bg='#d4f1f9').grid(sticky='W', row=6, column=0)
    tk.Label(window, text='Здравно осигуряване - 3.20%', bg='#d4f1f9').grid(sticky='W', row=7, column=0)
    tk.Label(window, text='Данъчна основа за облагане с ДДФЛ', bg='#d4f1f9').grid(sticky='W', row=8, column=0)
    tk.Label(window, text='Нетна сума за получаване', bg='#d4f1f9').grid(sticky='W', row=9, column=0)

    tk.Label(window, text='Вноски за работодателя:', bg='#d4f1f9').grid(row=10, column=0)

    tk.Label(window, text='Данък общ доход - 10.92%', bg='#d4f1f9').grid(sticky='W', row=11, column=0)
    tk.Label(window, text='Данък задължително пенсионно осигуряване - 2.80%', bg='#d4f1f9').grid(sticky='W', row=12, column=0)
    tk.Label(window, text='Трудова злополука и професионална болест - 0.40%', bg='#d4f1f9').grid(sticky='W', row=13, column=0)
    tk.Label(window, text='Здравно осигуряване - 4.80%', bg='#d4f1f9').grid(sticky='W', row=14, column=0)
    tk.Label(window, text='Общо разходи за работодателя - 18.92%', bg='#d4f1f9').grid(sticky='W', row=15, column=0)

    for i in data:
        tk.Label(window, text=i['BMS'], bg='#d4f1f9').grid(sticky='E', row=0, column=1)
        tk.Label(window, text=i['SSI'], bg='#d4f1f9').grid(sticky='E', row=1, column=1)
        tk.Label(window, text=i['PE'], bg='#d4f1f9').grid(sticky='E', row=2, column=1)
        tk.Label(window, text=i['Y'], bg='#d4f1f9').grid(sticky='E', row=3, column=1)

        tk.Label(window, text=i['IT'], bg='#d4f1f9').grid(sticky='E', row=5, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=5, column=2)
        tk.Label(window, text=i['AMPI'], bg='#d4f1f9').grid(sticky='E', row=6, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=6, column=2)
        tk.Label(window, text=i['HI'], bg='#d4f1f9').grid(sticky='E', row=7, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=7, column=2)
        tk.Label(window, text=i['TB'], bg='#d4f1f9').grid(sticky='E', row=8, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=8, column=2)
        tk.Label(window, text=i['NATBR'], bg='#d4f1f9').grid(sticky='E', row=9, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=9, column=2)

    for i in employer_data:
        tk.Label(window, text=i['EIT'], bg='#d4f1f9').grid(sticky='E', row=11, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=11, column=2)
        tk.Label(window, text=i['EAMPI'], bg='#d4f1f9').grid(sticky='E', row=12, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=12, column=2)
        tk.Label(window, text=i['AWOD'], bg='#d4f1f9').grid(sticky='E', row=13, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=13, column=2)
        tk.Label(window, text=i['EHI'], bg='#d4f1f9').grid(sticky='E', row=14, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=14, column=2)
        tk.Label(window, text=i['TCTTE'], bg='#d4f1f9').grid(sticky='E', row=15, column=1)
        tk.Label(window, text='лв', bg='#d4f1f9').grid(sticky='W', row=15, column=2)
