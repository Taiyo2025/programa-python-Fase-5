articulos = [
    ["A01", "Teclado",    5,  10],
    ["A02", "Mouse",      12, 10],
    ["A03", "Monitor",    3,  8],
    ["A04", "USB",        20, 15],
    ["A05", "Audifonos",  2,  7]
]

# Si el stock está por debajo del mínimo, calcula cuánto hay que pedir
def unidades_a_pedir(stock, minimo):
    if stock < minimo:
        return minimo - stock
    return 0

print("=== Lista de pedidos ===\n")

for codigo, nombre, stock, minimo in articulos:
    pedido = unidades_a_pedir(stock, minimo)
    print(f"Artículo: {nombre}")
    print(f"  Stock actual: {stock} | Mínimo: {minimo}")
    print(f"  Unidades a pedir: {pedido}\n")