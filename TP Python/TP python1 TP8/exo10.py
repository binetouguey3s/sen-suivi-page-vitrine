global_data = "donnees"
def modifier_global():
    global global_data
    global_data = "nouvelles_donnees"

print("Avant modification:", global_data)
modifier_global()
print("Après modification:", global_data)

