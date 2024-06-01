import json
import tkinter as tk
from tkinter import messagebox

# numuri = [52764, 52765, 52767, 52768, 52769, 52770, 52771, 52772, 52773, 52774, 52775, 52776, 52777, 52779, 52780, 52781, 52782, 52783, 52784, 52785, 52786, 52787, 52788, 52791, 52792, 52793, 52794, 52795, 52796, 52797, 52802, 52803, 52804, 52805, 52806, 52807, 52808, 52809, 52810, 52811, 52812, 52813, 52814, 52815, 52816, 52817, 52818, 52819, 52820, 52821, 52822, 52823, 52824, 52826, 52827, 52828, 52829, 52830, 52831, 52832, 52833, 52834, 52835, 52836, 52837, 52838, 52839, 52840, 52841, 52842, 52843, 52844, 52845, 52846, 52847, 52848, 52849, 52850, 52851, 52852, 52853, 52854, 52855, 52856, 52857, 52858, 52859, 52860, 52861, 52862, 52863, 52864, 52865, 52866, 52867, 52868, 52869, 52870, 52871, 52872, 52873, 52874, 52875, 52876, 52877, 52878, 52879, 52880, 52881, 52882, 52883, 52884, 52885, 52886, 52887, 52888, 52889, 52890, 52891, 52892, 52893, 52894, 52895, 52896, 52897, 52898, 52899, 52900, 52901, 52902, 52903, 52904, 52905, 52906, 52907, 52908, 52909, 52910, 52911, 52912, 52913, 52914, 52915, 52916, 52917, 52918, 52919, 52920, 52921, 52922, 52923, 52924, 52925, 52926, 52927, 52928, 52929, 52930, 52931, 52932, 52933, 52934, 52935, 52936, 52937, 52938, 52939, 52940, 52941, 52942, 52943, 52944, 52945, 52946, 52947, 52948, 52949, 52950, 52951, 52952, 52953, 52954, 52955, 52956, 52957, 52958, 52959, 52960, 52961, 52962, 52963, 52964, 52965, 52966, 52967, 52968, 52969, 52970, 52971, 52972, 52973, 52974, 52975, 52976, 52977, 52978, 52979, 52980, 52981, 52982, 52987, 52988, 52989, 52990, 52991, 52992, 52993, 52994, 52995, 52996, 52997, 52998, 52999, 53000, 53005, 53006, 53007, 53008, 53009, 53010, 53011, 53012, 53013, 53014, 53015, 53016, 53017, 53018, 53019, 53020, 53021, 53022, 53023, 53024, 53025, 53026, 53027, 53028, 53029, 53030, 53031, 53032, 53033, 53034, 53035, 53036, 53037, 53038, 53039, 53040, 53041, 53042, 53043, 53044, 53045, 53046, 53047, 53048, 53049, 53050, 53051, 53052, 53053, 53054, 53055, 53056, 53057, 53058, 53059, 53060, 53061, 53062, 53063, 53064, 53065, 53067, 53068, 53069, 53070, 53071, 53072, 53073, 53074, 53075, 53076, 53077, 53078, 53079, 53080, 53081, 53082, 53083]

#Tā kā informācija .txt failā ir angliski nepieciešams tulkot gan kategorijas, gan ēdienus
kategorijas_tulk = {
    "Liellops": "Beef",
    "Vista": "Chicken",
    "Deserts": "Dessert",
    "Jērs": "Lamb",
    "Cits": "Miscellaneous",
    "Pasta": "Pasta",
    "Cūkgaļa": "Pork",
    "Jūras veltes": "Seafood",
    "Uzkoda": "Side",
    "Starteris": "Starter",
    "Vegānisks": "Vegan",
    "Veģetārs": "Vegetarian"
}

valstis_tulk = {
    "Amerikāņu": "American",
    "Britu": "British",
    "Kanādiešu": "Canadian",
    "Ķīniešu": "Chinese",
    "Horvātu": "Croatian",
    "Holandiešu": "Dutch",
    "Ēģiptiešu": "Egyptian",
    "Filipīniešu": "Filipino",
    "Grieķu": "Greek",
    "Indiešu": "Indian",
    "Īru": "Irish",
    "Itāļu": "Italian",
    "Jamaikiešu": "Jamaican",
    "Japāņu": "Japanese",
    "Malaiziešu": "Malaysian",
    "Meksikāņu": "Mexican",
    "Marokāniešu": "Moroccan",
    "Poļu": "Polish",
    "Portugāļu": "Portuguese",
    "Spāņu": "Spanish",
    "Taju": "Thai",
    "Tunīziešu": "Tunisian",
    "Turku": "Turkish",
    "Vjetnamiešu": "Vietnamese",
    "Cits": "Unknown"
}

#Izveidots uznirstošais logs
logs = tk.Tk()
logs.geometry("500x300")
logs.title("Ēdienu izvēle")

#Izveidoti izkrītošie saraksti kategorijai un valstij
kategorijas_varianti = tk.StringVar(logs)
kategorijas_varianti.set("Kategorija")

