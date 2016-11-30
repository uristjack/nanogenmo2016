import random
from compiler.ast import flatten
import storygen
import eventgen
from pylatex import * # Yes, I know this is shitty code. No, I do not care right now.

"""
This program is part 3 of uristjack's Story Writer for NaNoGenMo, and for my CAS hours.
This is as per the structure of:
    https://gist.github.com/cpressey/6324fff6ef0dfdf69b96
This module treats the story structure as a tree, denoted as a list of lists.
It then complicates the tree, making the plot more complicated.

Licensed under the GNU General Public License, Version 3 by Julian Ferrone, 2016.
"""

# Replace events with structures of sentences. These will be turned into sentences in a sentence generator
# ALLCAPS are for titles, not sentences - they are for LaTeX

# Oh, and BTW, my secrets are going to be based on your average Tumblrina - A discovers B was a pyrogender trifox, or bimorphic chaosgender, or so on

newesttree = []

def sentencegen(x):
    # This plugs into the other two modules, giving me a final tree to transform.
    eventgen.eventgen(x)
    global newesttree
    newesttree = eventgen.bobtree

    doc = Document()
    
    for (i, item) in enumerate(newesttree):
        if item == "INTRO_TITLE":
            with doc.create(Section("The Multiverse", numbering = False)):
                doc.append('John and Jane are two characters living in a multiverse.')
                doc.append('They have one thing in common amongst every timeline, however.')
                doc.append('And what is this one thing in common?')
                doc.append('John is a criminal. And Jane is his victim.')

        if item == "DescribeA":
            eyecolourlist = ["amber", "blue", "brown", "hazel", "gray", "green"]
            skincolourlist = ["espresso", "chestnut", "deep bronze", "bronze", "golden bronze", "golden beige", "medium beige", "apricot", "light beige", "fair", "very fair"]                          
            haircolourlist = ["black", "brown", "blond", "auburn", "chestnut", "red", "gray", "white"]

            eyecolour = str(random.choice(eyecolourlist))
            skincolour = str(random.choice(skincolourlist))
            haircolour = str(random.choice(haircolourlist))
            
            doc.append("John has " + eyecolour + " eyes, " + skincolour + " skin, and " + haircolour + " hair.")

        if item == "DescribeB":
            eyecolourlist = ["amber", "blue", "brown", "hazel", "gray", "green"]
            skincolourlist = ["espresso", "chestnut", "deep bronze", "bronze", "golden bronze", "golden beige", "medium beige", "apricot", "light beige", "fair", "very fair"]                          
            haircolourlist = ["black", "brown", "blond", "auburn", "chestnut", "red", "gray", "white"]

            eyecolour = str(random.choice(eyecolourlist))
            skincolour = str(random.choice(skincolourlist))
            haircolour = str(random.choice(haircolourlist))
            
            doc.append("Jane has " + eyecolour + " eyes, " + skincolour + " skin, and " + haircolour + " hair.")

        if item == "DescribeMultiverse":
            vowellist = ["a",
                 "e",
                 "i",
                 "o",
                 "u",
                 "y"]

            # Note. This also includes dipthongs.
            consonantlist = ["b", "c", "d", "f",
                             "g", "h", "j", "k",
                             "l", "m", "n", "o",
                             "p", "r", "s", "t",
                             "u", "v", "w", "x",
                             "y", "z", "th", "sh"]
            citynamefirst = str(random.choice(consonantlist) + random.choice(vowellist) +
                           random.choice(consonantlist) + random.choice(vowellist) +
                           random.choice(consonantlist) + random.choice(vowellist))

            citynamesecond = str(random.choice(consonantlist) + random.choice(vowellist) +
                           random.choice(consonantlist) + random.choice(vowellist) +
                           random.choice(consonantlist) + random.choice(vowellist))
            
            citynamefirst = citynamefirst[:1].upper() + citynamefirst[1:]
            citynamesecond = citynamesecond[:1].upper() + citynamesecond[1:]

            cityname = str(citynamefirst + "-" + citynamesecond)

            directionlist =["North",
                "East",
                "West",
                "South",
                "North-East",
                "North-West",
                "South-East",
                "South-West"]

            direction = str(random.choice(directionlist))
            
            doc.append("Now, the multiverse is a big place. But we are only concerned with one very small part of it - the city of " + cityname + ", jewel of the " + direction + ", and where John and Jane live.")
            doc.append("This is where, throughout every timeline, John attacks Jane in some way.")

        if item == "DescribeDay":
            weatherlist = ["rainy",
                           "sunny",
                           "hailing",
                           "cloudy",
                           "clear",
                           "overcast",
                           "stormy",
                           "foggy"]
          
            temperaturelist = ["cool",
                               "cold",
                               "warm",
                               "moderate",
                               "average",
                               "warmer than normal",
                               "hot",
                               "cooler than normal"]

            windlist = ["a light breeze",
                        "a gale",
                        "a light wind",
                        "a moderate wind",
                        "a heavy wind"]
                
            directionlist =["North",
                            "East",
                            "West",
                            "South",
                            "North-East",
                            "North-West",
                            "South-East",
                            "South-West"]

            monthlist = ["January",
                         "February",
                         "March",
                         "April",
                         "May",
                         "June",
                         "July",
                         "August",
                         "September"
                         "October",
                         "November",
                         "December"]
            
            temp = str(random.choice(temperaturelist))
            weather = str(random.choice(weatherlist))
            wind = str(random.choice(windlist))
            direction = str(random.choice(directionlist))
            month = str(random.choice(monthlist))
            
            doc.append("On this particular day, the 5th of " + month + ", it was " + temp + " and " + weather + ", with " + wind + " coming from the " + direction +".")

        if item == "CONCLUSION_TITLE":
            with doc.create(Section("The End")):
                doc.append('And so, after looking through innumerable timelines, we come to this.')
                doc.append(' The end.')
                doc.append(' Well, not quite.')
                doc.append('There are still innumerable timelines to explore.')

        if item == "FindOutNextEpisode":
            doc.append('But we\'ve run out of time.')
            doc.append('So long, folks!') # Looney Tunes reference here

        if item == "NEW_PARAGRAPH_THREATENED":
            with doc.create(Subsection("A Timeline In Which John Threatens Jane With A Revolver")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_BLACKMAIL":
            with doc.create(Subsection("A Timeline In Which John Blackmails Jane")):
                doc.append('')
                 
        if item == "NEW_PARAGRAPH_DRUGGED":
            with doc.create(Subsection("A Timeline In Which John Drugs Jane")):
                doc.append('')
                 
        if item == "NEW_PARAGRAPH_SPIEDUPON":
            with doc.create(Subsection("A Timeline In Which John Spies Upon Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_EXTORTED":
            with doc.create(Subsection("A Timeline In Which John Tortures Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_ABUSED":
            with doc.create(Subsection("A Timeline In Which John Researchs Jane Using The Intertubes")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_SEDUCED":
            with doc.create(Subsection("A Timeline In Which John Seduces Jane")):
                doc.append('')
    
        if item == "NEW_PARAGRAPH_PROSTITUTION":
            with doc.create(Subsection("A Timeline In Which John Buys 'Favours' From Jane")):
                doc.append('')
                            
        if item == "NEW_PARAGRAPH_RAPE":
            with doc.create(Subsection("A Timeline In Which John Has His Way With Jane")):
                doc.append('')
                            
        if item == "NEW_PARAGRAPH_STRANGLED":
            with doc.create(Subsection("A Timeline In Which John Strangles Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_STABBED":
            with doc.create(Subsection("A Timeline In Which John Stabs Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_SUICIDE":
            with doc.create(Subsection("A Timeline In Which John Persuades Jane To Commit Suicide")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_MUGGED":
            with doc.create(Subsection("A Timeline In Which John Mugs Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_SCAM":
            with doc.create(Subsection("A Timeline In Which John Scams Jane")):
                doc.append('')
                
        if item == "NEW_PARAGRAPH_COUNTERFEIT":
            with doc.create(Subsection("A Timeline In Which John Sells Counterfeits To Jane")):
                doc.append('')

        if item == "APullsOutGun":
            roomlist = ["bar",
                        "cafe",
                        "restaurant",
                        "club",
                        "nightclub",
                        "pub",
                        "bookstore",
                        "library",
                        "park"]                        
            room = str(random.choice(roomlist))
            doc.append("John is sitting in the " + room + ".")
            doc.append("He sees a victim - Jane - someone he can threaten. He pulls out his gun, a revolver.")

        if item == "DescribeGun":
            guntypelist = ["Taurus Judge", "Chiappa Rhino", "Ruger LCR",
                           "Ruger Alaskan", "Smith & Wesson Model 500", "Smith & Wesson Model 340PD",
                           "Taurus Model 608", "OTs-20 Gnom", "U-94 Udar", "Ruger Vaquero",
                           "MP-412 REX", "Colt Anaconda", "Manurhin MR 73", "Charter Arms Bulldog"]
            guntype = str(random.choice(guntypelist))
            
            doc.append('But not just any revolver, but a ' + guntype + ".")

        if item == "AThreatensB":
            gesturesynonymlist = ["gestures at", "motions at", "waves at", "gesticulates at"]
            gesturesynonym = str(random.choice(gesturesynonymlist))
            compliancelist = ["comply with", "go along with", "yield to", "capitulate to", "relent to", "give in to"]
            compliance = str(random.choice(compliancelist))
            palelist = ["pales", "blanches", "whitens", "loses colour", "turns pallid", "becomes pale"]
            pale = str(random.choice(palelist))
                        
            doc.append("John " + gesturesynonym + " Jane with his revolver. Her face " + pale + ", and John knows that she will " + compliance + " with his demands.")

        if item == "BAcquiesces":
            quietlist = ["is silent", "is quiet", "is completely quiet", "is so quiet you could hear a pin drop"]
            quiet = str(random.choice(quietlist))

            doc.append("Jane " + quiet + ". She will do anything to remove the present danger. And so she complies with John's demands...")

        if item == "APullsOutBlackmail":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            colour = str(random.choice(colourlist))
            doc.append("John pulls out a letter, encased in a " + colour + " envelope. Inside, he knows, is information known only to him and his victim. And that information will grant him power.")

        if item == "DescribeBSecret":
            sexualitylist = ["abrosexual", "aceflux", "aegosexual", "androsexual",
                             "akiosexual", "aliquasexual", "amicussexual", "amorplatonic",
                             "androphiliac", "antihaemosexual", "apothi", "aromantic",
                             "aroflux", "arospike", "autosexual", "bellusromantic",
                             "culparomantic", "demisexual", "desinoromantic", "gerontosexual",
                             "gynephiliac", "gynosexual", "heteroflexible", "iculasexual",
                             "intrasexual", "intraromantic", "idemromantic", "kalossexual",
                             "menosexual", "multisexual", "nocismasexual", "objectumsexual",
                             "platoniromantic", "polyamorous", "pomosexual", "quoiromantic",
                             "sapiosexual", "skoliosexual", "apachehelisexual"]
            sexuality = str(random.choice(sexualitylist))
            genderlist = ["abimegender", "absorgender", "adamasgender", "adeptogender", "aerogender",
                          "aesthetgender", "videgender", "aethergender", "affectugender", "agender",
                          "agenderfluid", "agenderflux", "cancegender", "librafluid", "alexigender",
                          "aliusgender", "ambigender", "amaregender", "ambonec", "amicagender", "amogender",
                          "flirtgender", "amorgender", "androgyne", "anesigender", "angeligender", "angenital",
                          "anogender", "astralgender", "batmangender", "boggender", "blizzgender", "bigenderfluid",
                          "borderfluid", "canisgender", "chaosgender", "chaosflux", "cheiragender", "circgender",
                          "cloudgender", "cogitofluid", "burstgender", "duragender", "earthgender", "digigender",
                          "dryagender", "fissgender", "firegender", "flowergender", "fluidflux", "gemelgender",
                          "geminigender", "scorpiogender", "sagittariusgender", "genderale", "genderblank",
                          "genderblur", "genderfuzz", "heliogender", "horogender", "hydrogender", "intergender",
                          "invisigender", "kingender", "leogender", "mirrorgender", "mosaigender", "nesciogender",
                          "nobifluid", "nyctogender", "proxvir", "quivergender", "scorigender", "seagender",
                          "stargender", "stratogender", "technogender", "vagueflux", "vectorgender", "zodiacgender"]
            gender = str(random.choice(genderlist))
            numberlist = ["uni", "bi",
                          "tri", "quadra",
                          "quinto", "hexa",
                          "hepto", "septo",
                          "octo", "deca",
                          "centi", "milli",
                          "hecto", "kilo",
                          "mega", "giga",
                          "tera", "peta"]
            number = str(random.choice(numberlist))
            animallist = ["fox","wolf","dog","dragon","cat",
                          "tiger","skunk","horse","coyote","rat",
                          "lion","rabbit","otter","cheetah","eagle",
                          "raccoon","bear","bull","hyena","kangaroo",
                          "gryphon","leopard","lynx","ferret","squirrel",
                          "panther","mouse","bat","snail","deer"]
                          
            animal = str(random.choice(animallist))
            doc.append("John knows Jane's secret. What is her secret? She is a " + sexuality + " " + gender + " " + number + animal + ", and she will do anything to ensure nobody knows.")
            
        if item == "ABlackmailsB":
            emailaddressprefixlist = ["fox","wolf","dog","dragon","cat",
                                      "tiger","skunk","horse","coyote","rat",
                                      "lion","rabbit","otter","cheetah","eagle",
                                      "raccoon","bear","bull","hyena","kangaroo",
                                      "gryphon","leopard","lynx","ferret","squirrel",
                                      "panther","mouse","bat","snail","deer"]
            emailendinglist = [".com", ".net", ".org", ".club", ".pizza", ".int", ".mil", ".academy",
                               ".accountant", ".adult", ".apartments", ".deepweb", ".app", ".io",
                               ".audio", ".beer", ".scotchwhisky", ".whisky", ".wine", ".best",
                               ".blue", ".red", ".orange", ".yellow", ".green", ".cyan", ".purple",
                               ".white", ".black", ".gray", ".build", ".post", ".criminal", ".probablyillegal",
                               ".social", ".sucks", ".landica"]
            emailproviderlist = ["amail", "bmail", "cmail", "dmail", "fmail",
                                 "hmail", "imail", "jmail", "kmail", "mmail",
                                 "nmail", "omail", "pmail", "chainmail", "qmail",
                                 "rmail", "smail", "tmail", "umail", "vmail",
                                 "wmail", "xmail", "ymail", "zmail", "jesuschrist"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            emailaddress = str(random.choice(colourlist) + random.choice(emailaddressprefixlist) + str(random.randint(10,1000)))
            emailprovider = str(random.choice(emailproviderlist))
            emailending = str(random.choice(emailendinglist))
            email = str(emailaddress + "@" + emailprovider + emailending)
            doc.append("John sends off the letter, express post. He knows she will reply to the email address - " + email + " - he added soon...")

        if item == "APullsOutDrug":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            colour = str(random.choice(colourlist))
            doc.append("John pulls out a small " + colour + " packet from his pocket. Inside is one of his favourite (although illicit) drugs.")

        if item == "DescribeDrug":
            prefixlist = ["cephi", "corto", "tretino", "sulface", "trypto", "co", "opio", "ampheto",
                          "fluco", "keto", "aceta", "saxa", "sita", "lina", "ome", "esome", "doxy", "buta",
                          "butal", "futa", "beta", "alpha", "omega", "avana", "sildena", "clo"]
                          
            prefix = str(random.choice(prefixlist))
            suffixlist = ["fil", "sone", "bicin", "bital", "caine", "cillin", "cycline", "dazole", "dipine",
                          "dronate", "prazole", "fenac", "floxacin", "gliptin", "glitazone", "iramine", "lamide",
                          "mab", "mustine", "mycin", "nacin", "nazole", "lol", "lone", "nide", "prazole", "parin",
                          "phylline", "pramine", "pril", "profen", "ridone", "sartan", "semide", "setron", "statin",
                          "tadine", "terol", "thiazide", "tinib", "trel", "tretin", "triptan", "tyline", "vir",
                          "vudine", "zepam", "zodone", "zolam", "zosin"]
            suffix = str(random.choice(suffixlist))
            drugname = str(prefix + suffix)
            doc.append("The drug? None other than " + drugname + ", one of the most expensive drugs on the black market.")

        if item == "ADrugsB":
            cocktaillist = ["Martini", "Margarita", "Nanhattan", "Daiquiri", "Mojito", "Cosmopolitan",
                            "Fizz", "Pina Colada", "Mai Tai", "Gimlet"]
            cocktail = str(random.choice(cocktaillist))
            doc.append("John quickly dumps the powder into Jane's " + cocktail + ".")
            doc.append("Jane finishes off the rest of her drink, unaware of its extra ingredient.")

        if item == "DescribeEffectedB":
            sideeffectlist = ["mildly nauseous", "mildly dizzy",
                              "slightly nauseous", "slightly dizzy",
                              "nauseous", "dizzy",
                              "fairly nauseous", "dizzy",
                              "very nauseous", "very dizzy"]
            sideeffect = str(random.choice(sideeffectlist))
            pliablelist = ["pliable", "malleable", "impressionable", "flexible",
                           "adaptable", "pliant", "docile", "manageable",
                           "controllable", "persuadable", "receptive", "susceptible",
                           "susceptive", "amenable", "manipulable", "accommodating"]
            pliable = str(random.choice(pliablelist))
            doc.append("Shortly afterwards, Jane feels " + sideeffect + ", but it passes.")
            doc.append("More dangerously, however, she is rendered " + pliable + ", which is exactly as John wants her...")

        if item == "AResearchesB":
            webprefixlist = ["Face", "You", "Goo", "Podo", "My", "Social", "Blogo", "Wiki", "Twit", "Digi",
                             "Bubble", "Dyna", "Vlog", "Flip", "Snap"]
            websuffixlist = ["cast", "zip", "blog", "hoo", "tube", "sphere", "tag", "point", "crunch", "zone",
                             "graph", "vine", "tech", "path", "zoom", "space", "chat"]
            webprefix = str(random.choice(webprefixlist))
            websuffix = str(random.choice(websuffixlist))
            socialmedia = str(webprefix + websuffix)
            doc.append("John fires up his favourite software, which he knows will get him the information he needs.")
            doc.append("He points it at Jane's " + socialmedia + " account, and in a short time every single piece of information he needs on her will be his.")

        if item == "DescribeResearchEquipment":
            hackprefixlist = ["Net", "Data", "Meta", "Air", "Wire", "Malto", "Dig", "Cyber", "Pixie"]
            hacksuffixlist = ["map", "sploit", "hydra", "shark", "wolf", "fox", "bull", "bear", "wasp", "phoenix", "spider"]
            hacktool = str(str(random.choice(hackprefixlist)) + str(random.choice(hacksuffixlist)))
            doc.append(hacktool + " is John's tool of choice. Able to traverse the deep-web and access information behind almost any barrier, " + hacktool + " is John's personally-coded tool for blackmail discovery.")
            doc.append("And finally!")

        if item == "ASpiesOnB":
            roomlist = ["bedroom",
                        "living room",
                        "bathroom",
                        "kitchen",
                        "cellar",
                        "conservatory",
                        "greenhouse",
                        "garage",
                        "study",
                        "library",
                        "ballroom",
                        "box room",
                        "attic",
                        "games room",
                        "dining room",
                        "hall",
                        "basement"]
            room = str(random.choice(roomlist))
            doc.append("John takes out his equipment, and points it in the direction of Jane's house. He pinpoints onto her " + room + " window.")

        if item == "DescribeSpyingEquipment":
            equipmentlist = ["pair of binoculars", "telescope", "spyglass", "scope", "satellite dish", "laser microphone", "camera", "long-range camera"]
            equipment = str(random.choice(equipmentlist))
            materiallist = ["steel", "titanium", "ivory", "ebony", "glass", "plastic", "osmium", "iridium", "aluminium"]
            material = str(random.choice(materiallist))
            countrylist = ["France", "Italy", "Portugal", "Russia", "Prussia", "Austria", "Australia",
                           "China", "Disneyworld", "England", "Germany", "Japan", "Austria-Hungary",
                           "Yugoslavia", "Czechoslovakia", "Poland", "Israel", "Palestine", "Uzbekistan",
                           "McBekistan", "Skxc8aistan"]
            country = str(random.choice(countrylist))
            doc.append("He's using a " + material + " " + equipment + ", made in " + country + ".")

        if item == "DescribeTortureEquipment":
            bindlist = ["convoluted network of ropes", "wire frame", "set of straps", "specially modified bed",
                        "forcefield generator", "virtual reality device", "hypnosis machine", "brainwasher", "frame"]
            materiallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                            "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass"]
            gaglist = ["rag", "ball-gag", "spider-gag", "ring-gag"]
            bind = str(random.choice(bindlist))
            bindmaterial = str(random.choice(materiallist))
            gagmaterial = str(random.choice(materiallist))
            gag = str(random.choice(gaglist))
            doc.append("John immobilizes Jane, using a " + bind + ", made from " + bindmaterial  + ".")
            doc.append("He then gags her, using a " + gagmaterial + " " + gag + ".")

        if item == "ATorturesB":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            colour = str(random.choice(colourlist))
            torturelist = ["suction caps", "spikes", "knives", "blades", "constricting straps", "electrodes"]
            torture = str(random.choice(torturelist))
            doc.append("John turns on the device, and the " + colour + " " + torture + " work their magic upon her.")

        if item == "BConfesses":
            screamlist = ["screams", "whimpers", "moans", "whines", "wails", "howls", "shrieks"]
            screams = str(random.choice(screamlist))
            movementlist = ["thrashing about", "trying to wriggle out of the device", "trying to escape",
                            "writhing about", "squirming"]
            movement = str(random.choice(movementlist))
            doc.append("Jane " + screams + " through her gag, " + movement + ".")

        if item == "DescribeRomanticEnvironment":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            materiallist = ["tile", "carpet", "wood", "concrete", "cement",
                            "stone", "linoleum", "vinyl"]
            bedmateriallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                               "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass",
                               "mahogany", "marble", "oak", "spruce", "acacia"]
            flowerlist = ["rose", "tulip", "daisy", "violet", "daffodil",
                          "iris", "hyacinth", "chrysantheum"]
            colour = str(random.choice(colourlist))
            colour2 = str(random.choice(colourlist))
            colour3 = str(random.choice(colourlist))
            material = str(random.choice(materiallist))
            bedmaterial = str(random.choice(bedmateriallist))
            flower = str(random.choice(flowerlist))
            doc.append("The apartment has a " + colour + " " + material + " floor, and the walls are painted " + colour2 + ".")
            doc.append("The bedroom has a " + bedmaterial + " bed, with " + colour3 + " " + flower + " petals strewn about it.")

        if item == "VaguelySexualAllusions":
            verblist = ["smothers", "pushs", "whips", "grinds", "rubs", "soaks", "drills", "spreads",
                        "flosses", "brushes", "sniffs", "wraps", "satisfies", "parks in", "rushes",
                        "tempts", "locks", "unlocks", "crawls into", "milks"]
            verb = str(random.choice(verblist))
            nounlist = ["llama", "chicken", "seamstress", "rabbit", "swamp", "goat", "bomb site B",
                        "spoon", "spork", "Disney merchandise", "toothpaste", "furniture",
                        "zoo", "system", "tent", "boat"]
            noun = str(random.choice(nounlist))
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            colour = str(random.choice(colourlist))
            screamlist = ["screams", "howls", "bellows", "cries out", "squeals",
                          "shouts"]
            scream = str(random.choice(screamlist))
            delightlist = ["delight", "pleasure", "joy", "gratification", "relish",
                       "excitement", "bliss", "rapture", "euphoria", "ecstasy",
                       "indulgence", "sybaritism"]
            delight = str(random.choice(delightlist))
            sinlist = ["dark", "wicked", "profane", "blasphemous", "impious",
                       "godless", "base", "sacrilegious", "unspeakable", "atrocious",
                       "diabolical", "fiendish", "degenerate", "depraved"]
            sin = str(random.choice(sinlist))
            doc.append("John " + verb + " her " + colour + " " + noun + ".")
            doc.append("Jane " + scream + " in " + sin + " " + delight + ", and John continues throughout the night...")
            
        if item == "ASeducesB":
            movelist = ["darts over to", "walks to", "saunters to", "wanders to",
                        "strolls to", "drifts to", "lazily walks to", "ambles to"]
            move = str(random.choice(movelist))
            actionlist = ["massages", "kisses", "lightly bites", "licks", "sucks upon"]
            action = str(random.choice(actionlist))
            bodypartlist = ["earlobe", "ear", "neck", "cheek", "lips"]
            bodypart = str(random.choice(bodypartlist))
            doc.append("John " + move + " Jane, and " + action + " her " + bodypart + ".")

        if item == "DescribeSeedyBrothel":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            materiallist = ["tile", "carpet", "wood", "concrete", "cement",
                            "stone", "linoleum", "vinyl"]
            bedmateriallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                               "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass",
                               "mahogany", "marble", "oak", "spruce", "acacia"]
            flowerlist = ["rose", "tulip", "daisy", "violet", "daffodil",
                          "iris", "hyacinth", "chrysantheum"]
            colour = str(random.choice(colourlist))
            colour2 = str(random.choice(colourlist))
            colour3 = str(random.choice(colourlist))
            material = str(random.choice(materiallist))
            bedmaterial = str(random.choice(bedmateriallist))
            flower = str(random.choice(flowerlist))
            doc.append("The brothel has a " + colour + " " + material + " floor, and the walls are painted " + colour2 + ".")
            doc.append("Jane's personal serving-room has a " + bedmaterial + " bed, with " + colour3 + " " + flower + " petals strewn about it.")

        if item == "DescribeProstituteB":
            outfitlist = ["babydoll", "teddy", "dress",
                          "negligee", "nightgown", "minidress",
                          "bikini"]
            materiallist = ["silk", "lace", "cotton",
                            "gauze", "muslin", "flax",
                            "cashmere", "satin"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            outfit = str(random.choice(outfitlist))
            material = str(random.choice(materiallist))
            colour = str(random.choice(colourlist))
            doc.append("Jane is dressed in a " + colour + " " + outfit + " made from " + material + ".")

        if item == "APaysB":
            currencyprefixlist = ["Adamantine", "Elevated", "Emerald", "Golden",
                                  "Imperial", "Indigo", "Planetary", "Perfected",
                                  "Ivory", "Ebony", "Radiant", "Wondrous",
                                  "Prismatic", "Bear", "Marvelous", "Bull"]
            currencysuffixlist = ["Guilder", "Bill", "Quarter", "Piece",
                                  "Note", "Crown", "Ducat", "Sultanate",
                                  "Dollar", "Mark", "Bit", "Nickel", "Hawk"]
            currencyprefix = str(random.choice(currencyprefixlist))
            currencysuffix = str(random.choice(currencysuffixlist))
            currencyname = str(currencyprefix + " " + currencysuffix)
            doc.append("John pays Jane " + str(random.randint(120, 500)) + " " + currencyname + "s.")

        if item == "ABreaksIntoBHouse":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            floormateriallist = ["tile", "carpet", "wood", "concrete", "cement",
                                 "stone", "linoleum", "vinyl"]
            bedmateriallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                               "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass",
                               "mahogany", "marble", "oak", "spruce", "acacia"]
            materiallist = ["steel", "iron", "uranium glass", "lead", "titanium",
                            "ceramic", "iridium", "osmium", "carbon nanotube", "tungsten",
                            "plastic", "glass", "ebony"]
            toollist = ["lockpick", "crowbar", "hammer", "sledgehammer",
                        "hacking PDA"]
            colour = str(random.choice(colourlist))
            colour2 = str(random.choice(colourlist))
            floormaterial = str(random.choice(floormateriallist))
            material = str(random.choice(materiallist))
            tool = str(random.choice(toollist))
            doc.append("John breaks into the apartment with a " + material + " " + tool + ", and looks around.")
            doc.append("The apartment has a " + colour + " " + floormaterial + " floor, and the walls are painted " + colour2 + ".")

        if item == "AStalksIntoBedroom":
            sneaklist = ["sneaks into", "creeps into", "steals into", "slips into",
                         "tiptoes into", "pads into", "prowls into"]
            sneak = str(random.choice(sneaklist))
            doc.append("John " + sneak + " Jane's bedroom.")

        if item == "AIncapacitatesB":
            bindlist = ["convoluted network of ropes", "wire frame", "set of straps", "specially modified bed",
                        "forcefield generator", "virtual reality device", "hypnosis machine", "brainwasher", "frame"]
            materiallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                            "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass"]
            gaglist = ["rag", "ball-gag", "spider-gag", "ring-gag"]
            bind = str(random.choice(bindlist))
            bindmaterial = str(random.choice(materiallist))
            gagmaterial = str(random.choice(materiallist))
            gag = str(random.choice(gaglist))
            doc.append("John immobilizes Jane, using a " + bind + ", made from " + bindmaterial  + ".")
            doc.append("He then gags her, using a " + gagmaterial + " " + gag + ".")

        if item == "AStabsB":
            materiallist = ["steel", "wood", "ivory", "iron",
                            "newspaper", "Damascus stel", "titanium",
                            "aluminium", "chrome", "ceramic"]
            knifelist = ["karambit", "push-dagger", "dagger",
                         "knife", "tactical knife", "trench-knife",
                         "kukri", "ballistic knife", "butterfly knife",
                         "dirk", "machete", "sword", "X-Acto", "spear"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            stablist = ["stabs", "gores", "spears", "transfixes", "impales",
                        "pierces", "punctures", "penetrates", "perforates",
                        "gashes", "wounds", "slashes"]
            material = str(random.choice(materiallist))
            knife = str(random.choice(knifelist))
            colour = str(random.choice(colourlist))
            stab = str(random.choice(stablist))
            doc.append("John pulls out a " + colour + " " + knife + ", made out of " + material + ".")
            doc.append("He " + stab + " Jane with the " + knife + ".")

        if item == "DescribeStab":
            pourlist = ["pours", "streams", "flows", "gushes", "cascades",
                        "spouts", "jets", "spurts", "floods", "surges",
                        "spills", "rushes", "spews"]
            redlist = ["Scarlet", "Red", "Vermilion", "Ruby", "Claret",
                       "Cherry", "Cerise", "Carmine", "Flaming", "Rosy",
                       "Maroon", "Rusty", "Sanguine", "Gules"]
            bloodlist = ["blood", "ichor", "liquid", "fluid"]
            pour = str(random.choice(pourlist))
            red = str(random.choice(redlist))
            blood = str(random.choice(bloodlist))
            doc.append(red + " " + blood + " " + pour + " out from the wound.")

        if item == "AOverpowersB":
            bindlist = ["convoluted network of ropes", "wire frame", "set of straps", "specially modified bed",
                        "forcefield generator", "virtual reality device", "hypnosis machine", "brainwasher", "frame"]
            materiallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                            "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass"]
            bind = str(random.choice(bindlist))
            bindmaterial = str(random.choice(materiallist))
            doc.append("John immobilizes Jane, using a " + bind + ", made from " + bindmaterial  + ".")

        if item == "AStranglesB":
            stranglelist = ["throttles", "chokes", "garrottes", "asphyxiates",
                            "strangles", "strangulates"]
            strangle = str(random.choice(stranglelist))
            doc.append("John " + strangle + " Jane.")

        if item == "DescribeStrangulation":
            bluelist = ["blue", "azure", "sky-blue", "cyan", "turquoise",
                        "purple", "lilac", "magenta", "lavender", "violet"]
            blue = str(random.choice(bluelist))
            doc.append("Her face turns " + blue + ".")

        if item == "ACountsMoney":
            currencyprefixlist = ["Adamantine", "Elevated", "Emerald", "Golden",
                                  "Imperial", "Indigo", "Planetary", "Perfected",
                                  "Ivory", "Ebony", "Radiant", "Wondrous",
                                  "Prismatic", "Bear", "Marvelous", "Bull"]
            currencysuffixlist = ["Guilder", "Bill", "Quarter", "Piece",
                                  "Note", "Crown", "Ducat", "Sultanate",
                                  "Dollar", "Mark", "Bit", "Nickel", "Hawk"]
            currencyprefix = str(random.choice(currencyprefixlist))
            currencysuffix = str(random.choice(currencysuffixlist))
            currencyname = str(currencyprefix + " " + currencysuffix)
            doc.append("John receives " + str(random.randint(120, 500)) + " " + currencyname + "s, and is pleased with his gain.")

        if item == "AInsultsB":
            insult1list = ["artless", "bawdy", "beslubbering", "bootless", "churlish",
                           "cockered", "clouted", "craven", "currish", "dankish",
                           "dissembling", "droning", "errant", "fawning", "fobbing",
                           "froward", "frothy", "gleeking", "goatish", "gorbellied",
                           "impertinent", "knavish", "lewd", "peevish", "pernicious",
                           "rank", "purpled", "queasy", "reeky", "saucy",
                           "sottish", "mangled", "mummering", "loggerheaded", "tottering",
                           "unmuzzled", "vain", "weedy", "yeasty", "burly-boned"]
            insult2list = ["base-court", "bat-fowling", "beef-witted", "clapper-clawed", "clay-brained",
                           "common-kissing", "crook-pated", "doghearted", "dizzy-eyed", "dread-bolted",
                           "earth-vexing", "fen-sucked", "elf-skinned", "fool-born", "full-gorged",
                           "idle-headed", "hell-hated", "hedge-born", "onion-eyed", "rude-growing",
                           "rump-fed", "toad-spotted", "weatherbitten", "scurvy-valiant", "lily-livered",
                           "malmsey-nosed", "tardy-gaited", "spur-galled", "sheep-biting", "rough-hewn"]
            insult3list = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig",
                           "bugbear", "flapdragon", "malt-worm", "ratsbane", "scut",
                           "clotpole", "flax-wench", "measle", "vassal", "whey-face",
                           "clack-dish", "hedge-pig", "mammet", "knave", "schmuck",
                           "codpiece", "hugger-mugger", "nut-hook", "fool", "jolt-head",
                           "dewberry", "lout", "maggot-pie", "pigeon-egg", "devil-monk"]
            insult1 = str(random.choice(insult1list))
            insult2 = str(random.choice(insult2list))
            insult3 = str(random.choice(insult3list))
            doc.append("He then insults her - 'By God, aren't you a " + insult1 + " " + insult2 + " " + insult3 + "?")

        if item == "ATalksToB":
            greetinglist = ["Hello", "Good morning", "Good afternoon", "Good evening", "Good pre-evening", "Good pre-noon"]
            greeting = str(random.choice(greetinglist))
            doc.append("John walks into Jane's apartment, and says '" + greeting + "' to her.")

        if item == "ASuggestsSuicideToB":
            suicidelist = ["kill yourself", "off yourself", "commit suicide",
                           "end it all", "take your own life", "die by your own hand"]
            suicide = str(random.choice(suicidelist))
            doc.append("You know, Jane, maybe you should just " + suicide + ".'")

        if item == "BAgreesWithA":
            rightlist = ["right", "correct", "true", "veracious",
                         "precise", "unerring", "faultless", "flawless",
                         "error-free", "on the right track", "along the right lines",
                         "on the mark", "on the nail", "spot on", "on the money"]
            right = str(random.choice(rightlist))
            considerlist = ["thinks about", "contemplates", "reflects upon", "appraises",
                            "reviews", "mulls over", "ruminates over", "assesses",
                            "evaluates", "weighs up"]
            consider = str(random.choice(considerlist))
            doc.append("In fact, the more she " + consider + " his argument, the more she realizes it was almost certainly " + right + ", and resigns herself.")

        if item == "BConsidersSuicide":
            rightlist = ["right", "correct", "true", "veracious",
                         "precise", "unerring", "faultless", "flawless",
                         "error-free", "on the right track", "along the right lines",
                         "on the mark", "on the nail", "spot on", "on the money"]
            right = str(random.choice(rightlist))
            doc.append("Maybe his argument was " + right + ", Jane thinks.")

        if item == "BCommitsSuicide":
            guntypelist = ["Taurus Judge", "Chiappa Rhino", "Ruger LCR",
                           "Ruger Alaskan", "Smith & Wesson Model 500", "Smith & Wesson Model 340PD",
                           "Taurus Model 608", "OTs-20 Gnom", "U-94 Udar", "Ruger Vaquero",
                           "MP-412 REX", "Colt Anaconda", "Manurhin MR 73", "Charter Arms Bulldog"]
            guntype = str(random.choice(guntypelist))
            pinklist = ["Pink", "Rosy", "Salmon", "Shell-pink", "Rouge",
                        "Strawberry", "Coral", "Taffy", "Bubblegum", "Pale pink"]
            pink = str(random.choice(pinklist))
            chunklist = ["chunk", "lump", "bit", "masse", "gob"]
            chunk = str(random.choice(chunklist))
            spatterlist = ["spatter across", "bespatter", "moisten", "soak", "spatter",
                           "douse", "drench", "slosh across", "spray"]
            spatter = str(random.choice(spatterlist))
            redlist = ["scarlet", "red", "vermilion", "ruby", "claret",
                       "cherry", "cerise", "carmine", "flaming", "rosy",
                       "maroon", "rusty", "sanguine", "gules"]
            red = str(random.choice(redlist))
            bloodlist = ["blood", "ichor", "liquid", "fluid"]
            blood = str(random.choice(bloodlist))
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            colour = str(random.choice(colourlist))
            doc.append("Jane pulls out a revolver - a " + guntype + " - and puts it against her head.")
            doc.append("She squeezes the trigger, until BLAM!")
            doc.append(pink + " " + chunk + "s " + spatter + " the " + colour + " walls, and " + red + " " + blood + " pools upon the floor.")

        if item == "BInAlley":
            waitlist = ["walking", "strolling", "trudging",
                        "striding"]
            wait = str(random.choice(waitlist))
            doc.append("Jane was " + wait + " past a dark alley.")

        if item == "DescribeSeedyAlley":
            seedylist = ["sordid", "disreputable", "seamy", "sleazy",
                         "corrupt", "rough", "nasty", "unpleasant",
                         "unwholesome", "seedy"]
            dingylist = ["dilapidated", "derelict", "ruinous", "decrepit",
                         "broken-down", "crumbling", "decaying", "disintegrating",
                         "gloomy", "drab", "dark", "dull", "dim", "dismal", "sombre",
                         "grim", "dreary", "cheerless", "dirty", "grimy", "shabby",
                         "run-down"]
            placelist = ["speakeasy", "bordello", "black market", "cult", "opium den"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            leaklist = ["leaks", "escapes", "oozes out", "exudes", "emanates", "issues out"]
            seedy = str(random.choice(seedylist))
            dingy = str(random.choice(dingylist))
            dingy2 = str(random.choice(dingylist))
            place = str(random.choice(placelist))
            colour = str(random.choice(colourlist))
            leak = str(random.choice(leaklist))
            doc.append("It is " + dingy + " and " + dingy2 + ", with a " + seedy + " " + place + " hidden behind a secretive door.")
            doc.append("Smoke " + leak + " out of a crack in the door, and it is possible to see " + colour + " walls inside the building.")

        if item == "AStepsOutOfShadows":
            surpriselist = ["surprising Jane", "taking Jane by surprise", "catching Jane off-guard"]
            surprise = str(random.choice(surpriselist))
            shadowlist = ["shadows", "shade", "darkness", "dimness",
                          "murk", "gloom", "gloominess", "tenebrosity", "umbrage"]
            shadow = str(random.choice(shadowlist))
            doc.append("John steps out of the " + shadow + ", " + surprise + ".")

        if item == "AThreatensWithRevolver":
            guntypelist = ["Taurus Judge", "Chiappa Rhino", "Ruger LCR",
                           "Ruger Alaskan", "Smith & Wesson Model 500", "Smith & Wesson Model 340PD",
                           "Taurus Model 608", "OTs-20 Gnom", "U-94 Udar", "Ruger Vaquero",
                           "MP-412 REX", "Colt Anaconda", "Manurhin MR 73", "Charter Arms Bulldog"]
            nudgelist = ["nudges", "jabs", "pokes", "taps", "prods"]
            commandlist = ["commands", "orders", "instructs", "directs"]
            guntype = str(random.choice(guntypelist))
            nudge = str(random.choice(nudgelist))
            command = str(random.choice(commandlist))
            doc.append("He " + nudge + " her with an illegally bought revolver, a " + guntype + ".")
            doc.append("He " + command + " Jane to give him his money.")

        if item == "BGivesMoney":
            shakelist = ["Shaking", "Trembling", "Quivering", "Quaking", "Shuddering",
                         "Wobbling", "Swaying"]
            walletlist = ["wallet", "purse", "pouch", "billfold", "pocketbook", "pochette"]
            shake = str(random.choice(shakelist))
            wallet = str(random.choice(walletlist))
            doc.append(shake + " with fear, she hands him her " + wallet + ".")

        if item == "BEscapes":
            escapelist = ["gets away", "gets out", "bolts", "makes a break for it", "flees",
                          "escapes", "runs for it", "slips away", "steals away", "scarpers off",
                          "vamooses", "legs it"]
            escape = str(random.choice(escapelist))
            doc.append("She takes her change and " + escape + ", thankful that she survived.")            
            
        if item == "DescribeScam":
            emailaddressprefixlist = ["fox","wolf","dog","dragon","cat",
                                      "tiger","skunk","horse","coyote","rat",
                                      "lion","rabbit","otter","cheetah","eagle",
                                      "raccoon","bear","bull","hyena","kangaroo",
                                      "gryphon","leopard","lynx","ferret","squirrel",
                                      "panther","mouse","bat","snail","deer"]
            emailendinglist = [".com", ".net", ".org", ".club", ".pizza", ".int", ".mil", ".academy",
                               ".accountant", ".adult", ".apartments", ".deepweb", ".app", ".io",
                               ".audio", ".beer", ".scotchwhisky", ".whisky", ".wine", ".best",
                               ".blue", ".red", ".orange", ".yellow", ".green", ".cyan", ".purple",
                               ".white", ".black", ".gray", ".build", ".post", ".criminal", ".probablyillegal",
                               ".social", ".sucks", ".landica"]
            emailproviderlist = ["amail", "bmail", "cmail", "dmail", "fmail",
                                 "hmail", "imail", "jmail", "kmail", "mmail",
                                 "nmail", "omail", "pmail", "chainmail", "qmail",
                                 "rmail", "smail", "tmail", "umail", "vmail",
                                 "wmail", "xmail", "ymail", "zmail", "jesuschrist"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            titlelist = ["Doctor", "Barrister", "Minister"]
            firstnamelist = ["James", "Ken", "Mike", "Jamie"]
            surnamelist = ["Bankole", "Smith", "Bonganti", "Okon"]
            subjectlinelist = ["URGENT", "TREAT AS URGENT", "CONFIDENTIAL", "important and confidential",
                               "dearest friend"]
            monthlist = ["January", "February", "March", "April", "May", "June",
                         "July", "August", "September", "October", "November", "December"]
            deathlist = ["involved in a plane crash on their way home from their holidays and were among the 111 people confirmed dead",
                         "in a car crash on the main road from Lagos to Kaduna (they died)",
                         "contracted a deadly disease and died",
                         "involved in bomb blast here in my country",
                         "killed by Prince Yomi Johnson when the Ecomog soldiers came in",
                         "kidnapped and taken away by unidentified gunmen from their home in Kaduna"]
            banklist = ["Plunder & Flee Incorporated", "Santi Manilo Bank", "United Bank of Trust", "Disney Bank",
                        "Intercontinental Bank PLC"]
            materiallist = ["leather", "hemp", "cotton", "aluminium", "steel", "titanium", "ivory",
                            "ebony", "rubber", "glass", "plastic", "osmium", "iridium", "uranium glass", "flax"]
            moneylist = ["1350", "10983", "528", "1598", "253", "263", "169", "1579", "712", "666"]
            emailaddress = str(random.choice(colourlist) + random.choice(emailaddressprefixlist) + str(random.randint(10,1000)))
            emailprovider = str(random.choice(emailproviderlist))
            emailending = str(random.choice(emailendinglist))
            email = str(emailaddress + "@" + emailprovider + emailending)
            title = str(random.choice(titlelist))
            firstname = str(random.choice(firstnamelist))
            lastname = str(random.choice(surnamelist))
            subjectline = str(random.choice(subjectlinelist))
            day = str(str(random.randint(1, 32)) + "th")
            month = str(random.choice(monthlist))
            year = str("19" + str(random.randint(13, 99)))
            death = str(random.choice(deathlist))
            bank = str(random.choice(banklist))
            money = str(random.choice(moneylist))
            material = str(random.choice(materiallist))
            doc.append("John had a plan to make some money - illegal money, but money nonetheless.")
            doc.append("He sends an email using an illegal email address to a victim, hoping she will take the bait.")
            doc.append("\n\n")
            doc.append("SUBJECT LINE: " + subjectline)
            doc.append("FROM: " + firstname + " " + lastname + "[" + email + "]")
            doc.append("\n")
            doc.append("I am " + title + " " + firstname + " " + lastname + ".")
            doc.append("I am the personal attorney to Mr. Tony, a national of your country, who used to work with the Shell Oil Producing Company")
            doc.append("Herein after he will be referred to as my client.")
            doc.append("On the day of " + day + " of " + month + ", " + year + ", my client and his wife and their only daughter were " + death + ".")
            doc.append("\n")
            doc.append("Since then I have made several inquiries to your embassy here to locate any of my client's extended relatives, Which has also proved abbortive.")
            doc.append("After these unsuccessful attempts, I decided contact you since you have the same last name.")
            doc.append("I have contacted you to assist in repatriating the fund valued at " + money + " tonnes of " + material + " Left behind by my client before it get confiscated or declared unservicable by " + bank + ", where this huge amount was deposited.")
            doc.append("\n")
            doc.append("What bothers me most is the fund, which according to my country's constitution becomes the governments own, if there is no-one close to the deceased to claim the funds.")
            doc.append(bank + " have issued me a notice to provide a next of kin or have the account confiscated in the next one month.")
            doc.append("For the fact that I have been unsuccessful in locating any relatives of my late client since then, I hereby seek your consent to present yuo as the next-of-kin to the deceased so that the proceeds of this account can be paid to you.")
            doc.append("Therefore, on receipt of your positive response, we shall then discuss the percentage that is comming to me after the money has been credited and the modalities for sharing is as follows: " + str(random.randint(13, 49)) + "% to me, and the rest to you.")
            doc.append("\n")
            doc.append("I can assist in procuring the necessary information and legal documents that may be needed to actualise this proposal.")
            doc.append("All I requrie from you is your honest coo-peration to enable us see this transaction through.")
            doc.append("I guarnatee this will be executted under a legitimate platform that will protect you from any breach of law.")
            doc.append("\n")
            doc.append("I look forward to hear from you soonest.")
            doc.append("Please note that this transaction must remain confidential at all times.")
            doc.append("Regards, " + title + " " + firstname + " " + lastname)
            doc.append("\n\n")

        if item == "BScammedByA":
            trustlist = ["trustworthy", "reliable", "dependable", "honest", "honourable",
                         "full of integrity", "worthy of her trust", "upright", "ethical",
                         "virtuous", "incorruptible", "above suspicion", "responsible"]
            trust = str(random.choice(trustlist))
            doc.append("Jane thinks that this guy is really " + trust + ", and sends him some money.")

        if item == "DescribeBlackMarket":
            seedylist = ["sordid", "disreputable", "seamy", "sleazy",
                         "corrupt", "rough", "nasty", "unpleasant",
                         "unwholesome", "seedy"]
            dingylist = ["dilapidated", "derelict", "ruinous", "decrepit",
                         "broken-down", "crumbling", "decaying", "disintegrating",
                         "gloomy", "drab", "dark", "dull", "dim", "dismal", "sombre",
                         "grim", "dreary", "cheerless", "dirty", "grimy", "shabby",
                         "run-down"]
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            leaklist = ["leaks", "escapes", "oozes out", "exudes", "emanates", "issues out"]
            multicolourlist = ["kaleidoscopic", "psychedelic", "highly colourful", "multicolour",
                               "many-hued", "many-coloured", "like a rainbow", "varicoloured",
                               "technicolour", "prismatic", "polychromatic"]
            thicklist = ["thick", "dense", "heavy", "opaque", "soupy",
                         "murky", "smoggy"]
            vapourlist = ["smoke", "smog", "vapour", "haze"]
            seedy = str(random.choice(seedylist))
            dingy = str(random.choice(dingylist))
            dingy2 = str(random.choice(dingylist))
            colour = str(random.choice(colourlist))
            leak = str(random.choice(leaklist))
            multicolour = str(random.choice(multicolourlist))
            thick = str(random.choice(thicklist))
            vapour = str(random.choice(vapourlist))
            doc.append("It is " + dingy + " and " + dingy2 + ", with a " + seedy + " black market hidden behind a secretive door.")
            doc.append("Smoke " + leak + " out of a crack in the door, and it is possible to see light emanating from inside the building.")
            doc.append("Jane enters the black market through the wooden door.")
            doc.append("Inside, it is filled with " + multicolour + " stalls, with " + thick + " " + vapour + " swirling about in the air.")
                
        if item == "DescribeCounterfeits":
            itemlist = ["knife", "pen", "fountain pen", "purse", "wallet",
                        "cigarettes", "smartphone", "shoes", "watch", "pair of earrings",
                        "handbag", "pipe", "snuff tobacco bottle", "cigar"]
            brandlist = ["Cartier", "Montblanc", "Rolex", "Prada",
                         "Mercedes-Benz", "Gucci", "Chanel", "Versace", "Disney"]
            item = str(random.choice(itemlist))
            brand = str(random.choice(brandlist))
            doc.append("John (the merchant of this particular stall) shows her exactly what she's looking for - a counterfeit " + item + " made by " + brand + ".")

        if item == "ASellingCounterfeits":
            colourlist = ["scarlet", "red", "crimson",
                          "orange", "apricot", "peach",
                          "cream", "yellow", "blonde",
                          "green", "mint", "emerald",
                          "cyan", "aquamarine", "teal",
                          "blue", "cobalt", "azure",
                          "purple", "lilac", "mauve",
                          "pink", "rose", "salmon"]
            fabriclist = ["cotton", "wool", "polyester", "rayon", "denim",
                          "double gauze", "silk", "satin", "linen", "flannel"]
            woodlist = ["oak", "maple", "mahogany", "walnut", "rosewood", "teak", "spruce",
                        "pine", "ash", "hickory", "beech", "birch", "cedar", "redwood"]
            colour = str(random.choice(colourlist))
            fabric = str(random.choice(fabriclist))
            wood = str(random.choice(woodlist))
            doc.append("Jane wanders around the black market, until she comes upon a stall, made from " + wood + " and covered with " + colour + " " + fabric + ".")
                    
        if item == "BBuysCounterfeits":
            buylist = ["buys", "purchases", "acquires", "obtains", "procures"]
            buy = str(random.choice(buylist))
            doc.append("Jane " + buy + " the item, and navigates around the black market until she finds the exit, leaving.")

        
    doc.generate_tex(filepath="Crime Write")  


