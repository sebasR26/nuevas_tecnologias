import pandas as pd

deporte = {"Terrestres": ["Artes marciales", "Rugby", "Atletismo"],
           "Acuatico": ["waterpolo", "Nado sincronizados", "Buceo"],
           "Aereo": ["bungee", "Paracaidismo", "Gimnasia aerea"]}

matiz = pd.DataFrame(deporte)
print(matiz)

