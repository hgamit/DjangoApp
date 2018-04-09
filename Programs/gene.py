def hasvalidsub(seq):
    
    if(len(seq)>6):
        a = ['TAG', 'TAA', 'TGA']
    
        if any(x in seq[3:len(seq)-3] for x in a):
            print ("Since, It has intervening stop codons.", end='')
            return False
    
        return True
    
    else:
         return True

def hasvalidstart(seq):
    if(seq.startswith('ATG')):
        return True
    else:
        print("Since, It doesn't have valid start.", end='')
        return False

def hasvalidend(seq):
    if(seq.endswith(('TAG', 'TAA', 'TGA'))):
        return True
    else:
        print("Since, It doesn't have valid end.", end='')
        return False

def ismultiple(seq):
    if(len(seq)%3==0):
        return True
    else:
        print("Since, It doesn't have valid length(multiple of 3).", end='')
        return False

def isgene(seq):
    if(hasvalidstart(seq) and ismultiple(seq) and hasvalidend(seq) and hasvalidsub(seq)):
        return True
    else:
        return False

def is_valid_DNA(seq):
    validchar = set('ACGT')
    if(set(seq)<=validchar):
        if(isgene(seq)):
            print("This DNA is a potential gene.")
        else:
            print("This DNA is NOT a potential gene.")
    else:
        print ("Not valid DNA")


seq = input("ENTER DNA CODE: ")
is_valid_DNA(seq)