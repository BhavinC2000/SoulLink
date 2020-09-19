import requests
from bs4 import BeautifulSoup
import tkinter as tk
import re

rowCounter = 6

usedTypes = []
pairs = []


class Pair:

    def __init__(self, name1, type1, name2, type2, gender1, gender2):
        global rowCounter
        self.button = tk.Button(win, text="(" + gender1 + ") " + name1 + " (" + type1 + ")  <--->  (" + gender2 + ") " + name2 + " (" + type2 + ")", command=self.kill)
        self.type1 = type1
        self.type2 = type2
        usedTypes.append(type1)
        usedTypes.append(type2)
        types.remove(type1)
        types.remove(type2)
        win.typeList.delete(0, 'end')
        for type in types:
            win.typeList.insert(tk.END, type)
        self.button.grid(column=0, row=rowCounter, columnspan=3)
        rowCounter += 1

    def kill(self):
        usedTypes.remove(self.type1)
        usedTypes.remove(self.type2)
        types.append(self.type1)
        types.append(self.type2)
        win.typeList.delete(0, 'end')
        for type in types:
            win.typeList.insert(tk.END, type)
        self.button.grid(column=0, row=rowCounter, columnspan=3)
        self.button.destroy()
        win.console.config(text="You just deleted a pair. You can now\nhave pokemon of type " + self.type1 + " and " + self.type2 + ".")

kanto = ["Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6", "Route 7", "Route 8", "Route 9", "Route 10", "Route 11", "Route 12", "Route 13", "Route 14", "Route 15", "Route 16", "Route 17", "Route 18", "Route 19", "Route 20", "Route 21", "Route 22", "Route 23", "Route 24", "Route 25", "Route 26", "Route 27", "Route 28", "Berry Forest", "Bond Bridge", "Canyon Entrance", "Cape Brink", "Celadon City", "Cerulean Cave", "Cerulean City", "Cinnabar Island", "Diglett's Cave", "Five Island", "Five Isle Meadow", "Four Island", "Fuchsia City", "Green Path", "Icefall Cave", "Indigo Plateau", "Kindle Road", "Lavender Town", "Lost Cave", "Memorial Pillar", "Mt. Ember", "Mt. Moon", "Navel Rock", "One Island", "Outcast Island", "Pallet Town", "Pattern Bush", "Pewter City", "Pokémon Mansion", "Pokémon Tower", "Power Plant", "Resort Gorgeous", "Roaming Kanto", "Rock Tunnel", "Ruin Valley", "Safari Zone", "Saffron City", "Seafoam Islands", "Sevault Canyon", "Silph Co.", "Tanoby Ruins", "Three Isle Port", "Tohjo Falls", "Trainer Tower", "Treasure Beach", "Underground Path 5-6", "Vermilion City", "Victory Road", "Viridian City", "Viridian Forest", "Water Labyrinth", "Water Path"]
jhoto = ["Route 29", "Route 30", "Route 31", "Route 32", "Route 33", "Route 34", "Route 35", "Route 36", "Route 37", "Route 38", "Route 39", "Route 40", "Route 41", "Route 42", "Route 43", "Route 44", "Route 45", "Route 46", "Route 47", "Route 48", "Azalea Town", "Bell Tower", "Blackthorn City", "Burned Tower", "Cherrygrove City", "Cianwood City", "Cliff Cave", "Cliff Edge Gate", "Dark Cave", "Dragon's Den", "Ecruteak City", "Embedded Tower", "Goldenrod City", "Ice Path", "Ilex Forest", "Lake of Rage", "Mt. Mortar", "Mt. Silver", "National Park", "New Bark Town", "Olivine City", "Roaming Johto", "Ruins of Alph", "Safari Zone Gate", "Sinjoh Ruins", "Slowpoke Well", "Sprout Tower", "Team Rocket HQ", "Tin Tower", "Union Cave", "Violet City", "Whirl Islands"]
hoenn = ["Route 101", "Route 102", "Route 103", "Route 104", "Route 105", "Route 106", "Route 107", "Route 108", "Route 109", "Route 110", "Route 111", "Route 112", "Route 113", "Route 114", "Route 115", "Route 116", "Route 117", "Route 118", "Route 119", "Route 120", "Route 121", "Route 122", "Route 123", "Route 124", "Route 125", "Route 126", "Route 127", "Route 128", "Route 129", "Route 130", "Route 131", "Route 132", "Route 133", "Route 134", "Abandoned Ship", "Altering Cave", "Artisan Cave", "Battle Resort", "Battle Tower", "Birth Island", "Cave of Origin", "Desert Underpass", "Dewford Town", "Ever Grande City", "Faraway Island", "Fiery Path", "Fortree City", "Granite Cave", "Jagged Pass", "Lilycove City", "Littleroot Town", "Marine Cave", "Meteor Falls", "Mirage Island", "Mirage Spots", "Mirage Tower", "Mossdeep City", "Mt. Pyre", "New Mauville", "Pacifidlog Town", "Petalburg City", "Petalburg Woods", "Roaming Hoenn", "Rustboro City", "Rusturf Tunnel", "Safari Zone", "Scorched Slab", "Sea Mauville", "Seafloor Cavern", "Sealed Chamber", "Shoal Cave", "Sky Pillar", "Slateport City", "Sootopolis City", "Southern Island", "Team Magma/Aqua Hideout", "Terra Cave", "Victory Road"]
kalos = ["Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6", "Route 7", "Route 8", "Route 9", "Route 10", "Route 11", "Route 12", "Route 13", "Route 14", "Route 15", "Route 16", "Route 17", "Route 18", "Route 19", "Route 20", "Route 21", "Route 22", "Ambrette Town", "Anistar City", "Aquacorde Town", "Azure Bay", "Battle Chateau", "Battle Maison", "Camphrier Town", "Chamber of Emptiness", "Connecting Cave", "Coumarine City", "Couriway Town", "Cyllage City", "Dendemille Town", "Flare Cafe", "Frost Cavern", "Geosenge Town", "Glittering Cave", "Kalos Power Plant", "Kiloude City", "Laverre City", "Lost Hotel", "Lumiose City", "Parfum Palace", "Poké Ball Factory", "Pokémon League", "Pokémon Village", "Reflection Cave", "Roaming Kalos", "Santalune City", "Santalune Forest", "Sea Spirit's Den", "Shalour City", "Snowbelle City", "Team Flare HQ", "Terminus Cave", "Tower of Mastery", "Unknown Dungeon", "Vaniville Town", "Victory Road"]

