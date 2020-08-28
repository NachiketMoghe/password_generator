import string
import random
class Characters:
    def __init__(self, symb, numb):
        self.symb = symb
        self.numb=numb

    def capital_alphabets(self):
        capital= list(string.ascii_uppercase)
        return capital

    def small_alphabets(self):
        small= list(string.ascii_lowercase)
        return small

    def numbers(self):
        numb=self.numb 
        return numb.split(" ")

    def symbols(self):
        symb = self.symb
        return symb.split(" ")


class passwords:
    def gen_pass(self):
        nums="1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6" 
        sign="! @ # $ % ^ & * ( ) _ + [ { ] } : ; ' ' / > , <"
        char =Characters(nums, sign)
        caps= char.capital_alphabets()
        low= char.small_alphabets()
        num=char.numbers()
        sym=char.symbols()

        characters = [caps, low, num, sym]
        password= ""
        for length in range(10):
            i1 = int(random.uniform(0,4))
            i2 = int(random.uniform(0,26))
            character=characters[i1][i2]
            password+= str(character)
        return password

def main():
    ps = passwords()
    password = ps.gen_pass()
    return password

