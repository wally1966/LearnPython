from sys import argv
def somma(a,b):
    c=int(a)+int(b)
    return c

def sottrazione(a,b):
    c=int(a)-int(b)
    return c

def moltiplicazione(a,b):
    c=int(a)*int(b)
    return c

def divisione(a,b):
    c=int(a)/int(b)
    return c 

a = argv[1]
b = argv[2]
segno_operazione = argv[3]
if segno_operazione == '+':
    c=somma(a,b)
elif segno_operazione == '-':  
    c=sottrazione(a,b)
elif segno_operazione == '*':
    c=moltiplicazione(a,b)
elif segno_operazione == '/':
    c=divisione(a,b)

fn_output = "FileRisultato_2.txt"
with open(fn_output,"a") as f: 
    f.write(f"Il risultato della operazione di {a} {segno_operazione} {b} è {c}\n")

