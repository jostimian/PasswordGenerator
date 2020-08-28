from tkinter import *
import random
root = Tk()
root.title("Password Generator V1.1")
#passwordChoices
lowerCases = "abcdefghijklmnopqrstuvwxyz"
uperCases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-="
numbers = "1234567890"
IDN_Remapped_Case_Atomic = "АӘӔБВГҐҒҔДԀЂԂҘЕЄЖҖЗԄЅӠԆИҊІЈКҚӃҠҞҜЛӅЉԈМӍНӉҢӇҤЊԊОӨПҦҀРҎСԌҪТԎҬЋУҮҰѸФХҲҺѠѾѼѺЦҴЧҶӋҸҼҾЏШЩЪЫЬҌѢЭЮЯѤѦѪѨѬѮѰѲѴҨ®©"
combine = lowerCases + uperCases + symbols + numbers + IDN_Remapped_Case_Atomic
mvar = IntVar()
mvar2 = IntVar()
iscomplex = False
#Generate Password 
def compx_savetofile():
	global iscomplex
	global saveToDevice
	if iscomplex == False:
		iscomplex = True
	if iscomplex == True:
		iscomplex = False
def genpas():
	if iscomplex == True:
		passlen = int(length.get())*2
		phase1 = "".join([random.choice(combine) for _ in range (passlen)])
		phase1_len = int(len(phase1)/2)
		generated_password = "".join([random.choice(phase1) for _ in range (phase1_len)])
		gendpass.delete(0,END)
		gendpass.insert(0, generated_password)

	else:
		passlen = int(length.get())	
		generated_password = "".join([random.choice(combine) for _ in range(passlen)] )
		gendpass.delete(0,END)
		gendpass.insert(0,generated_password)
#Tkinter Widgets
ttl = Label(text = "Password Generator V1.1")
ttl.pack()
ttl.config(font=("Calibri", 44)) 

lenlbl = Label(text = "Password length")
lenlbl.pack()
lenlbl.config(font=("Calibri",18))

length = Entry()
length.pack(ipadx=100,ipady=10)

gen = Label(text = "Generated Password")
gen.pack()
gen.config(font=("Calibri",18))

gendpass = Entry()
gendpass.pack(ipadx=100,ipady=10)

compl = Checkbutton(text = "Make It More Complex!", state = ACTIVE, variable = mvar,command = compx_savetofile)
compl.pack()

submit = Button(text = "Generate Secure Password", command = genpas)
submit.pack()

root.mainloop()