# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from dummy import *

class TimeSuite:
    def time_a(self):
        for i in range(100000):
            pass

    def time_b(self):
        for i in range(1000):
            pass

    def time_c(self):
        for i in range(100000):
            pass
