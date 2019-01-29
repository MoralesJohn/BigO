# BigO Notation
Big O exercises for my algorithm and data structures class.

I am taking a class on algorithms and data structures. The first assignment was to write some basic functions demonstrating various Big O time complexities. I hope some of this information proves useful to others. 

My exercises are implemented in python 3. 

## timing.py
We were given various makework algorithms to implement, analyze the time complexity, and then record the runtimes with various input sizes to compare against the analysis. The functions implemented vary from O(n) to more complicated ones, but I will let you figure them out for yourself. The input values (n_set) should change depending on which actual function you are testing with to better illustrate the differences. 

The times printed are in microseconds. Python's time function outputs floats of milliseconds, but I found the resulting runtimes bounced in and out of scientific notation, making direct comparisons cumbersome, so I converted the results. 

## ith_element.py
The goal here was given an array of integers such that A[1] < A[2] < A[3] < ... < A[N], find out if there exists an integer i where A[i] == i. 

You can see I have included various test versions of the array. 
