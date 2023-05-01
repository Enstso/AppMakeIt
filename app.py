from tkinter import  *
import webbrowser

def portfolio():
 
 return webbrowser.open_new("https://gitlab.com/portfolio-2023-janvier-enstso")

def createTitle(titleEntry,window):
  with open("README.md","w+") as file:
    titleEntry = '# '+titleEntry
    file.write(titleEntry)
    file.close()
  window.destroy()
def title():
   windowTitle = Tk()
   windowTitle.title('Makeit')
   windowTitle.minsize(899,599)
   windowTitle.maxsize(901,601)
   windowTitle.iconbitmap("assets/logo.ico")
   windowTitle.config(background='white')
   frame = Frame(windowTitle,bg="white")
   lbl_title = Label(windowTitle,text="Makeit",font=("Terminal",30),bg="white",fg="#018AED")
   lbl_title.pack(pady=50)
   lbl_titre = Label(frame,text="Titre du READ ME",font=("Open sans",25), bg="white")
   lbl_titre.pack()
   titleEntry = Entry(windowTitle,font=("Open sans",20), bg="grey")
   titleEntry.place(x=300,y=350)
   btnvalid = Button(windowTitle,text="Valider",bg="black", font=("Open sans",15), fg="white",height=2, width=10, command= lambda : createTitle(titleEntry.get(),windowTitle))
   btnvalid.place(x=380,y=480)
   btnPortfolio = Button(windowTitle,text="Mon portfolio", command=portfolio, font=("Open sans",12), bg="grey", fg="white", height=2,width=10)
   btnPortfolio.place(x=800,y=550)
   frame.pack()
   return windowTitle



# Creer une fenêtre Tkinter

window = Tk()

#personnaliser la fenêtre

window.title("Makeit")
window.geometry("900x600")
window.minsize(899,599)
window.maxsize(901,601)
window.iconbitmap("assets/logo.ico")
window.config(background='white')

# creer la frame
frame = Frame(window,bg="white")

#Labels
lbl_title = Label(window,text="Makeit",font=("Terminal",30),bg="white",fg="#018AED")
lbl_title.pack(pady=50)

lbl_titre = Label(frame,text="Vos choix",font=("Open sans",25), bg="white")
lbl_titre.pack()

# Boutons
btnTitle = Button(frame,text="Mettre un titre",bg="black",font=("Open sans",15), fg="white",height=5, width=50, command=title)
btnTitle.pack(pady=25)

btnSection = Button(frame,text="Créer une section",bg="black",font=("Open sans",15),fg="white",height=5, width=50)
btnSection.pack(pady=25,fill=X)

btnPortfolio = Button(window,text="Mon portfolio", command=portfolio, font=("Open sans",12), bg="grey", fg="white", height=2,width=10)
btnPortfolio.place(x=800,y=550)
#btnPortfolio.pack()
# afficher

frame.pack(expand=YES)
window.mainloop()