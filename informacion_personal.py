# 1. Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Diana Menéndez",
    "edad": 44,
    "ciudad": "Santo Domingo",
    "profesion": "Chef de partida"
}

# 2. Acceder y modificar valores
# Cambiar la ciudad
informacion_personal["ciudad"] = "El Carmen Manabí"

# 3. Agregar nueva clave-valor (en este caso, "profesion" ya existe, así que se actualizaría)
# Para agregar una clave diferente, por ejemplo "hobbies":
informacion_personal["hobbies"] = ["bailar", "hacer ejercicios", "viajar"]

# 4. Verificar existencia de clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+0990504129"

# 5. Eliminar la clave "edad"
informacion_personal.pop("edad", None)  # Usamos .pop() para evitar errores si la clave no existe

 6. Imprimir el diccionario final
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")