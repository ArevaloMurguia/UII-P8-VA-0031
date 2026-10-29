import numpy as np
import matplotlib.pyplot as plt
# ----Arevalo Rafael NC:0031 Fecha:29/10/26----
DiasX=["Lun","Mar","Mie","Jue","Vie"]
Califa_VA_Y=[5,6,3,8,10]
plt.bar(DiasX,Califa_VA_Y)
plt.title("Califas en VA de Arevalo Rafael NC:0031")
plt.xlabel("Dias semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()
