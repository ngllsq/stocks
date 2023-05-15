import tkinter as tk
import customtkinter
import tkinter.ttk as ttk
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_csv(r'C:\Users\nglls\OneDrive\Рабочий стол\stocks.csv')

class window:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x500")
        self.master.title("Faberlic")
        self.master.configure(bg="#020111")
        
        self.label = tk.Label(self.master,
                               text="Мы собрали данные компании Faberlic c 2013 по 2021 год,\n проанализировали их и создали модель машинного обучения.\n Результаты нашей работы вы можете наблюдать в этом приложении",
                               font = ('Courier', 15), bg="#020111", fg="white", padx=20, pady=20)
        self.label.pack()
        self.revenue_button = customtkinter.CTkButton(self.master, text="Акции",
                                                      fg_color="#6335CB", hover_color="#5AC5AC", width = 170, height = 50,
                                                      command=self.new_window, font = ('Courier', 15))
        self.revenue_button.pack(padx=10, pady=10)

    def new_window(self):
        self.window1 = tk.Toplevel(self.master)
        self.window1.geometry("1000x500")
        self.window1.title("Акции")
        self.window1.configure(bg="#020111")

        self.trend_and_sesonal_button = customtkinter.CTkButton(self.window1, text="Тренд и Сезонность", 
                                                                command=self.window_trend_and_sesonal, fg_color="#6335CB", 
                                                                hover_color="#5AC5AC", width = 180, height = 50, 
                                                                font = ('Courier', 16))
        self.trend_and_sesonal_button.pack(padx=10, pady=10)

        self.sesonal_button = customtkinter.CTkButton(self.window1, text="Динамика дохода по сезонам", 
                                                              command = self.sesonal, fg_color="#6335CB", 
                                                              hover_color="#5AC5AC", width = 180, height = 50,
                                                              font = ('Courier', 16))
        self.sesonal_button.pack(padx=10, pady=10)

        self.stationarity_button = customtkinter.CTkButton(self.window1, text="Стационарность", 
                                                           command = self.stationarity, fg_color="#6335CB", 
                                                           hover_color="#5AC5AC", width = 180, height = 50,
                                                           font = ('Courier', 16))
        self.stationarity_button.pack(padx=10, pady=10)

        self.predict_button = customtkinter.CTkButton(self.window1, text="Прогнозирование", 
                                                      command = self.predictions, fg_color="#6335CB", 
                                                      hover_color="#5AC5AC", width = 180, height = 50,
                                                      font = ('Courier', 16))
        self.predict_button.pack(padx=10, pady=10)

    def window_trend_and_sesonal(self):
        plt.plot(df['weaks'], df['stocks'])
        plt.title('График акций')
        plt.xlabel('Недели')
        plt.ylabel('Акции')
        plt.show()

    def sesonal(self):
        self.sesonal_window = tk.Toplevel(self.master)
        self.sesonal_window.geometry("1000x500")
        self.sesonal_window.title("Динамика дохода по сезонам")
        self.sesonal_window.configure(bg="#020111")

        self.winter_button = customtkinter.CTkButton(self.sesonal_window, text="Зима", 
                                       command = self.winter, fg_color="#6335CB", 
                                       hover_color="#5AC5AC", width = 150, height = 50, font = ('Courier', 16))
        self.winter_button.pack(padx=10, pady=10)

        self.spring_button = customtkinter.CTkButton(self.sesonal_window, text="Весна", 
                                       command = self.spring, fg_color="#6335CB", 
                                       hover_color="#5AC5AC", width = 150, height = 50, font = ('Courier', 16))
        self.spring_button.pack(padx=10, pady=10)

        self.summer_button = customtkinter.CTkButton(self.sesonal_window, text="Лето", 
                                       command = self.summer, fg_color="#6335CB", 
                                       hover_color="#5AC5AC", width = 150, height = 50, font = ('Courier', 16))
        self.summer_button.pack(padx=10, pady=10)

        self.autumn_button = customtkinter.CTkButton(self.sesonal_window, text="Осень", 
                                       command = self.autumn, fg_color="#6335CB", 
                                       hover_color="#5AC5AC", width = 150, height = 50, font = ('Courier', 16))
        self.autumn_button.pack(padx=10, pady=10)

    def winter(self):
        z = 0
        w13 = []
        w14 = []
        w15 = []
        w16 = []
        w17 = []
        w18 = []
        w19 = []
        w20 = []
        w21 = []
        for i in df['stocks']:
            if z <=7 or 46 < z < 51:
                w13.append(i)
            elif 51 < z <= 59 or 99 < z <= 103:
                w14.append(i)
            elif 103 < z <= 111 or 151 < z <= 155:
                w15.append(i)
            elif 155 < z <= 164 or 203 < z < 207:
                w16.append(i)
            elif 207 < z <= 216 or 255 < z < 259:
                w17.append(i)
            elif 260 < z <= 268 or 307 < z < 312:
                w18.append(i)
            elif 312 < z <= 320 or 359 < z < 364:
                w19.append(i)
            elif 364 < z <= 372 or 412 < z <= 416:
                w20.append(i)
            elif 416 < z < 425 or z > 464:
                w21.append(i)
            z+= 1
        x = list(range(12))
        y1 = w13 
        y2 = w14
        y3 = w15
        y4 = w16
        y5 = w17
        y6 = w18
        y7 = w19
        y8 = w20
        y9 = w21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("WINTER")
        plt.show()

    def spring(self):
        z = 0
        s13 = []
        s14 = []
        s15 = []
        s16 = []
        s17 = []
        s18 = []
        s19 = []
        s20 = []
        s21 = []
        for i in df['stocks']:
            if 7 < z <= 20:
                s13.append(i)
            elif 59 < z <= 72:
                s14.append(i)
            elif 111 < z < 125:
                s15.append(i)
            elif 164 < z <= 177:
                s16.append(i)
            elif 216 < z <= 229:
                s17.append(i)
            elif 268 < z <= 281:
                s18.append(i)
            elif 320 < z <= 333:
                s19.append(i)
            elif 372 < z < 386:
                s20.append(i)
            elif 425 < z <= 438:
                s21.append(i)
            z+= 1
            x = list(range(13))
        y1 = s13 
        y2 = s14
        y3 = s15
        y4 = s16
        y5 = s17
        y6 = s18
        y7 = s19
        y8 = s20
        y9 = s21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("SPRING")
        plt.show()

    def summer(self):
        z = 0
        su13 = []
        su14 = []
        su15 = []
        su16 = []
        su17 = []
        su18 = []
        su19 = []
        su20 = []
        su21 = []
        for i in df['stocks']:
            if 20 < z <= 33:
                su13.append(i)
            elif 72 < z < 86:
                su14.append(i)
            elif 125 < z <= 138:
                su15.append(i)
            elif 177 < z <= 190:
                su16.append(i)
            elif 229 < z <= 242:
                su17.append(i)
            elif 281 < z <= 294:
                su18.append(i)
            elif 333 < z <= 346:
                su19.append(i)
            elif 386 < z <= 399:
                su20.append(i)
            elif 438 < z <= 451:
                su21.append(i)
            z+= 1
            x = list(range(13))
        y1 = su13 
        y2 = su14
        y3 = su15
        y4 = su16
        y5 = su17
        y6 = su18
        y7 = su19
        y8 = su20
        y9 = su21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("SUMMER")
        plt.show()

    def autumn(self):
        z = 0
        a13 = []
        a14 = []
        a15 = []
        a16 = []
        a17 = []
        a18 = []
        a19 = []
        a20 = []
        a21 = []
        for i in df['stocks']:
            if 33 < z <= 46:
                a13.append(i)
            elif 86 < z <= 99:
                a14.append(i)
            elif 138 < z <= 151:
                a15.append(i)
            elif 190 < z <= 203:
                a16.append(i)
            elif 242 < z <= 255:
                a17.append(i)
            elif 294 < z <= 307:
                a18.append(i)
            elif 346 < z <= 359:
                a19.append(i)
            elif 399 < z <= 412:
                a20.append(i)
            elif 451 < z <= 464:
                a21.append(i)
            z+= 1
            x = list(range(13))
        y1 = a13 
        y2 = a14
        y3 = a15
        y4 = a16
        y5 = a17
        y6 = a18
        y7 = a19
        y8 = a20
        y9 = a21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("AUTUMN")
        plt.show()

    def stationarity(self):
        self.stationarity_window = tk.Toplevel(self.master)
        self.stationarity_window.geometry("1000x500")
        self.stationarity_window.title("Стационарность")
        self.stationarity_window.configure(bg="#020111")
        adf_result = adfuller(df['stocks'])
        adf_text = f"ADF Statistic: {adf_result[0]:.4f}\n"
        adf_text += f"p-value: {adf_result[1]:.4f}\n"
        adf_text += "Critical Values:\n"
        for key, value in adf_result[4].items():
            adf_text += f"\t{key}: {value:.4f}\n"
        self.adfuller_label = tk.Label(self.stationarity_window, text="Для проверки временного ряда мы использовали тест Дики-Фуллера.\n Это статистический тест, который используется\n для проверки наличия единичных корней во временных рядах.", 
                                       bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
        self.adfuller_label.pack()
        self.stationarity_label = tk.Label(self.stationarity_window, text=adf_text, bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 16))
        self.stationarity_label.pack()
        if adf_result[1] > 0.05:
            self.unstat = tk.Label(self.stationarity_window, text="Временной ряд нестационарен", 
                                       bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
            self.unstat.pack()
        else:
            self.stat = tk.Label(self.stationarity_window, text="временной ряд является стационарным", 
                                       bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
            self.stat.pack()


    def predictions(self):
        self.predictions_window = tk.Toplevel(self.master)
        self.predictions_window.geometry("1000x500")
        self.predictions_window.title("Прогнозирование")
        self.predictions_window.configure(bg="#020111")
        self.predictions_label = tk.Label(self.predictions_window, text='Введите количество недель для прогнозирования:',
                              bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
        self.predictions_label.pack()
        self.days_entry = tk.Entry(self.predictions_window, width=15, font=('Courier', 12))
        self.days_entry.pack()
        self.button_pred = customtkinter.CTkButton(self.predictions_window, text='Сделать прогноз', 
                                                   command=self.prediction, fg_color="#6335CB", 
                                                   hover_color="#5AC5AC", width = 150, height = 50, font = ('Courier', 16))
        self.button_pred.pack(padx=10, pady=10)
        

    def prediction(self):
        days_entry_value = self.days_entry.get()
        if len(days_entry_value.strip()) == 0:
            self.label = tk.Label(self.predictions_window, text='Ошибка: Вы не вели количество недель!',
                                  bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
            self.label.pack()
        else:
            days = int(days_entry_value)
            if days == 0:
                self.label = tk.Label(self.predictions_window, text='Ошибка: количество недель должно быть больше нуля!',
                                      bg="#020111", fg="white", padx=20, pady=20, font = ('Courier', 15))
                self.label.pack()
            else:
                df['weaks'] = pd.to_datetime(df['weaks'], infer_datetime_format=True)
                df.set_index('weaks', inplace = True)
                model2 = SARIMAX(df, order=(1, 0, 1), seasonal_order=(1, 1, 0, 108))
                model_fit = model2.fit()
                global pred
                pred = model_fit.forecast(days)
                
                label = tk.Label(self.predictions_window, text=pred, font = ('Courier', 15), bg="#020111", fg="white", padx=20, pady=20)
                label.pack()
                self.button_graphics = customtkinter.CTkButton(self.predictions_window, 
                                                               text='Посмотреть графическое представление спрогнозированных данных',
                                                               command=self.prediction_graphics, 
                                                               fg_color="#6335CB", hover_color="#5AC5AC", 
                                                               width = 150, height = 50, font = ('Courier', 16))
                self.button_graphics.pack(padx=10, pady=10)

                
    def prediction_graphics(self):
        plt.figure(figsize=(12, 6))
        plt.plot(pred)
        plt.title('График акций')
        plt.xlabel('Недели')
        plt.ylabel('Акции')
        plt.show()


if __name__ == '__main__':
    root = tk.Tk()
    app = window(root)
    root.mainloop()