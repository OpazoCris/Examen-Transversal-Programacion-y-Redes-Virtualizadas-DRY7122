#ET C.opazo Fel.sobarzo
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def calcular_tiempo(distancia_km, transporte):
    velocidades = {
        "auto": 80,         # km/h
        "bicicleta": 15,
        "caminando": 5,
        "vuelo": 800
    }
    velocidad = velocidades.get(transporte, 80)
    horas = distancia_km / velocidad
    return horas

def main():
    print("=== Calculadora de distancia entre ciudades (Chile - Perú) ===")
    print("Escriba 's' en cualquier momento para salir.\n")

    geolocator = Nominatim(user_agent="geoapi")

    while True:
        origen = input("Ingrese ciudad de origen: ").strip()
        if origen.lower() == "s":
            break

        destino = input("Ingrese ciudad de destino: ").strip()
        if destino.lower() == "s":
            break

        print("Seleccione medio de transporte: auto, caminando, bicicleta, vuelo")
        transporte = input("Medio de transporte: ").strip().lower()
        if transporte == "s":
            break

        try:
            loc_origen = geolocator.geocode(origen + ", Chile")
            loc_destino = geolocator.geocode(destino + ", Perú")

            if not loc_origen or not loc_destino:
                print("No se pudo encontrar una o ambas ciudades. Intente nuevamente.\n")
                continue

            coord_origen = (loc_origen.latitude, loc_origen.longitude)
            coord_destino = (loc_destino.latitude, loc_destino.longitude)

            distancia_km = geodesic(coord_origen, coord_destino).km
            distancia_millas = distancia_km * 0.621371
            duracion_horas = calcular_tiempo(distancia_km, transporte)

            print(f"\n Desde: {origen.title()} ({coord_origen})")
            print(f" Hasta: {destino.title()} ({coord_destino})")
            print(f" Distancia: {distancia_km:.2f} km | {distancia_millas:.2f} millas")
            print(f" Duración estimada en {transporte}: {duracion_horas:.2f} horas")
            print(f" El viaje desde {origen.title()} hasta {destino.title()} cubre aproximadamente {distancia_km:.2f} km por {transporte}.\n")

        except Exception as e:
            print(f"Ocurrió un error: {e}\n")

if __name__ == "__main__":
    main()
