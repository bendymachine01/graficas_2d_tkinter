from tkinter import *

BASE = 800
ALTURA = 500

ventana = Tk()
ventana.title("Tren en Canvas")

c = Canvas(ventana, width=BASE, height=ALTURA, bg="lightcyan")
c.pack()

# -----------------------------
# Cuerpo principal del tren
# -----------------------------
c.create_rectangle(BASE/10, ALTURA/2.3, BASE/2, ALTURA/1.6, fill="royalblue", outline="black", width=3)

# Cabina del tren
c.create_rectangle(BASE/2, ALTURA/3, BASE/1.4, ALTURA/1.6, fill="deepskyblue", outline="black", width=3)

# Chimenea
c.create_rectangle(BASE/7, ALTURA/3, BASE/6, ALTURA/2.3, fill="dimgray", outline="black", width=2)
c.create_rectangle(BASE/7.5, ALTURA/3.3, BASE/5.5, ALTURA/3, fill="black")

# -----------------------------
# Ruedas
# -----------------------------
c.create_oval(BASE/8, ALTURA/1.7, BASE/6, ALTURA/1.55, fill="black")
c.create_oval(BASE/4, ALTURA/1.7, BASE/3, ALTURA/1.55, fill="black")
c.create_oval(BASE/2.5, ALTURA/1.7, BASE/2, ALTURA/1.55, fill="black")

# Ejes de las ruedas
c.create_oval(BASE/7.5, ALTURA/1.68, BASE/6.2, ALTURA/1.58, fill="gray")
c.create_oval(BASE/3.9, ALTURA/1.68, BASE/3.1, ALTURA/1.58, fill="gray")
c.create_oval(BASE/2.45, ALTURA/1.68, BASE/2.05, ALTURA/1.58, fill="gray")

# Barra que conecta las ruedas
c.create_rectangle(BASE/8, ALTURA/1.65, BASE/2, ALTURA/1.63, fill="red")

# -----------------------------
# Ventana en la cabina
# -----------------------------
c.create_rectangle(BASE/1.9, ALTURA/2.6, BASE/1.5, ALTURA/2, fill="white", outline="black")
c.create_line(BASE/1.7, ALTURA/2.6, BASE/1.7, ALTURA/2, fill="black")  # división ventana

# -----------------------------
# Humo de la chimenea
# -----------------------------
c.create_oval(BASE/6, ALTURA/3.5, BASE/5, ALTURA/3, fill="lightgray")
c.create_oval(BASE/5.5, ALTURA/4, BASE/4.8, ALTURA/3.3, fill="lightgray")
c.create_oval(BASE/5, ALTURA/5, BASE/4.5, ALTURA/4, fill="lightgray")

# -----------------------------
# Texto en el cuerpo del tren
# -----------------------------
c.create_text(BASE/3, ALTURA/1.9, text="HAROLD", font=("Arial", 28, "bold"), fill="white")

ventana.mainloop()
