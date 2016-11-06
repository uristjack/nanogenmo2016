import random
from compiler.ast import flatten
import storygen

# Replace events with structures of sentences. These will be turned into sentences in a sentence generator
# ALLCAPS are for titles, not sentences - they are for LaTeX

introduce = ["INTRO_TITLE", "DescribeDay","DescribeA", "DescribeB", "DescribeMultiverse"] # First character = A, 2nd = B
convalesce = ["CONCLUSION_TITLE", "FindOutNextEpisode"]

bobtree = []

threatened = ["NEW_PARAGRAPH_THREATENED", "APullsOutGun", "DescribeGun", "AThreatensB"]
willbyrevolver = ["BAcquiesces"]

blackmailed = ["NEW_PARAGRAPH_BLACKMAIL", "APullsOutBlackmail", "DescribeBlackmail", "ABlackmailsB"]
willbyblackmail = ["BAcquiesces"]

drugged = ["NEW_PARAGRAPH_DRUGGED", "APullsOutDrug", "DescribeDrug", "ADrugsB"]
willbydrugs = ["DescribeEffectedB"]

spiedupon = ["NEW_PARAGRAPH_SPIEDUPON", "ASpiesOnB", "DescribeSpyingEquipment"]
secretbyspy = ["DescribeBSecret"] # I want these secrets to be a mish-mash of random stuff, based on your average Tumblrina - pyrogender, triform etc.

extorted = ["NEW_PARAGRAPH_EXTORTED", "ATorturesB", "DescribeTortureEquipment"]
secretbyextortion = ["BConfesses"]

abused = ["NEW_PARAGRAPH_ABUSED", "AResearchsB", "DescribeResearchEquipment"]
secretbyabuse = ["DescribeBSecret"]

seduced = ["NEW_PARAGRAPH_SEDUCED", "DescribeRomanticEnvironment", "ASeducesB"]
sexualseduction = ["VaguelySexualAllusions"]

favourbought = ["NEW_PARAGRAPH_PROSTITUTION", "DescribeSeedyBrothel", "DescribeProstituteB", "APaysB", "VaguelySexualAllusions"]

raped = ["NEW_PARAGRAPH_RAPE", "ABreaksIntoBHouse", "AStalksIntoBedroom", "AIncapacitatesB", "VaguelySexualAllusions", "DescribeBImpact"]

strangled = ["NEW_PARAGRAPH_STRANGLED", "AOverpowersB", "AStranglesB"]
deathbystrangle = ["DescribeStrangulation"]

stabbed = ["NEW_PARAGRAPH_STABBED", "AOverpowersB", "AStabsB"]
deathbystab = ["DescribeStab"]

inducesuicide = ["NEW_PARAGRAPH_SUICIDE", "ATalksToB", "AInsultsB", "ASuggestsSuicideToB"]
considersuicide = ["BConsidersSuicide", "BAgreesWithA"]
deathbysuicide = ["BCommitsSuicide"] # Commits suicide via revolver gunshot.

muggedwithrevolver = ["NEW_PARAGRAPH_MUGGED", "BInAlley", "DescribeSeedyAlley", "AStepsOutOfShadows", "AThreatensWithRevolver"]
moneybyrevolver = ["BGivesMoney", "BEscapes", "ACountsMugMoney"]

scamdescription = ["NEW_PARAGRAPH_SCAM", "DescribeScam"]
scammed = ["BScammedByA"]
moneybyscam = ["AReceivesMoneyFromScam", "ACountsScamMoney"] 

counterfeit = ["NEW_PARAGRAPH_COUNTERFEIT", "DescribeBlackMarket", "ASellingCounterfeits", "DescribeCounterfeits"]
moneybycounterfeit = ["BBuysCounterfeits", "ACountsCounterfeitMoney"]



def rearrange(tree):
    tree[0] = introduce
    tree[-1] = convalesce
    for (i, item) in enumerate(tree):
        if item == 'CharacterThreatenedWithRevolver':
            tree[i] = threatened
        if item == 'WillAppropriatedByRevolver':
            tree[i] = willbyrevolver
        if item == 'CharacterBlackmailed':
            tree[i] = blackmailed
        if item == 'WillAppropriatedByBlackmail':
            tree[i] = willbyblackmail
        if item == 'CharacterDrugged':
            tree[i] = drugged
        if item == 'WillAppropriatedByDrugs':
            tree[i] = willbydrugs
        if item == 'CharacterSpiedUpon':
            tree[i] = spiedupon
        if item == 'SecretAppropriatedByVoyeur':
            tree[i] = secretbyspy
        if item == 'CharacterBrutallyExtorted':
            tree[i] = extorted
        if item == 'SecretAppropriatedByExtortion':
            tree[i] = secretbyextortion
        if item == 'CharacterConfidenceAbused':
            tree[i] = abused
        if item == 'SecretAppropriatedByAbuse':
            tree[i] = secretbyabuse
        if item == 'CharacterSeduced':
            tree[i] = seduced
        if item == 'SexAppropriated':
            tree[i] = sexualseduction
        if item == 'SexualFavourBought':
            tree[i] = favourbought
        if item == 'CharacterRaped':
            tree[i] = raped
        if item == 'CharacterStrangled':
            tree[i] = strangled
        if item == 'CharacterDiesToStrangle':
            tree[i] = deathbystrangle
        if item == 'CharacterStabbed':
            tree[i] = stabbed
        if item == 'CharacterDiesToStab':
            tree[i] = deathbystab
        if item == 'CharacterInducedToSuicide':
            tree[i] = inducesuicide
        if item == 'CharacterConsidersSuicide':
            tree[i] = considersuicide
        if item == 'CharacterCommitsSuicide':
            tree[i] = deathbysuicide
        if item == 'CharacterMuggedWithRevolver':
            tree[i] = muggedwithrevolver
        if item == 'MoneyAppropriatedByRevolver':
            tree[i] = moneybyrevolver
        if item == 'DescribeScam':
            tree[i] = scamdescription
        if item == 'CharacterScams':
            tree[i] = scammed
        if item == 'MoneyAppropriatedByScam':
            tree[i] = moneybyscam
        if item == 'CharacterSellsCounterfeitsOnBlackMarket':
            tree[i] = counterfeit
        if item == 'MoneyAppropriatedByCounterfeit':
            tree[i] = moneybycounterfeit
        
def eventgen(x):
    storygen.plotgen(x)
    global bobtree
    bobtree = storygen.storytree
    rearrange(bobtree)
    bobtree = flatten(bobtree)
    print(bobtree)

"""
                def plotgen(x):
                    global storytree
                    for i in range(x):
                        PlotComplicate(storytree)
                        storytree = list(flatten(storytree))
                    RemoveAsterisks(storytree)
                    RemoveAsterisks(storytree)
                    print(storytree)
                """
