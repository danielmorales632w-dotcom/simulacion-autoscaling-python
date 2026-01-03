Markdown

# Simulación de Auto-Scaling de Servidores

Este proyecto es una simulación en Python que compara diferentes estrategias de escalado de infraestructura para un entorno de alta demanda.

## ¿Qué hace?
El script analiza un patrón de demanda de 24 horas y calcula cuántos servidores se necesitan bajo tres políticas distintas, permitiendo visualizar costos y eficiencia:

1.  **Escalado Fijo:** Mantiene una cantidad estática de servidores (Sobrecosto en horas valle, riesgo en horas pico).
2.  **Escalado Reactivo:** Ajusta los servidores exactamente a la demanda del momento.
3.  **Escalado con Margen:** Agrega servidores extra preventivamente cuando la carga supera el 70% (Simulando un enfoque de alta disponibilidad).

## Tecnologías
* **Python 3**
* **Pandas & NumPy:** Procesamiento de datos.
* **Matplotlib:** Visualización de métricas y gráficos de costos.

## Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone 
Instalar dependencias:

Bash

pip install -r requirements.txt
Ejecutar la simulación:

Bash

python simulacion_autoscaling.py
 Resultados Visuales
El script genera gráficas comparativas de:

Demanda de tráfico vs. Servidores activos.

Costo acumulado por estrategia.

