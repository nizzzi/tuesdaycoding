# hello.py

#Def main(argv):
#   print "hello world"
#    return 0
    
    
#def target(*args):
#   return main, None   #returns the entry point
    
#if __name__ == '__main__':
#   import sys
#    main(sys.argv)



class Foo(object):
    def __init__(self, value):
        self.value = value
        
    def double(self):
        return Foo(self.value*2)
        
print Foo(42).double().value
print Foo("hello").double().value


d={}
for i in [1,2,3,4]:
    d[i]=i*i
print d


class Point(object)

make a change






    
    
