def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1
    return freq


Reverse:
def Reverse(Pattern):
    z = ''
    for char in Pattern:
        z = char + z
    return z


Complete:
def Complement(Pattern):
    comp = ""
    for char in Pattern:
        if char == "A":
            char = char.replace("A","T")
        elif char == "C":
            char = char.replace("C","G")
        elif char == "G":
            char = char.replace("G","C")
        elif char == "T":
            char = char.replace("T","A")
        comp += char
    return comp

Reverse complete:
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern
def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev
def Complement(Pattern):
    comp = ""
    for char in Pattern:
        if char == "A":
            char = char.replace("A","T")
        elif char == "C":
            char = char.replace("C","G")
        elif char == "G":
            char = char.replace("G","C")
        elif char == "T":
            char = char.replace("T","A")
        comp = comp + char
    return comp

Find place of the pattern in the gene:
def PatternMatching(Pattern, Genome):

    positions = [] #create a list called positions   

    Pattern_length = len(Pattern)  #create a variable that is the length of the pattern. E.G., “2”
    Genome_length = len(Genome) #create a variable that is the length of the genome  E.G., “10”

    for i in range(Genome_length - Pattern_length + 1): #setting up range to search for pattern
        if Genome[i:i + Pattern_length] == Pattern:  #E.G., if the positions of 0 up to but not including (0 + 2) = the pattern we're looking for,
            positions.append(i)   #then add the position "0" to the list we created called positions

    return positions     #return the positions list that show all the starting positions of the pattern in the genome

