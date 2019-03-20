from tkinter import *
from tkinter import messagebox
from biblioteket import Materiale, Bog, Film

# TODO - du skal have initialiseret nogle bog objekter og nogle film
# objekter og sat ind i listen - Lav minium 3 af hver type -
# og husk at give dem alle et forskelligt ID - som skal bruges til
# at udlåne det.

m = Materiale(0, "min bog", 3, 0, 1989)
bog1 = Bog(1, "min bog", 10, 0, 1989, 560, "lars larsen")
bog2 = Bog(2, "min bog2", 8, 0, 1989, 560, "lars larsen2")
bog3 = Bog(3, "min bog3", 28, 0, 1989, 560, "lars larsen2")

film1 = Film(4, "die hard 3", 15, 0, 2007, "John wien", 90)
film2 = Film(5, "die hard 3", 7, 0, 2007, "John wien", 90)
film3 = Film(6, "die hard 3", 10, 0, 2007, "John wien", 90)

listMaterialer = [bog1, bog2, bog3, film1, film2, film3]

print(listMaterialer)


class Application(Frame):

    def udlaan(self):

        # TODO - her skal du have udlånt det korrekte materiale.
        # med det korrekte id og opdater objektet.
        # print("id der skal lånes: " + idnr)

        idnr = self.id_entry.get()
        found = False

        if len(idnr) == 0:
            messagebox.showwarning("Warning", "Input felten er tom!!!!")
        else:
            udlaanId = [bog1.idnr, bog2.idnr, bog3.idnr, film1.idnr, film2.idnr, film3.idnr]

            for laanid in udlaanId:
                if laanid == int(idnr):
                    self.listGui.delete('1.0', END)
                    list_index = udlaanId.index(laanid)
                    listMaterialer[list_index].antaludlaan = m.udlaan(1)
                    kan_udlaane = m.kan_udlaane(listMaterialer[list_index].antal,
                                                listMaterialer[list_index].antaludlaan)
                    print(listMaterialer[list_index].antal)
                    print(listMaterialer[list_index].antaludlaan)
                    print(kan_udlaane)
                    if not kan_udlaane:
                        messagebox.showwarning("Warning", "du kan ikke lån!!!")
                    self.listGui.insert(END, listMaterialer[list_index].tostring())
                    found = True

            if not found:
                messagebox.showwarning("Warning", "findes ikke!!!")

    def aflever(self):
        idnr = self.aflever_entry.get()
        print("id der skal afleveres: " + idnr)
        # TODO - her skal du have afleveret det korrekte materiale
        # med det korrekte id og så opdater det objekt.

    def sog_i_listen(self):
        search_text = self.entry.get()
        print("søge tekst: " + search_text)
        # TODO Nu skal listen af materiale søges igennem og
        # de materialer som matcher (dvs. hvor søgestrengen indgår som
        # en delstring) skal nu vises i listen og altså IKKE alle
        # materialer. Så du kan få brug for at slette det som
        # allerede står i vinduet og så tilføje de materialer
        # som matcher.

    def vis_hele_listen(self):
        print("Vis hele listen")
        # linjen nedenunder sletter hele listen i GUI'en
        # Den være være nyttig andre steder.....
        #    self.listGui.delete('1.0', END)
        # TODO - nu skal du vise HELE listen af materialer igen
        self.listGui.delete('1.0', END)
        for mat in listMaterialer:
            self.listGui.insert(INSERT, mat.tostring() + "\n")

    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame, text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        # Her definerer vi en Text widget - dvs
        # den kan indeholde multiple linjer
        # ideen er så at hver linje indeholde et styk materiale
        # Nedenunder kan du se hvordan listen af materiale løbes
        # igennem og toString metoden bliver kaldt og så bliver
        # der indsat en ny linje i Text widgeten
        self.listGui = Text(self, width=140)

        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.tostring() + "\n")
        frame.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
