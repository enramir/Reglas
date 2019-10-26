# Inteligencia Artificial.
# Grado en Ingeniería Informática - Tecnologías Informáticas
# lentes.py



atributos=[("Edad",['Joven','Prepresbicia','Presbicia']),
           ("Diagnóstico",['Miope','Hipermétrope']),
           ("Astigmatismo",['+','-']),
           ("Lagrima",['Reducida','Normal'])]

atributo_clasificación='Lente'
clases=['Ninguna','Blanda','Rígida']



entr=[["Joven","Miope","-","Reducida","Ninguna"],
      ["Joven","Miope","-","Normal","Blanda"], 
      ["Joven","Miope", "+","Reducida","Ninguna"],
      ["Joven","Miope","+","Normal","Rígida"], #borrar fila 4
      ["Joven","Hipermétrope","-","Reducida","Ninguna"],
      ["Joven","Hipermétrope","-","Normal","Blanda"], 
      ["Joven", "Hipermétrope","+","Reducida","Ninguna"],
      ["Joven", "Hipermétrope","+","Normal","Rígida"],#todavía por coger 
      ["Prepresbicia","Miope","-","Reducida","Ninguna"],
      ["Prepresbicia","Miope","-","Normal","Blanda" ],
      ["Prepresbicia","Miope","+","Reducida","Ninguna"],
      ["Prepresbicia","Miope","+","Normal","Rígida"], #borrar fila 12
      ["Prepresbicia","Hipermétrope","-","Reducida","Ninguna"],
      ["Prepresbicia","Hipermétrope","-","Normal","Blanda"],
      ["Prepresbicia","Hipermétrope","+","Reducida","Ninguna"],
      ["Prepresbicia","Hipermétrope","+","Normal","Ninguna"],
      ["Presbicia","Miope","-","Reducida","Ninguna"],
      ["Presbicia","Miope","-","Normal","Ninguna"],
      ["Presbicia","Miope","+","Reducida","Ninguna"],
      ["Presbicia","Miope","+","Normal","Rígida"],#borrar fila 20
      ["Presbicia","Hipermétrope","-", "Reducida","Ninguna"],
      ["Presbicia","Hipermétrope","-","Normal","Blanda"], 
      ["Presbicia","Hipermétrope","+","Reducida","Ninguna"],
      ["Presbicia","Hipermétrope","+","Normal","Ninguna"]]


