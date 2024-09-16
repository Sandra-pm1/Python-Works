class Operations:

    def perform_adds(self,*args):
        total=sum([arg for arg in args if isinstance(arg,(int,float))])
        return total

    def get_max(self,*args):
        return max(args)

math=Operations()

print(math.perform_adds(10,30))
print(math.perform_adds(20,60,40))