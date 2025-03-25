# Creación del diccionario con información personal
informacion_personal = {
    "nombre": "Diana Menéndez",
    "edad": 44,
    "ciudad": "Santo Domimgo",
    "profesion": "Chef de partida"
}

# 1. Modificar la ciudad
informacion_personal["ciudad"] = "Quito"  # Cambiamos de Guadalajara a Monterrey

# 2. Agregar una nueva clave-valor (en este caso "profesion" ya existe)
# Vamos a agregar otra información relevante como "estado_civil"
informacion_personal["estado_civil"] = "Casada"

# 3. Verificar y agregar teléfono si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0990504129"

# 4. Eliminar la clave "edad"
del informacion_personal["edad"]  # Eliminamos la edad

# Mostramos el diccionario final
print("Información Personal Actualizada:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")