names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran (Female)", "Nidorina", "Nidoqueen", "Nidoran (Male)", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet", "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys"]
types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy", "???"]

def kantoReg():
    win.routeList.delete(0, 'end')
    for route in kanto:
        win.routeList.insert(tk.END, route)

def jhotoReg():
    win.routeList.delete(0, 'end')
    for route in jhoto:
        win.routeList.insert(tk.END, route)

def hoennReg():
    win.routeList.delete(0, 'end')
    for route in hoenn:
        win.routeList.insert(tk.END, route)

def kalosReg():
    win.routeList.delete(0, 'end')
    for route in kalos:
        win.routeList.insert(tk.END, route)


def getPokemonURL(pokeName):
    return requests.get("https://pokemondb.net/pokedex/" + pokeName).content
    


def getType(pokeName):
    try:
        soup = BeautifulSoup(getPokemonURL(pokeName), 'html.parser')

        el = soup.select('a.type-icon')
        typeNamePattern = re.compile(r'(\w*)(-type)?')
        match = typeNamePattern.match(el[0].text)
        return match.group(1)
    except IndexError:
        clear()
        win.console.config(text="Sorry, one or both Pokemon does not exist.")

def clear():
    win.entry1.delete(0, 'end')
    win.entry2.delete(0, 'end')

def pair():
    try:
        poke1 = win.entry1.get()
        if poke1.isdigit():
            poke1 = names[int(poke1) - 1]
        type1 = getType(poke1)
        poke2 = win.entry2.get()
        if poke2.isdigit():
            poke2 = names[int(poke2) - 1]
        type2 = getType(poke2)
        if type1 is None or type2 is None:
            return
        if type1 == type2:
            clear()
            win.console.config(text="Sorry, there is a type conflict.")
            return
        for types in usedTypes:
            if type1 == types or type2 == types:
                clear()
                win.console.config(text="Sorry, there is a type conflict.")
                return
        if var1.get() == 0:
            clear()
            win.console.config(text="Sorry, no gender was specified.")
            return
        elif var1.get() == 1:
            gender1 = "Male"
            gender2 = "Female"
        else:
            gender1 = "Female"
            gender2 = "Male"
        var1.set(0)
        pairs.append(Pair(poke1, type1, poke2, type2, gender1, gender2))
        clear()
        win.routeList.itemconfig(win.routeList.curselection(), {'bg':'green'})
        win.console.config(text="Congratulations!! A new pair!!")
    except ValueError:
        clear()
        win.console.config(text="Sorry, one or both Pokemon was not inputted.")



win = tk.Tk()

win.title = "Soul Link"

win.geometry("1000x400")

win.entry1 = tk.Entry(win)
win.entry1.grid(column=0, row=2)

var1 = tk.IntVar()
var1.set(0)
win.order1= tk.Radiobutton(win, text="Male <--> Female", variable=var1, value=1)
win.order2 = tk.Radiobutton(win, text="Female <--> Male", variable=var1, value=2)
win.order1.grid(column=1, row=3)
win.order2.grid(column=1, row=4)

win.label = tk.Label(win, text="<---->")
win.label.grid(column=1, row=2)

win.entry2 = tk.Entry(win)
win.entry2.grid(column=2, row=2)

win.submit = tk.Button(win, text="Create Pair", command=pair)
win.submit.grid(column=4, row=2)

win.team1 = tk.Label(win, text="Pairs")
win.team1.grid(column=1, row=5)

win.console = tk.Label(win, text="Welcome to a Soul Link!\nFirst, choose your region!")
win.console.grid(column=3, row=5, rowspan=10)

scrollbar1 = tk.Scrollbar(win)
win.routeList = tk.Listbox(win, yscrollcommand=scrollbar1.set)
for route in kanto:
    win.routeList.insert(tk.END, route)
win.routeList.grid(column=3, row=2, rowspan = 3)

scrollbar = tk.Scrollbar(win)
win.typeList = tk.Listbox(win, yscrollcommand=scrollbar.set)
for type in types:
    win.typeList.insert(tk.END, type)
win.typeList.grid(column=4, row=5, rowspan = 10)

win.menu = tk.Menu(win)
chooseGame = tk.Menu(win.menu, tearoff=0)
chooseGame.add_command(label="Kanto", command=kantoReg)
chooseGame.add_command(label="Jhoto", command=jhotoReg)
chooseGame.add_command(label="Hoenn", command=hoennReg)
chooseGame.add_command(label="Kalos", command=kalosReg)

win.menu.add_cascade(label="Choose Region", menu=chooseGame)

win.config(menu=win.menu)
win.mainloop()
