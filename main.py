import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# ======================
# 1. Datos base
# ======================
horas = list(range(24))
demanda = [50,45,40,42,55,70,90,120,140,160,180,190,200,210,220,200,180,150,140,130,110,90,70,60]

capacidad = 25  # solicitudes por servidor
costo_por_servidor = 1  # costo por hora
umbral = 0.7  # 70%

# ======================
# 2. Políticas de escalado
# ======================

# Escalado fijo (10 servidores siempre)
fijo = [10]*24

# Escalado reactivo (ajusta exacto a la demanda)
reactivo = [math.ceil(d/capacidad) for d in demanda]

# Escalado con margen (usa umbral +1 servidor si supera 70%)
margen = []
for d in demanda:
    servidores_necesarios = math.ceil(d/capacidad)
    if d/servidores_necesarios > capacidad*umbral:
        servidores_necesarios += 1
    margen.append(servidores_necesarios)

# ======================
# 3. Crear DataFrame con resultados
# ======================
df = pd.DataFrame({
    "Hora": horas,
    "Demanda (sol/seg)": demanda,
    "Escalado Fijo": fijo,
    "Escalado con Margen": margen,
    "Escalado Reactivo": reactivo
})

# Calcular costos
df["Costo Fijo"] = df["Escalado Fijo"] * costo_por_servidor
df["Costo Margen"] = df["Escalado con Margen"] * costo_por_servidor
df["Costo Reactivo"] = df["Escalado Reactivo"] * costo_por_servidor

# ======================
# 4. Resultados finales
# ======================
costo_total_fijo = df["Costo Fijo"].sum()
costo_total_margen = df["Costo Margen"].sum()
costo_total_reactivo = df["Costo Reactivo"].sum()

print("Costo total Escalado Fijo:", costo_total_fijo)
print("Costo total Escalado con Margen:", costo_total_margen)
print("Costo total Escalado Reactivo:", costo_total_reactivo)

# ======================
# 5. Graficar resultados
# ======================

# Demanda vs servidores (ejemplo gráfico)
plt.figure(figsize=(12,6))
plt.plot(df["Hora"], df["Demanda (sol/seg)"], label="Demanda (sol/seg)", linewidth=2, color="black")
plt.plot(df["Hora"], df["Escalado Fijo"], label="Servidores Fijo", linestyle="--")
plt.plot(df["Hora"], df["Escalado con Margen"], label="Servidores con Margen", linestyle="-.")
plt.plot(df["Hora"], df["Escalado Reactivo"], label="Servidores Reactivo", linestyle=":")
plt.xlabel("Hora del día")
plt.ylabel("Demanda / Servidores")
plt.title("Simulación de Escalado de Servidores")
plt.legend()
plt.grid(True)
plt.show()

# Costos acumulados
plt.figure(figsize=(10,5))
plt.plot(df["Hora"], df["Costo Fijo"].cumsum(), label="Fijo")
plt.plot(df["Hora"], df["Costo Margen"].cumsum(), label="Margen")
plt.plot(df["Hora"], df["Costo Reactivo"].cumsum(), label="Reactivo")
plt.xlabel("Hora del día")
plt.ylabel("Costo acumulado")
plt.title("Costo acumulado por política de escalado")
plt.legend()
plt.grid(True)
plt.show()

# ======================
# 6. Mostrar tabla final
# ======================
print("\n=== TABLA DE RESULTADOS ===")
print(df)

