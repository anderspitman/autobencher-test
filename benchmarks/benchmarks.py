# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from dummy import func1, func2, func3

class TimeSuite:
    def time_func1(self):
        func1()

    def time_func2(self):
        func2()

    def time_func3(self):
        func3()
