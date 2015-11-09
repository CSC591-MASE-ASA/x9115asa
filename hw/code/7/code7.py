from models import *
from optimizers import *


def main():
    for model in [Golinski]:
        mod = model()
        mod.baseline()
        for optimizer in [sa,mws]:
            op = optimizer(mod)
            op.compute()
            # TODO: write code...

if __name__ == "__main__":
    main()