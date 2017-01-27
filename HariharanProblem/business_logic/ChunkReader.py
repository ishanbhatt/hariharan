'''
Created on Jan 9, 2017

@author: Ishan.Bhatt
'''
def get_line():
    with open(r'D:\VikasStuff/UBSRTOUBSR_ACCTPGP_first.csv') as f1:
        for i in f1:
            yield i

lines_required = 100
gen = get_line()

chunk = [next(gen) for i in range(lines_required)]
print chunk[0].rstrip()
chunk = [next(gen) for i in range(lines_required)]
print chunk[0].rstrip()

class A(object):
    def sum(self):
        print "A Called"
        
class B(A):
    def sum(self):
        super(B,self).sum() #Do not call A.sum(self)
        print "B Called"
        
a = B()
a.sum()

