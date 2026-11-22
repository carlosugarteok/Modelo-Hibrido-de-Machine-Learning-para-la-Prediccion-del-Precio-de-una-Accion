# Guía de instalación en Windows y VS Code

## Requisitos
Python **3.11 de 64 bits**, VS Code con extensiones Python y Jupyter. Trabajá desde la raíz del repositorio (donde está `requirements-lstm.txt`).

## Crear un entorno virtual local
En PowerShell, dentro del proyecto:

```powershell
py -3.11 -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements-lstm.txt
& ".\.venv\Scripts\python.exe" -m ipykernel install --user --name hybrid-ml --display-name "Python 3.11 - Hybrid ML"
```

**No es necesario activar el entorno.** Esto evita los bloqueos de scripts de PowerShell.

Si preferís activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

La excepción de seguridad dura solo esa sesión.

## Seleccionar kernel
En VS Code: abrí el notebook → **Select Kernel** → **Python 3.11 - Hybrid ML**. Reiniciá el kernel y ejecutá:

```python
import sys
import pandas
import tensorflow as tf
print(sys.executable, pandas.__version__, tf.__version__)
```

La ruta del intérprete debe terminar en `.venv\Scripts\python.exe`.

## Verificar dependencias
Desde PowerShell, en la raíz del proyecto:

```powershell
& ".\.venv\Scripts\python.exe" -c "import numpy,pandas,matplotlib,sklearn,tensorflow; print('ENTORNO CORRECTO')"
& ".\.venv\Scripts\python.exe" -m unittest discover -s tests -v
```

## Solución de errores
- **`No module named pandas`**: Jupyter y PowerShell están usando diferentes intérpretes. Compará `sys.executable` dentro del notebook con `python -c "import sys; print(sys.executable)"` en PowerShell. Instalá con la ruta explícita de `.venv\Scripts\python.exe` como arriba. También podés usar `%pip install pandas` dentro del notebook.
- **`DLL load failed ... _pywrap_tensorflow_internal`**: TensorFlow puede estar instalado pero falla la carga de componentes nativos. Verificá el import desde `.venv\Scripts\python.exe`; si falla, comprobá Microsoft Visual C++ Redistributable x64, la arquitectura de 64 bits y reinstalá en un entorno limpio.
- **`Activate.ps1` bloqueado**: utilizá la ruta directa del Python del entorno sin activarlo, o `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
- **`FileNotFoundError` del CSV**: abrí VS Code desde la raíz del proyecto y comprobá `data/precios_historicos_normalizados.csv`.
- **Avisos oneDNN**: son mensajes informativos, no fallos.

## Ejecución
Con `USAR_LSTM=True` se entrena el híbrido completo; con `USAR_LSTM=False` solo se ejecutan regresión y persistencia. Ejecutá **Restart Kernel and Run All Cells**. No publiques métricas LSTM sin ejecutar el entrenamiento.
