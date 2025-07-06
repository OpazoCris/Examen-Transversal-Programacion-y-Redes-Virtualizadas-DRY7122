#ET C.opazo Fel.sobarzo
def es_as_privado(asn):
    return (64512 <= asn <= 65534) 

def main():
    print("===== Verificador de ASN BGP =====")
    try:
        asn = int(input("Ingrese un numero de Sistema Autonomo (AS) PARA BGP: "))
        if es_as_privado(asn):
            print(f"\nEl ASN {asn} corresponde a un AS PRIVADO.")
        else:
            print(f"\nEl ASN {asn} corresponde a un AS PÚBLICO.")
    except ValueError:
        print("\nError: debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()