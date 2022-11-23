fn_input = "DatiPersonali.txt"
fn_output = "Risultato.txt"
with open(fn_input,"r") as f:
    risultato = [line.rstrip().split(": ")[1] for line in f]
with open(fn_output,"w") as f:    
    f.write(f"Sono {risultato[0]} {risultato[1]}, ho {risultato[2]} e sono alto {risultato[3]} cm")