class Alignment():

    #class variables. Sollten entsprechend nicht geaendert werden in den Instanzen

    lawful = 1;
    neutral = 0;
    chaotic = -1;

    good = 1;
    #neutral =0; Das selbe wie oben
    evil = -1;

    def __init__(self, tradition, moral):
        self.alignment = (tradition,moral)

    def isLawful(self):
        return self.alignment[0] == Alignment.lawful

    def isChaotic(self):
        return self.alignment[0] == Alignment.chaotic

    def isGood(self):
        return self.alignment[1] == Alignment.good

    def isEvil(self):
        return self.alignment[1] == Alignment.evil

    # Allgemein die Differenz der Alignment
    def differenceTo(self, deity_alignment):
        #tradition alignment differenz
        difference = abs(self.alignment[0]-deity_alignment.alignment[0])
        #moral alignment differenz
        difference += abs(self.alignment[1]-deity_alignment.alignment[1])
        return difference

    # Vereinfachter Alignment-Test, d.h ob ein Char im Alignment der Deity ist
    def inDeitiesAlignment(self, deity_alignment):
        return (self.differenceTo(deity_alignment)<=1)


#Einfach nur Test; wird ja eh nie aufgerufen außer beim direkten Aufruf
if __name__ == "__main__":
    test = Alignment(Alignment.lawful, Alignment.good)

    deity_test1 = Alignment(Alignment.lawful, Alignment.good)   #True
    deity_test2 = Alignment(Alignment.chaotic, Alignment.good)  #False
    deity_test3 = Alignment(Alignment.neutral, Alignment.good)  #True
    deity_test4 = Alignment(Alignment.neutral, Alignment.neutral)#False
    deity_test5 = Alignment(Alignment.chaotic, Alignment.evil)   #False

    print(test.differenceTo(deity_test1), end=" ")
    print(str(test.inDeitiesAlignment(deity_test1)))

    print(test.differenceTo(deity_test2), end=" ")
    print(str(test.inDeitiesAlignment(deity_test2)))

    print(test.differenceTo(deity_test3), end=" ")
    print(str(test.inDeitiesAlignment(deity_test3)))

    print(test.differenceTo(deity_test4), end=" ")
    print(str(test.inDeitiesAlignment(deity_test4)))

    print(test.differenceTo(deity_test5), end=" ")
    print(str(test.inDeitiesAlignment(deity_test5)))

    print("Is Lawful: " +str(test.isLawful()) )
    print("Is Chaotic: " +str(test.isChaotic()))
    print("Is Deity2 Chaotic: "+ str(deity_test2.isChaotic()))
