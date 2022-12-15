import tkinter as tk
import os

root = tk.Tk()
root.title("SolarPy")
while True:
    texto = tk.Label(root, text='SIMULAÇÕES PLANETÁRIAS')
    texto.grid(column=0, row=0, padx=10, pady=10)
    botao1 = tk.Button(root, text='Sistema solar', command=lambda: os.system('solarsystem.py'))
    botao1.grid(column=0, row=1, padx=10, pady=10)
    botao2 = tk.Button(root, text='Terra', command=lambda: os.system('earth.py'))
    botao2.grid(column=0, row=2, padx=10, pady=10)
    botao3 = tk.Button(root, text='Jupiter', command=lambda: os.system('jupiter.py'))
    botao3.grid(column=0, row=3, padx=10, pady=10)
    root.quit()
    root.mainloop()