from models import *
from optimizers import *


def main():
    for model in [Schaffer, Kursawe, Osyczka2]:
        for optimizer in [sa]:
            print optimizer(model())
            # TODO: write code...

if __name__ == "__main__":
    main()