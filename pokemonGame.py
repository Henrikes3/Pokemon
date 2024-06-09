import random

pokemons = {
'pokemon muito comum' : [
'Caterpie',
'Weedle',
'Pidgey',
'Rattata',
'Ekans',
'Sandshrew',
'Nidoran(Female)',
'Nidoran(Male)',
'Zubat',
'Geodude',
'Bellsprout',
'Machop',
'Poliwag',
'Mankey',
'Meowth',
'Venonat',
'Paras',
'Oddish',
'Slowpoke',
'Magnemite',
'Gastly',
'Krabby',
'Voltorb',
'Goldeen',
'Magikarp',
'Eevee'
],
'pokemon comum' : [
'Bulbasaur',
'Charmander',
'Squirtle',
'Metapod',
'Kakuna',
'Pidgeotto',
'Raticate',
'Spearow',
'Arbok',
'Psyduck',
'Persian',
'Diglet',
'Golbat',
'Jigglypuff',
'Vulpix',
'Clefairy',
'Sandslash',
'Pikachu',
'Growlith',
'Abra',
'Machoke',
'Tentacool',
'Graveler',
'Ponyta',
'Magneton',
'Doduo',
'Seel',
'Koffing',
'Hitmonlee',
'Cubone',
'Exeggcute',
'Electrode',
'Drowzee',
'Haunter',
'Shellder',
'Grimer',
'Rhyhorn',
'Horsea',
'Staryu',
'Jynx'
],
'pokemon incomum' : [
'Butterfree',
'Fearow',
'Nidorina',
'Nidorino',
'Wigglytuff',
'Gloom',
'Parasect',
'Dugtrio',
'Kabuto',
'Golem',
'Tentacruel',
'Machamp',
'Kadabra',
'Poliwhirl',
'Chansey',
'Primeape',
'Golduck',
'Dratini',
'Dodrio',
'Cloyster',
'Scyther',
'Hypno',
'Seadra',
'Seaking',
'Starmie'
],
'pokemons raro' : [
'Beedrill',
'Pidgeot',
'Weepinbell',
'Pinsir',
'Snorlax',
'Mr. Mime',
'Farfetch\'d',
'Onix',
'Exeggutor',
'Muk',
'Arcanine',
'Rapidash',
'Rhydon',
'Kingler',
'Magmar',
'Flareon',
'Jolteon',
'Tangela'
],
'pokemons muito raro' : [
'Gyarados',
'Lapras',
'Vaporeon',
'Kabutops',
'Ivysaur',
'Charmeleon',
'Wartortle',
'Porygon',
'Omanyte',
'Dragonair',
'Raichu',
'Nidoqueen',
'Nidoking',
'Vileplume',
'Gengar',
'Marowak',
'Dewgong',
'Kangaskhan',
'Victreebel',
'Electabuzz',
'Alakazam',
'Poliwrath',
'Venomoth'
],
'pokemons epico' : [
'Aerodactyl',
'Venusaur',
'Charizard',
'Blastoise',
'Clefable',
'Tauros',
'Omastar',
'Dragonite'
],
'pokemons lendario' : [
'Ditto',
'Articuno',
'Zapdos',
'Moltres',
'Mewtwo',
'Mew'
]
}

raridade = [0.7, 0.6, 0.4, 0.3, 0.2, 0.1, 0.05]
box = []

while True:
    escolha_raridade = random.choices(list(pokemons.keys()), weights = raridade, k=1)[0]
    escolha_pokemon = random.choice(list(pokemons[escolha_raridade]))



    print(escolha_raridade)
    print(escolha_pokemon)

    capturar = input('capturar pokemon?(s/n)')
    tentativa = ()

    def capturar_pokemon():
        if tentativa == 1:
            box.append(escolha_pokemon)
            print(f'Você capturou {escolha_pokemon}!')
        elif tentativa == 2:
            print(f'{escolha_pokemon} escapou!')
            pass



    if capturar == 's':
        tentativa = random.randint(1, 2)
        capturar_pokemon()
        print(list(box))
    elif capturar == 'n':
        continue


