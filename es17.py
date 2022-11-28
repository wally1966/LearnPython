# Versione senza usare il content manager"
""" 
fn_input = "FiledaCopiare.txt"
fn_output = "FileRisultato.txt"
f = open(fn_input,"r") 
g = open(fn_output,"w") 
for line in f:
    g.write(line)
f.close()
g.close()    
"""
# Versione usando il context manager 

fn_input = "FiledaCopiare.txt"
fn_output = "FileRisultato.txt"

with open(fn_input,"r") as f, open(fn_output,"w") as g:
# f.read() leggo in un colpo solo tutto il contenuto del file f 
# g.write() scrivo in un colpo solo tutto il contenuto del file f 
    g.write(f.read())
