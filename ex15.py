"""# Apertura file modo tradizionale
fn = "DatiPersonali.txt"
f = open(fn,"r")
while True:
    linea = f.readline()
    if not linea:
        break
    num_find = linea.find(": ")
    dato_persona = linea[num_find+2:]
    print(dato_persona)
f.close()

# Apertura file modo tradizionale versione Riccardo
fn = "DatiPersonali.txt"
f = open(fn,"r")
while (linea := f.readline()):
    if not linea:
        break
    num_find = linea.find(": ")
    dato_persona = linea[num_find+2:]
    print(dato_persona)
f.close()

# Apertura file modo Python 1 versioni
fn = "DatiPersonali.txt"
f = open(fn,"r")
for line in f:
    dato_persona = line.split(": ")[1]
    print(dato_persona)
f.close()

"""

# Apertura file modo Python Python
fn = "DatiPersonali.txt"
# Uso il context manager 
# linea 27 e 31 si fondono 
# in una istruzione facciamo l3 righe 28 29 30 
# metodo rstrip toglie "\n" 
with open(fn,"r") as f:
    risultato = [line.rstrip().split(": ")[1] for line in f]
print(f"Sono {risultato[0]} {risultato[1]}, ho {risultato[2]} e sono alto {risultato[3]} cm")
