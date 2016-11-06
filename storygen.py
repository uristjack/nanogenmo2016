import random
from compiler.ast import flatten

"""
This program is part 1 of uristjack's Story Writer for NaNoGenMo, and for my CAS hours.
This is as per the structure of:
    https://gist.github.com/cpressey/6324fff6ef0dfdf69b96
This module treats the story structure as a tree, denoted as a list of lists.
It then complicates the tree, making the plot more complicated.

Licensed under the GNU General Public License, Version 3 by Julian Ferrone, 2016.
"""


# Initial storytree
storytree = ["IntroduceCharacters", "*", "CharactersConvalesce"]

# Let's get some crimes sorted!

# The Appropriation of Will Crimes
threaten = ["*", "CharacterThreatenedWithRevolver", "WillAppropriatedByRevolver", "*"]
blackmail = ["*", "CharacterBlackmailed", "WillAppropriatedByBlackmail", "*"]
drug = ["*", "CharacterDrugged", "WillAppropriatedByDrugs", "*"]

# The Secret Appropriation Stuff.
spyupon = ["CharacterSpiedUpon", "SecretAppropriatedByVoyeur", "*", "*"]
extort = ["CharacterBrutallyExtorted", "SecretAppropriatedByExtortion", "*", "*"]
confidenceabuse = ["CharacterConfidenceAbused", "SecretAppropriatedByAbuse", "*", "*"]

# The Sexual Appropriation actions
seduce = ["*", "CharacterSeduced", "SexAppropriated", "*"]
buyfavour = ["*", "SexualFavourBought", "*"]
rape = ["*", "CharacterRaped", "*"]

# Murder!
strangle = ["CharacterStrangled", "CharacterDiesToStrangle", "*"]
stab = ["CharacterStabbed", "CharacterDiesToStab", "*"]
inducesuicide = ["CharacterInducedToSuicide", "CharacterConsidersSuicide", "CharacterCommitsSuicide", "*", "*"]

# Possession is 0.9 of the law
mug = ["*","CharacterMuggedWithRevolver", "MoneyAppropriatedByRevolver", "*"]
scam = ["*", "DescribeScam", "CharacterScams", "MoneyAppropriatedByScam", "*"]
counterfeit = ["CharacterSellsCounterfeitsOnBlackMarket", "MoneyAppropriatedByCounterfeit", "*", "*"]



crimebox = [threaten,
            blackmail,
            drug,
            spyupon,
            extort,
            confidenceabuse,
            seduce,
            buyfavour,
            rape,
            strangle,
            stab,
            inducesuicide,
            mug,
            scam,
            counterfeit]


result = []

# Let's complicate the tree!
def PlotComplicate(tree):
    for (i, item) in enumerate(tree):
        if item == '*':
            tree[i] = random.sample(crimebox, 1)

# Remove the asterisks from the plot tree once done.
def RemoveAsterisks(tree):
    for (i, item) in enumerate(tree):
        if item == '*':
            del tree[i]

def plotgen(x):
    global storytree
    for i in range(x):
        PlotComplicate(storytree)
        storytree = list(flatten(storytree))
    RemoveAsterisks(storytree)
    RemoveAsterisks(storytree)
"""
if __name__ == "__main__":
    plotgen(10)
"""
