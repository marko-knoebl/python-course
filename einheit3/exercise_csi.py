dna_code = open('dna.txt').read()

black_hair = 'CCAGCAATCGC'
brown_hair = 'GCCAGTGCCG'
carrot_hair = 'TTAGCTATCGC'

square_face = 'GCCACGG'
round_face = 'ACCACAA'
oval_face = 'AGGCCTCA'

if dna_code.find(black_hair) != -1:
    hair = 'black'
elif dna_code.find(brown_hair) != -1:
    hair = 'brown'
elif dna_code.find(carrot_hair) != -1:
    hair = 'orange'
print hair + ' hair'

if dna_code.find(square_face) != -1:
    print 'square face'
    face = 'square'
elif dna_code.find(round_face) != -1:
    print 'round face'
    face = 'round'
elif dna_code.find(oval_face) != -1:
    print 'oval face'
    face = 'oval'

if hair == 'orange' and face == 'round':
    print "It's Ziga"
if hair == 'black' and face == 'oval':
    print "It's Matej"
if hair == 'brown' and face == 'square':
    print "It's Miha"

