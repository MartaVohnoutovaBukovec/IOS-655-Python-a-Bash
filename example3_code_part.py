#example3 Marta UAI 735I winter 2017/2018  code part
import timeit

def clock(label, fce_name, cmd, times, cycle):
    repetition = timeit.repeat(setup="from __main__ import " + fce_name, stmt=cmd, repeat=times, number=cycle)
    return (label, *('{:.3f}'.format(x) for x in repetition))

