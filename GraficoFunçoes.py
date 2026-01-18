import matplotlib.pyplot as plt
import numpy as np 
import sympy as sp
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("340x520")
app.title("Grafico de Funções")
app.resizable(False, False)

MenuPrincipal = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
MenuPrincipal.pack(padx=5 ,pady=15)

def Menu():
        TituloMenu = ctk.CTkLabel(MenuPrincipal, text="ESCREVA A FUNÇÂO:", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
        TituloMenu.place(x=10, y=50)
        EntradaFun = ctk.CTkEntry(MenuPrincipal, width=200,height=50, placeholder_text="Função...", bg_color="#222222")
        EntradaFun.place(x=65, y=150)
        def Grafico():
                try:
                    plt.clf()
                    plt.close("all")
                    x = sp.symbols("x")

                    Funcao_Str = str(EntradaFun.get())

                    Funcao = sp.sympify(Funcao_Str)
 
                    f = sp.lambdify(x, Funcao, "numpy")

                    ValoresX = np.linspace(-5,5,1000)
                    ValoresY = f(ValoresX)
                    plt.plot(ValoresX,ValoresY,'--r',linewidth=2)
                    plt.title("Grafico da Função:")
                    plt.xlabel("x")
                    plt.ylabel(Funcao_Str)
                    plt.xlim([-5,6])
                    plt.ylim([-5, 20])
                    plt.grid()
                    EntradaFun.delete(0,"end")
                    plt.show(block=False)
                except Exception:
                    pass
        BotaoCriarGrafico = ctk.CTkButton(MenuPrincipal, width=150, height=75, text="Fazer grafico",command=Grafico, bg_color="#222222", fg_color="#0058CC", border_color="black", border_width=4)
        BotaoCriarGrafico.place(x=100, y=300)

    
Menu()
app.mainloop()