from __future__ import division
from sets import Set;
from random import randint;

def has_duplicates(ip_list):
    s = Set();
    for i in ip_list:
        if(i in s):
            # print("Dup",i)
            return True;
        else:
            s.add(i);
    return False;
    
def generate_sample(n):
    res=[];
    for i in xrange(n):
        res.append(randint(1, 365));
    return res;

def create_simulations(s,n):
    res=[];
    for i in xrange(s):
        res.append(generate_sample(n))
    return res;

def calculate_total_positives(nested_list):
    count = 0;
    for this_list in nested_list:
        if has_duplicates(this_list):
            count+=1
    return count;

def birthday_paradox(simulation_size,sample_size):
    sim = create_simulations(simulation_size,sample_size);
    # print sim
    positives = calculate_total_positives(sim);
    # print "positives",positives;
    # print (simulation_size,positives/simulation_size)
    return positives/simulation_size;
    

simulations = 1000;
sample_size = 31;
probability = birthday_paradox(simulations,sample_size)
print ("Probability of birthday paradox = '{0}' for '{1}' simulations, each of size '{2}'"
        .format(probability,simulations,sample_size))
    