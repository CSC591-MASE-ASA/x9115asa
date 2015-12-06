__author__ = 'Sushil'
from code10 import *
import dtlz
import pickle

if __name__ == '__main__':
    models = [dtlz.dtlz7]
    objs = [2, 4, 6, 8]
    decs = [10, 20, 40]
    lower = [0.01, 20, 200]
    upper = [0.5, 100, 1000]
    for model in models:
        for num_objs in objs:
            for num_decs in decs:
                run_name = model.__name__+'_o'+str(num_objs)+'_d'+str(num_decs)+'_t'
                tune = [run_name]
                tune_spread = [run_name+'_spread']
                tm = Tuner_Model(lower, upper, model, num_objs, num_decs)
                ga_params = differential_evolution(tm)
                print 'DE Runs Completed, Params are: '+str(ga_params)
                print run_name
                for i in xrange(20):
                    ga_t = GA(model, num_objs, num_decs, *ga_params)
                    res_t = ga_t.run()
                    print 'Completed Run'+str(i)+': HV='+str(res_t.hyper_vol)
                    tune.append(res_t.hyper_vol)
                with open('outputs/'+run_name+'.lst', 'wb') as file:
                    pickle.dump(tune, file)
                with open('outputs/'+run_name+'_spread.lst', 'wb') as file:
                    pickle.dump(tune, file)