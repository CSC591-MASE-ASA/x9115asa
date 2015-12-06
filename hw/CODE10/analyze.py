__author__ = 'Sushil'
import glob
import pickle
from sk import rdivDemo


if __name__ == '__main__':
    rDiv_ip=[]
    for file in glob.glob('outputs/*lst'):
        with open(file, 'rb') as f:
            my_list = pickle.load(f)
            rDiv_ip.append(my_list)
    rdivDemo(rDiv_ip)