from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#   AJUSTAR CLAVE

def ajustar_clave(clave_bytes, required_len, use_random_padding=True):
    if len(clave_bytes) < required_len:
        faltan = required_len - len(clave_bytes)
        if use_random_padding:
            relleno = get_random_bytes(faltan)
            print(f"PAD: se añadieron {faltan} bytes aleatorios.")
        else:
            relleno = b'\x00' * faltan
            print(f"PAD: se añadieron {faltan} bytes de ceros.")
        clave_final = clave_bytes + relleno
    elif len(clave_bytes) > required_len:
        clave_final = clave_bytes[:required_len]
        print(f"TRUNC: la clave original ({len(clave_bytes)} bytes) fue truncada a {required_len} bytes.")
    else:
        clave_final = clave_bytes
        print("OK: la clave tiene la longitud requerida.")
    print("Clave final (hex):", clave_final.hex().upper())
    return clave_final

# Utility: limpiar hex input
def limpiar_hex(s):
    s = s.strip()
    if s.startswith("0x") or s.startswith("0X"):
        s = s[2:]
    return "".join(s.split())  # quita espacios y saltos

#   AES CBC

def aes_cifrar():
    print("\n=== CIFRAR: AES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 32, False)
    iv = ajustar_clave(input("IV (16 bytes): ").encode(), 16, False)
    texto = input("Texto plano: ").encode()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    cifrado = cipher.encrypt(pad(texto, AES.block_size))
    print("\nCIFRADO (hex):", cifrado.hex().upper())

def aes_descifrar():
    print("\n=== DESCIFRAR: AES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 32, False)
    iv = ajustar_clave(input("IV (16 bytes): ").encode(), 16, False)

    cifrado_hex = limpiar_hex(input("Texto cifrado (hex): "))
    try:
        cifrado = bytes.fromhex(cifrado_hex)
    except ValueError:
        print("Error: el texto cifrado no es un hex válido.")
        return

    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        descifrado = unpad(cipher.decrypt(cifrado), AES.block_size)
    except (ValueError, KeyError):
        print("Error: descifrado fallido (clave/IV/ciphertext incorrectos o padding inválido).")
        return

    try:
        print("\nTEXTO PLANO:", descifrado.decode())
    except UnicodeDecodeError:
        print("\nTEXTO PLANO (bytes):", descifrado)

#   DES CBC

def des_cifrar():
    print("\n=== CIFRAR: DES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 8, False)
    iv = ajustar_clave(input("IV (8 bytes): ").encode(), 8, False)
    texto = input("Texto plano: ").encode()

    cipher = DES.new(key, DES.MODE_CBC, iv)
    cifrado = cipher.encrypt(pad(texto, DES.block_size))
    print("\nCIFRADO (hex):", cifrado.hex().upper())

def des_descifrar():
    print("\n=== DESCIFRAR: DES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 8, False)
    iv = ajustar_clave(input("IV (8 bytes): ").encode(), 8, False)

    cifrado_hex = limpiar_hex(input("Texto cifrado (hex): "))
    try:
        cifrado = bytes.fromhex(cifrado_hex)
    except ValueError:
        print("Error: el texto cifrado no es un hex válido.")
        return

    cipher = DES.new(key, DES.MODE_CBC, iv)
    try:
        descifrado = unpad(cipher.decrypt(cifrado), DES.block_size)
    except (ValueError, KeyError):
        print("Error: descifrado fallido (clave/IV/ciphertext incorrectos o padding inválido).")
        return

    try:
        print("\nTEXTO PLANO:", descifrado.decode())
    except UnicodeDecodeError:
        print("\nTEXTO PLANO (bytes):", descifrado)

#   3DES CBC

def des3_cifrar():
    print("\n=== CIFRAR: 3DES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 24, False)
    # Ajustar paridad de claves para 3DES
    try:
        key = DES3.adjust_key_parity(key)
    except ValueError:
        print("Error: la clave 3DES no es válida tras ajustar paridad.")
        return
    iv = ajustar_clave(input("IV (8 bytes): ").encode(), 8, False)
    texto = input("Texto plano: ").encode()

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    cifrado = cipher.encrypt(pad(texto, DES3.block_size))
    print("\nCIFRADO (hex):", cifrado.hex().upper())

def des3_descifrar():
    print("\n=== DESCIFRAR: 3DES CBC ===")
    key = ajustar_clave(input("Clave: ").encode(), 24, False)
    try:
        key = DES3.adjust_key_parity(key)
    except ValueError:
        print("Error: la clave 3DES no es válida tras ajustar paridad.")
        return
    iv = ajustar_clave(input("IV (8 bytes): ").encode(), 8, False)

    cifrado_hex = limpiar_hex(input("Texto cifrado (hex): "))
    try:
        cifrado = bytes.fromhex(cifrado_hex)
    except ValueError:
        print("Error: el texto cifrado no es un hex válido.")
        return

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    try:
        descifrado = unpad(cipher.decrypt(cifrado), DES3.block_size)
    except (ValueError, KeyError):
        print("Error: descifrado fallido (clave/IV/ciphertext incorrectos o padding inválido).")
        return

    try:
        print("\nTEXTO PLANO:", descifrado.decode())
    except UnicodeDecodeError:
        print("\nTEXTO PLANO (bytes):", descifrado)

#   MENÚ PRINCIPAL

if __name__ == "__main__":

    print("Seleccione el algoritmo:")
    print("1 - DES")
    print("2 - AES-256")
    print("3 - 3DES")
    alg = input("Opción: ")

    print("\n¿Desea cifrar o descifrar?")
    print("1 - Cifrar")
    print("2 - Descifrar")
    op = input("Opción: ")

    if alg == "1" and op == "1": des_cifrar()
    elif alg == "1" and op == "2": des_descifrar()
    elif alg == "2" and op == "1": aes_cifrar()
    elif alg == "2" and op == "2": aes_descifrar()
    elif alg == "3" and op == "1": des3_cifrar()
    elif alg == "3" and op == "2": des3_descifrar()
    else: print("Opción inválida")
