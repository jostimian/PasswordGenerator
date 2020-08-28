from tkinter import *
import random
root = Tk()
root.title("Password Generator V1.1")
#passwordChoices
lowerCases = "abcdefghijklmnopqrstuvwxyz"
uperCases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-="
numbers = "1234567890"
IDN_Remapped_Case_Atomic = "АӘӔБВГҐҒҔДԀЂԂҘЕЄЖҖЗԄЅӠԆИҊІЈКҚӃҠҞҜЛӅЉԈМӍНӉҢӇҤЊԊОӨПҦҀРҎСԌҪТԎҬЋУҮҰѸФХҲҺѠѾѼѺЦҴЧҶӋҸҼҾЏШЩЪЫЬҌѢЭЮЯѤѦѪѨѬѮѰѲѴҨ"
#Generate Password 
def genpas():
	passlen = int(length.get())
	combine = lowerCases + uperCases + symbols + numbers + IDN_Remapped_Case_Atomic	
	generated_password = "".join([random.choice(combine) for _ in range(passlen)] )
	gendpass.delete(0,END)
	gendpass.insert(0,generated_password)
#Tkinter Widgets
ttl = Label(text = "Password Generator V1.0")
ttl.pack()
ttl.config(font=("Calibri", 44)) 

lenlbl = Label(text = "Password length")
lenlbl.pack()
lenlbl.config(font=("Calibri",18))

length = Entry()
length.pack(ipadx=100)

gen = Label(text = "Generated Password")
gen.pack()
gen.config(font=("Calibri",18))

gendpass = Entry()
gendpass.pack(ipadx=100)

submit = Button(text = "Generate Secure Password", command = genpas)
submit.pack()

root.mainloop()