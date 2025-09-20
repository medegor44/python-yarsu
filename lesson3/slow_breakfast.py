import time

def make_breakfast():
    make_fried_eggs()
    make_sandwich()
    make_coffee()

def make_fried_eggs():
    time.sleep(2)
    print("Fried eggs are ready!")

def make_sandwich():
    time.sleep(1)
    print("Sandwich is ready!")

def make_coffee():
    time.sleep(1)
    print("Coffee is ready!")

make_breakfast()