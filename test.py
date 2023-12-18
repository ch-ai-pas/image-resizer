import PIL as pil
import ttkbootstrap as ttkbs
from tkinter import filedialog

class App:
    def __init__(self):
        def open_img(self):
            self.filename = filedialog.askopenfilename(title="Ouvrir l'image",filetypes=(("png","*.png"),("jpeg","*.jpeg"),("jpg","*.jpg"),("all files","*.*"))) 
            print(self.filename)
            
            self.fenetre.title(self.debut_nom_fenetre + "- " + self.filename)
            
        def resizeimg(self):
            # Ouvrir l'image avec PIL
            self.image = pil.Image.open(self.filename)

            # Définir la largeur souhaitée
            self.largeur = int(self.entry.get())
            print(self.largeur)

            # Calculer la hauteur correspondante tout en conservant le rapport d'aspect
            self.hauteur = int((float(self.image.size[1]) * float(self.largeur / float(self.image.size[0]))))
            print("hauteur image " + str(self.hauteur))

            # Redimensionner l'image tout en conservant le rapport d'aspect
            self.new_imagedos = self.image.resize((self.largeur, self.hauteur))
            
            self.new_imagedos.save(self.filename)
        
        self.fenetre = ttkbs.Window(themename="superhero")
        
        self.debut_nom_fenetre = "Redimensionne Image "
        
        self.fenetre.title(self.debut_nom_fenetre)
        
        self.frame1 = ttkbs.Frame(self.fenetre)
        self.frame1.grid(row=0, column=1, padx=2, pady=2, sticky=ttkbs.NSEW)
        
        self.btn_open = ttkbs.Button(self.frame1, text="Ouvrir l'image :", command=lambda:open_img(self))
        self.btn_open.grid(row=0, column=1, padx=5, pady=5, sticky=ttkbs.EW)
        
        self.frame2 = ttkbs.LabelFrame(self.frame1, text="Largeur (en pixels) :")
        self.frame2.grid(row=1, column=1, padx=5, pady=2, sticky=ttkbs.EW)
        
        self.entry = ttkbs.Entry(self.frame2)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky=ttkbs.EW)
        
        self.resizebtn = ttkbs.Button(self.frame1, text="Redimensionner et enregistrer l'image :", command=lambda:resizeimg(self))
        self.resizebtn.grid(row=2, column=1, padx=5, pady=5, sticky=ttkbs.EW)
        
        self.fenetre.mainloop()
        
app = App()