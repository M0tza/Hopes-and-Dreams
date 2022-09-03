from pysine import sine
import time

c = 16.35
cs = 17.32
d = 18.35
ef =19.45
e = 20.60
f = 21.83
fs = 23.12
g = 24.50
gs = 25.96
a = 27.50
bf = 29.14
b = 30.87

w  = 1.412
dh = 1.059
h = 0.706
dq= 0.528
q = 0.353
ei= 0.176
s = 0.088


def note(letter, octave, length):
    sine(letter*(2 ** octave), 11*length/12)
    time.sleep(length/12)

def rest(length):
    time.sleep(length)
i = 0
while i != 2:
    #1
    note(f,4,q)
    rest(q)
    note(f,5,q)
    rest(q)
    #2
    note(c,5,h)
    rest(h)
    #3
    note(bf,4,q)
    rest(q)
    note(f,5,q)
    rest(q)
    #4
    note(f,4,h)
    rest(h)
    #5
    note(f,4,q)
    rest(q)
    note(a,4,q)
    rest(q)
    #6
    note(a,5,dh)
    note(bf,5,q)
    #7
    note(a,5,q)
    rest(q)
    note(f,5,q)
    rest(q)
    if i == 0:
        #8
        note(d,5,h)
        rest(h)
    i = i + 1
i = 0
#10
note(d,6,ei)
note(bf,5,ei)
note(a,5,ei)
note(f,5,ei)
note(d,5,ei)
note(c,5,ei)
note(bf,4,ei)
note(f,4,ei)
while i != 2:
    #11
    note(f,4,h)
    note(f,5,h)
    #12
    note(c,5,dh)
    rest(q)
    #13
    note(bf,4,h)
    note(f,5,h)
    #14
    note(f,4,dh)
    rest(q)
    #15
    note(f,4,h)
    note(a,4,h)
    #16
    note(a,5,dh)
    rest(q)
    #17
    note(bf,4,h)
    note(f,5,h)
    #18
    note(d,5,h)
    rest(h)
    i = i +1
i = 0
while i != 2:
    note(f,3,q)
    note(bf,4,q)
    note(c,4, q)
    note(bf,4,q)
    #20
    note(f,3,q)
    note(bf,4,q)
    note(c,4,q)
    note(bf,4,q)
    #21
    note(f,3,q)
    note(f,3,ei)
    note(bf,4,ei)
    note(c,4,q)
    note(ef,4,q)
    #22
    note(d,4,q)
    note(ef,4,q)
    note(d,4,ei)
    note(c,4,ei)
    note(bf,4,q)
    i = i + 1

i = 0
while i != 2:
    note(f,4,q)
    note(bf,5,q)
    note(c,5, q)
    note(bf,5,q)
    #20
    note(f,4,q)
    note(bf,5,q)
    note(c,5,q)
    note(bf,5,q)
    #21
    note(f,4,q)
    note(f,4,ei)
    note(bf,5,ei)
    note(c,5,q)
    note(ef,5,q)
    #22
    note(d,5,q)
    note(ef,5,q)
    note(d,5,ei)
    note(c,5,ei)
    note(bf,5,q)
    i = i + 1