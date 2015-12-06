__author__ = 'Sushil'
from code9 import *
import dtlz
import pickle

if __name__ == '__main__':
    models = [dtlz.dtlz5]
    objs = [2, 4, 6, 8]
    decs = [10, 20, 40]
    for model in models:
        for num_objs in objs:
            for num_decs in decs:
                run_name = model.__name__+'_o'+str(num_objs)+'_d'+str(num_decs)+'_u'
                untune = [run_name]
                untune_spread = [run_name+'_spread']
                print run_name
                for i in xrange(20):
                    ga_u = GA(model, num_objs, num_decs, prob_mut=0.05, num_candidates=100, num_generations=1000)
                    res_u = ga_u.run()
                    untune.append(res_u.hyper_vol)
                    untune_spread.append(res_u.spread)
                    print 'Completed Run'+str(i)+': HV='+str(res_u.hyper_vol)
                with open('outputs/'+run_name+'.lst', 'wb') as file:
                    pickle.dump(untune, file)
                with open('outputs/'+run_name+'_spread.lst', 'wb') as file:
                    pickle.dump(untune_spread, file)