import tkinter as tk
from tkinter import *
from tkinter import ttk
from servidor import Servidor
from client import Client
from codificador import Codificador

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from matplotlib import pyplot as plt
class Aplicacao():
    def __init__(self):

        self.codificador = Codificador()

        self.root = Tk()
        self.root.title("Codificação/Decodificação")
        self.root.configure(background = '#1e3743')
        self.root.geometry("300x100")

        self.criar_botoes_menu_principal()
        self.rodar()

    def rodar(self):
        self.root.mainloop()

    def criar_botoes_menu_principal(self):
        self.bt = Button(self.root,text= "Servidor",command=self.abrir_servidor)
        self.bt.place(relx=0.2,rely=0.4)

        self.bt = Button(self.root,text= "Cliente",command=self.abrir_cliente)
        self.bt.place(relx=0.7,rely=0.4)

    #Cliente
    def abrir_cliente(self):
        self.root.destroy() # close the current window
        self.root = tk.Tk() # create another Tk instance

        self.root.title("Cliente")
        self.root.geometry("500x300")
        self.criar_abas_client()
        self.widgets_botoes_client()

        self.client = Client()
        
        self.root.mainloop()

    def criar_abas_client(self):
        self.abas = ttk.Notebook(self.root)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)

        self.abas.add(self.aba1,text = "Aba 1")
        self.abas.add(self.aba2,text = "Input (Codificado)")
        self.abas.add(self.aba3,text = "Binário (Decodificado)")
        

        self.abas.place(relx = 0,rely =0, relwidth=0.98, relheight=0.98)


    def widgets_botoes_client(self):
        self.bt_receber = Button(self.aba1,text= "Receber Mensagem",command=self.receber_mensagem_client)
        self.bt_receber.place(relx=0.4,rely=0.1,relwidth=0.3)

        self.text = Text(self.aba1)
        self.text.place(rely=0.2)
    
    def receber_mensagem_client(self):
        mnsg = self.client.ler_mensagem()
        mnsg,mnsg_int,mnsg_bin = self.codificador.decodifica_mensagem(mnsg)

        if mnsg != None:
            self.text.delete("1.00","end")
            self.text.insert(END,self.formatar_texto_cliente(mnsg,mnsg_bin,mnsg_int))

        self.plotar_grafico1_client(mnsg_int)
        self.plotar_grafico2_client(mnsg_bin)

    def plotar_grafico1_client(self,mensagem_codificada):

        self.aba2.destroy()
        self.aba2 = Frame(self.abas)
        self.abas.add(self.aba2,text = "Input (Codificado)")

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.step(x = [i for i in range(len(mensagem_codificada))],y = mensagem_codificada,where='post')
        bar1 = FigureCanvasTkAgg(figure1, self.aba2)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def plotar_grafico2_client(self,mensagem):

        self.aba3.destroy()
        self.aba3 = Frame(self.abas)
        self.abas.add(self.aba3,text = "Binário (Decodificado)")

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.step(x = [i for i in range(len(mensagem))],y = mensagem,where='post')
        bar1 = FigureCanvasTkAgg(figure1, self.aba3)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def formatar_texto_cliente(self,mnsg_escrita,mnsg_bin,mnsg_algoritmo):
        return "Mensagem Escrita: " + str(mnsg_escrita) +"\n"+ "Mensagem Binário: " + str(mnsg_bin) + "\n" + "Mensagem Algoritmo: " + str(mnsg_algoritmo) 

    ##SERVIDOR
    def abrir_servidor(self):
        self.root.destroy() # close the current window
        self.root = tk.Tk() # create another Tk instance

        self.root.title("Codificação/Decodificação")
        self.root.geometry("500x300")

        self.servidor = Servidor()
        self.criar_abas_servidor()
        self.widgets_botoes_servidor()
        self.root.mainloop()
        
    def criar_abas_servidor(self):
        self.abas = ttk.Notebook(self.root)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)
        
        self.abas.add(self.aba1,text = "Aba 1")
        self.abas.add(self.aba2,text = "Binário")
        self.abas.add(self.aba3,text = "Codificação")

        self.abas.place(relx = 0,rely =0, relwidth=0.98, relheight=0.98)

    def widgets_botoes_servidor(self):
        self.lb_codigo = Label(self.aba1,text = "Mensagem")
        self.lb_codigo.place(relx=0.05,rely=0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx = 0.05,rely = 0.15,relwidth=0.5)

        self.bt_enviar = Button(self.aba1,text= "Enviar Mensagem",command = self.enviar_mensagem_servidor)
        self.bt_enviar.place(relx=0.6,rely=0.15,relwidth=0.3)
        
        self.text = Text(self.aba1)
        self.text.place(rely=0.3)

    def enviar_mensagem_servidor(self):
        text = self.codigo_entry.get()
        
        mensagem_codificada,mensagem_bin = self.codificador.codificar_mensagem(text)

        self.text.delete("1.00","end")
        self.text.insert(END,self.formatar_texto_servidor(text,mensagem_bin,mensagem_codificada))

        self.plotar_grafico_servidor1(mensagem_bin)
        self.plotar_grafico_servidor2(mensagem_codificada)

        self.servidor.mandar_mensagem(','.join([str(mnsg) for mnsg in mensagem_codificada]))
        self.codigo_entry.delete(0,"end")

    def plotar_grafico_servidor1(self,mensagem):

        self.aba2.destroy()
        self.aba2 = Frame(self.abas)
        self.abas.add(self.aba2,text = "Binário")

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.step(x = [i for i in range(len(mensagem))],y = mensagem,where='post')
        bar1 = FigureCanvasTkAgg(figure1, self.aba2)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def plotar_grafico_servidor2(self,mensagem_codificada):

        self.aba3.destroy()
        self.aba3 = Frame(self.abas)
        self.abas.add(self.aba3,text = "Codificação")

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.step(x = [i for i in range(len(mensagem_codificada))],y = mensagem_codificada,where='post')
        bar1 = FigureCanvasTkAgg(figure1, self.aba3)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def formatar_texto_servidor(self,mnsg_escrita,mnsg_bin,mnsg_algoritmo):
        return "Mensagem Escrita: " + str(mnsg_escrita) +"\n"+ "Mensagem Binário: " + str(mnsg_bin) + "\n" + "Mensagem Algoritmo: " + str(mnsg_algoritmo) 

app = Aplicacao()