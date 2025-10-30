# Laboratorio 4 – Cifrado Simétrico (DES, 3DES y AES-256)

**Autor:** Felipe Cuevas  
**Fecha:** Octubre 2025  
**Correo:** felipe.cuevas1@mail.udp.cl  

---

##  Descripción del laboratorio

Este laboratorio tiene como objetivo implementar y analizar los algoritmos de **cifrado simétrico** DES, 3DES y AES-256, utilizando el modo **CBC (Cipher Block Chaining)**.  
Se trabajó en Python empleando la librería **PyCryptodome** para realizar los procesos de cifrado y descifrado, además de validar y ajustar las claves según los requisitos de cada algoritmo.

Durante el desarrollo, se utilizó un **entorno virtual (venv)** en Linux, ya que el sistema operativo puede presentar restricciones al instalar librerías criptográficas directamente.  
Esto permitió aislar el entorno del sistema y evitar posibles conflictos o errores al usar **PyCryptodome**.

---

##  Contenido del repositorio

```
├── cifrados.py          # Código con implementación de DES, 3DES y AES-256
└── README.md             # Este archivo
```

---

##  Requisitos

- Python 3.8 o superior  
- Librería PyCryptodome  
- Entorno virtual (opcional pero recomendado en Linux)

### Instalación de dependencias

```bash
# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar librería necesaria
pip install pycryptodome
```

---

##  Uso del programa

Ejecutar el script principal desde la terminal:

```bash
python3 cifrados.py
```

### Flujo del programa

1. Seleccionar el algoritmo:
   - `1` → DES  
   - `2` → AES-256  
   - `3` → 3DES  

2. Seleccionar la operación:
   - `1` → Cifrar  
   - `2` → Descifrar  

3. Ingresar los valores solicitados:
   - Clave (Key)  
   - Vector de inicialización (IV)  
   - Texto plano o cifrado (según corresponda)

---

##  Ejemplo de uso

**Cifrado con AES-256 (modo CBC):**

```
Clave: G7d9Kf2LmNpQ8rXsT4vB1yHjUeW3cV0a
IV (16 bytes): Xy7!rT4vB1yHjUeW
Texto plano: felipe

CIFRADO (hex): 6E9D5FE4357F9B35C93074017076B0DD
```

**Descifrado correspondiente:**

```
Clave: G7d9Kf2LmNpQ8rXsT4vB1yHjUeW3cV0a
IV (16 bytes): Xy7!rT4vB1yHjUeW
Texto cifrado (hex): 6E9D5FE4357F9B35C93074017076B0DD

TEXTO PLANO: felipe
```

---

##  Comparación con herramientas online

Para validar los resultados obtenidos con el código, se compararon los cifrados con los generados por las siguientes herramientas:

- **DES:** [https://www.devglan.com/online-tools/triple-des-encrypt-decrypt](https://www.devglan.com/online-tools/triple-des-encrypt-decrypt)  
- **AES-256:** [https://www.devglan.com/online-tools/aes-encryption-decryption](https://www.devglan.com/online-tools/aes-encryption-decryption)  
- **3DES:** [https://anycript.com/crypto/des](https://anycript.com/crypto/des)

---

##  Conclusión

Los algoritmos de **cifrado simétrico** son esenciales para mantener la **confidencialidad** de la información en entornos digitales.  
A través de este laboratorio se comprobó que:

- DES es inseguro debido a su tamaño de clave reducido.  
- 3DES mejora la seguridad pero resulta menos eficiente.  
- AES-256 se mantiene como el estándar más robusto y confiable.  

Además, se verificó que el uso de **entornos virtuales** facilita la instalación de librerías de seguridad sin comprometer la estabilidad del sistema operativo.

---

**Felipe Cuevas – Ingeniería Civil en Informática y Telecomunicaciones – Universidad Diego Portales**
