import json

if __name__ == "__main__":
    # read files:
    f = open('test.txt')




    with open('superheroes.json') as f:
        superheroes = json.load(f)
    print(type(superheroes))
    # output is dict
    print(superheroes.keys())