valstis_varianti= tk.StringVar(logs)
valstis_varianti.set("Valsts")

l1 = tk.Label(logs, text='Izvēlēties kategoriju', width=12)
l1.grid(row=1, column=1)

#Izkrītošajā sarakstā rāda kategoriju variantu latviskos nosaukumus ar .keys() palīdzību dict 
om1 = tk.OptionMenu(logs, kategorijas_varianti, *kategorijas_tulk.keys())
om1.grid(row=1, column=2)

l3 = tk.Label(logs, text='Izvēlēties valsti', width=12)
l3.grid(row=2, column=1)

#Izkrītošajā sarakstā rāda valstu variantu latviskos nosaukumus ar .keys() palīdzību dict 
om2 = tk.OptionMenu(logs, valstis_varianti, *valstis_tulk.keys())
om2.grid(row=2, column=2)

#Izveidota poga apstiprināšanai, kas parāda ēdienus ar funkcijas palīdzību
b1 = tk.Button(logs, text='Parādīt ēdienus', command=lambda: edieni_kopa())
b1.grid(row=3, column=1)

# Izveidots norādošais uzraksts par klikšķināšanu uz ēdieniem
l2 = tk.Label(logs, text='Klikšķiniet uz ēdiena, lai redzētu recepti', width=30)
l2.grid(row=4, column=1, columnspan=2)

#Izveidots recepšu uznirstošais logs
popups = tk.Listbox(logs, height=10, width=50)  
popups.grid(row=5, column=1, columnspan=3)

#Veidota funkcija ēdienu info ievākšanai
def edieni_kopa():
    izveleta_kategorija_lv = kategorijas_varianti.get() #Iegūta izvēlētā kategorija logā
    izveleta_valsts_lv = valstis_varianti.get() #Iegūta izvēlētā valsts logā

    if izveleta_kategorija_lv == "Kategorija" or izveleta_valsts_lv == "Valsts": #Ja netiek izvēlēts kaut viens, tiek parādīta attiecīga ziņa
        messagebox.showwarning("Uzmanību!", "Lūdzu, izvēlieties kategoriju un valsti!")
        return

    for kategorija_lv, kategorija_ang in kategorijas_tulk.items(): #Kategorija tiek pārtulkota, lai varētu strādāt ar .txt failu
        if kategorija_lv == izveleta_kategorija_lv:
            izveleta_kategorija_ang = kategorija_ang
            break

    for valsts_lv, valsts_ang in valstis_tulk.items():
        if valsts_lv == izveleta_valsts_lv:
            izveleta_valsts_ang = valsts_ang
            break

    global edieni1
    edieni1 = [] 
    
    #Iet cauri datiem kuri atbilst lietotāja ievadītajam un ielikti sarakstā
    for edieni in izvade(izveleta_kategorija_ang, izveleta_valsts_ang):
        edieni1.append(edieni)

    popups.delete(0, tk.END) #Notīrīti varianti kad tiek izvēlētas jaunas valstis/ kategorijas

    for ediens in edieni1:
        popups.insert(tk.END, ediens['strMeal']) #Tiek parādīti ēdieni

#Veidota funkcija, lai noteiktu, kuri ēdieni no .txt faila atbilst lietotāja ievadītajam
def izvade(kategorija_angliski, valsts_angliski):
    edieni = []
    with open("dati.txt", "r") as dati:
        for k in dati:
            ediens = json.loads(k)
            if ediens['strCategory'] == kategorija_angliski and ediens['strArea'] == valsts_angliski:
                edieni.append(ediens)
    return edieni

#Veidota funkcija klikšķim priekš receptēm
def uzspiez(klikskis):
    loga_kliskis = klikskis.widget
    pec_kartas = loga_kliskis.curselection() #Reģistrē kurš pēc kārtas ir izvēlētais ēdiens tieši logā.
    izvele = popups.get(pec_kartas) #Reģistrē, ka izvēle ir tieši tas ēdiens
    for ediens in edieni1:
        if ediens['strMeal'] == izvele: #Ja ēdiens no .txt faila ir vienāds ar izvēli beidz for loop un veic receptes iegūšanas funkciju
            break
    recepte(ediens)

def recepte(ediens):
    recepte = ediens['strInstructions'] #Izvēlētā ēdiena recepte
    messagebox.showinfo(ediens['strMeal'], recepte) #Loga augšas nosaukums (strMeal) un saturs (recepte)

popups.bind('<<ListboxSelect>>', uzspiez) #Kad tiek veikta izvēle Listbox (popup), sākas funkcija "uzspiez"

logs.mainloop()

# visi_dati = []

# for nr in numuri:
#     dati = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={nr}').json()
#     dats = dati["meals"]
#     visi_dati.extend(dats) 
# visi_dati = list({json.dumps(k) for k in visi_dati})

# with open("dati.txt", "w") as file:
#     for k in all_dati:
#         file.write(k)
#         file.write("\n")

