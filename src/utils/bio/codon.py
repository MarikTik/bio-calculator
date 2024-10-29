from typing import Union, Dict

class Codon:
     def __init__(self, codon: str):
          self.codon = codon.lower()

     def __eq__(self, other: Union['Codon', str]) -> bool:
          if isinstance(other, str):
               return codon_to_amino_acid[self.codon] == codon_to_amino_acid[other.lower()]
          elif isinstance(other, Codon):
               return self.__eq__(other.codon)
          raise TypeError(f"Cannot compare Codon with {type(other)}")
     
     def __ne__(self, value: Union['Codon', str]) -> bool:
          return not self.__eq__(value)

     def __hash__(self) -> int:
          return hash(codon_to_amino_acid[self.codon])
     
     def __str__(self) -> str:
          return self.codon.upper()
     
     def __repr__(self) -> str:
          return self.codon
     
     def __lt__(self, other: 'Codon') -> bool:
          return self.codon < other.codon
     @staticmethod
     def codons_count_map(gene: str) -> Dict['Codon', int]:
          triplets = [gene[i:i+3] for i in range(0, len(gene) - 2)]
          
          codon_map = dict()
          for triplet in triplets:
               triplet = triplet.lower().strip()
               if triplet in codon_to_amino_acid:
                    codon = Codon(triplet)
                    if codon in codon_map:
                         codon_map[codon] += 1
                    else:
                         codon_map[codon] = 1
          return codon_map

codon_associations = {
    ("ttt", "ttc"): "Phenylalanine (Phe)",
    ("tta", "ttg"): "Leucine (Leu)",
    ("att", "atc", "ata"): "Isoleucine (Ile)",
    ("atg",): "Methionine (Met)", 
    ("gtt", "gtc", "gta", "gtg"): "Valine (Val)",
    ("tct", "tcc", "tca", "tcg"): "Serine (Ser)",
    ("cct", "ccc", "cca", "ccg"): "Proline (Pro)",
    ("act", "acc", "aca", "acg"): "Threonine (Thr)",
    ("gct", "gcc", "gca", "gcg"): "Alanine (Ala)",
    ("tgg",): "Tryptophan (Trp)",
    ("cgt", "cgc", "cga", "cgg"): "Arginine (Arg)"
}

 
codon_to_amino_acid = {
    codon: name
    for codons, name in codon_associations.items()
    for codon in codons
}

