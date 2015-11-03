from models import *
from optimizers import *


def main():
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [sa, mws]:
            optimizer(model())
            # TODO: write code...

if __name__ == "__main__":
    main()