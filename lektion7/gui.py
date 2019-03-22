from tkinter import *
from tkinter import messagebox
from biblioteket import Materiale, Bog, Film

# TODO - du skal have initialiseret nogle bog objekter og nogle film
# objekter og sat ind i listen - Lav minium 3 af hver type -
# og husk at give dem alle et forskelligt ID - som skal bruges til
# at udlåne det.

m = Materiale(0, "Das Kapital", 3, 0, 2015)
bog1 = Bog(1, "Das Kapital", 8, 0, 1989, 697, "Karl Marx")
bog2 = Bog(2, "Outlander", 10, 0, 2015, 749, "Diana Gabaldon")
bog3 = Bog(3, "Fra krig og fred", 28, 0, 1865, 560, "Lev Tolstojs")
bog4 = Bog(7, "Den, der lever stille", 28, 0, 2018, 374, "Leonora Christina Skov")

film1 = Film(4, "The Godfather", 15, 0, 1972, " Francis Ford Coppola", 178)
film2 = Film(5, "Lady Bird", 7, 0, 2017, "Greta Gerwig", 93)
film3 = Film(6, "CASABLANCA", 10, 0, 1942, "Michael Curtiz", 102)
film4 = Film(7, "Moonlight", 10, 0, 2017, "Barry Jenkins", 110)

listMaterialer = [bog1, bog2, bog3, bog4,film1, film2, film3]

class Application(Frame):

    def udlaan(self):

        # TODO - her skal du have udlånt det korrekte materiale.
        # med det korrekte id og opdater objektet.
        # print("id der skal lånes: " + idnr)

        idnr = self.id_entry.get()
        found = False
        kan_udlaane = True

        if len(idnr) == 0:
            messagebox.showwarning("Warning", "Indtast Idnr!")
        else:
            udlaanId = [bog1.idnr, bog2.idnr, bog3.idnr, bog4.idnr, film1.idnr, film2.idnr, film3.idnr]

            for laanid in udlaanId:
                if laanid == int(idnr):
                    self.listGui.delete('1.0', END)
                    list_index = udlaanId.index(laanid)

                    listMaterialer[list_index].antaludlaan = m.udlaan(1)
                    kan_udlaane = m.kan_udlaane(listMaterialer[list_index].antal,
                                                listMaterialer[list_index].antaludlaan)
                    self.listGui.insert(END, listMaterialer[list_index].tostring())
                    found = True

                if not kan_udlaane:
                    messagebox.showwarning("Warning", "Det er ikke flere tilbage, alle er udlånt!")
                    break
            if not found:
                messagebox.showwarning("Warning", "findes ikke!!!")

    def aflever(self):
        idnr = self.aflever_entry.get()
        # print("id der skal afleveres: " + idnr)
        # TODO - her skal du have afleveret det korrekte materiale
        # med det korrekte id og så opdater det objekt.
        found = False
        if len(idnr) == 0:
            messagebox.showwarning("Warning", "Input felten er tom!!!!")
        else:
            afleverId = [bog1.idnr, bog2.idnr, bog3.idnr, film1.idnr, film2.idnr, film3.idnr]

            for laanid in afleverId:
                if laanid == int(idnr):
                    self.listGui.delete('1.0', END)
                    list_index = afleverId.index(laanid)
                    found = True
                    if listMaterialer[list_index].antaludlaan > 0:
                        listMaterialer[list_index].antaludlaan = m.udlaan(-1)
                        self.listGui.insert(END, listMaterialer[list_index].tostring())
                    else:
                        messagebox.showwarning("Warning", "Du har aflevet!")
                        self.listGui.insert(END, listMaterialer[list_index].tostring())

            if not found:
                messagebox.showwarning("Warning", "Den idnr findes ikke, prøve igen!!!")

    def sog_i_listen(self):
        search_text = (self.entry.get()).lower()
        # print("søge tekst: " + search_text)
        # TODO Nu skal listen af materiale søges igennem og
        # de materialer som matcher (dvs. hvor søgestrengen indgår som
        # en delstring) skal nu vises i listen og altså IKKE alle
        # materialer. Så du kan få brug for at slette det som
        # allerede står i vinduet og så tilføje de materialer
        # som matcher.
        found = False
        if len(search_text) == 0:
            messagebox.showwarning("Warning", "Input felten er tom!!!!")
        else:
            listsearch = [bog1.tostring(), bog2.tostring(), bog3.tostring(),
                          film1.tostring(), film2.tostring(), film3.tostring()]

            self.listGui.delete('1.0', END)
            for materiale in listsearch:
                if search_text in materiale.lower():
                    #self.L1(END, text="Hej, velkommen til mit program\n\n\n")
                    self.listGui.insert(INSERT, materiale + "\n")
                    found = True
            if not found:
                messagebox.showwarning("Warning", "Den idnr findes ikke, prøve igen!!!")

    def vis_hele_listen(self):
        # print("Vis hele listen")
        # linjen nedenunder sletter hele listen i GUI'en
        # Den være være nyttig andre steder.....
        #    self.listGui.delete('1.0', END)
        # TODO - nu skal du vise HELE listen af materialer igen
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.tostring() + "\n")

    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng", padx=10)
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=2)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen", padx=10, pady=5)
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån", padx=10)
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=2)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån", padx=10, pady=5)
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:", padx=10)
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=2)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever", padx=10, pady=5)
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame, text="Vis hele listen", padx=10, pady=5)
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT", padx=10, pady=5)
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # Her definerer vi en Text widget - dvs
        # den kan indeholde multiple linjer
        # ideen er så at hver linje indeholde et styk materiale
        # Nedenunder kan du se hvordan listen af materiale løbes
        # igennem og toString metoden bliver kaldt og så bliver
        # der indsat en ny linje i Text widgeten
        self.listGui = Text(self, width=160)

        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.tostring() + "\n")
        frame.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master, pady=10, padx=10)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
