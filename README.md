# Modelo híbrido de Machine Learning: LSTM + Regresión Lineal

**Proyecto de Data Science** · Predicción experimental de series de precios históricos

> **Advertencia:** el dataset proporcionado cubre 2010–2020; no contiene precios vigentes ni ajustes corporativos verificados. Los resultados no constituyen asesoramiento financiero.

## Objetivo
Combinar una red LSTM (dos capas de 50 unidades) y una regresión lineal con tres rezagos para pronosticar cierres de una serie bursátil.

## Características
- **Dataset:** se utiliza un archivo adjunto por el usuario, con **2.518 registros** entre **2010-03-01 y 2020-02-28**.
- **Escalado sin fuga:** `MinMaxScaler` ajustado únicamente en entrenamiento.
- **Predicciones alineadas:** LSTM y regresión predicen exactamente las mismas fechas.
- **Partición temporal:** entrenamiento 70 %, validación 15 %, prueba 15 %.
- **Baseline:** persistencia (último precio observado).
- **Combinación:** peso 70/30 de la fuente y peso elegido **solo** en validación.
- **Pronóstico:** diez sesiones hábiles aproximadas con rezagos en el orden correcto.
- **Reproducibilidad:** tests y ejecución opcional sin TensorFlow.

## Archivos
```text
modelo-hibrido-ml/
├── Modelo_Hibrido_LSTM_Regresion_Lineal.ipynb
├── README.md
├── requirements.txt
├── requirements-lstm.txt
├── LICENSE
├── .gitignore
├── data/
│   ├── precios_historicos_normalizados.csv
│   └── FUENTE_DATOS.md
├── docs/
│   └── Documentacion_Modelo_Hibrido_ML.docx
└── tests/
    └── test_integridad.py
```

## Instalación
Python 3.11 de 64 bits recomendado. En la raíz del repositorio:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
python -m pip install -r requirements-lstm.txt
python -m pip install notebook
python -m notebook
```

Abrí `Modelo_Hibrido_LSTM_Regresion_Lineal.ipynb` y ejecutá las celdas en orden. La primera ejecución LSTM puede tardar varios minutos. Para ejecutar **sin TensorFlow**, instalá solo `requirements.txt` y cambiá `USAR_LSTM=False` en la primera celda; se ejecutarán los baselines pero no el híbrido.

## Pruebas
```bash
python -m unittest discover -s tests -v
```

## Métricas y criterio de éxito
Se reportan MAE, RMSE y MAPE sobre la **misma partición cronológica de prueba**. La mejora se determina comparando el híbrido con persistencia; no se presupone que el híbrido sea superior. El peso se elige en validación, no en prueba.

## Riesgos metodológicos
El dataset no certifica el ticker ni el proveedor, no incluye precio ajustado y podría incorporar efectos de splits/dividendos. El uso de días hábiles no equivale al calendario bursátil. El pronóstico de 10 pasos es recursivo y puede acumular error. La evaluación es una sola partición, no walk-forward. **No usar para decisiones financieras.**

## Fuente y atribución
- Datos: archivo CSV proporcionado por el usuario, normalizado en `data/`. Procedencia externa no verificada.
- Implementación propia.

## Licencia
Código propio: MIT (`LICENSE`). La licencia no transfiere derechos sobre datos de terceros ni sobre el artículo original. Revisar la autorización para redistribuir el dataset si corresponde.

## Windows y VS Code: instalación y resolución de errores

Seguí la [guía de instalación de Windows](docs/GUIA_INSTALACION_WINDOWS.md). Es esencial que Jupyter y `pip` usen **el mismo intérprete**; el notebook muestra `sys.executable`. No es necesario activar el entorno para instalar dependencias si se utiliza `.venv\\Scripts\\python.exe -m pip`.
