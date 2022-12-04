class BPP_Instance:
    
    def __init__(self, e_n, e_vol, c):
        # number of objects 
        # 0...len(self.e_vol)-1 (? useful ?)
        self.e_n = e_n                        
        # volume of each object
        self.e_vol = e_vol   
        # capacity of the containers 
        self.c = c                           

    # returns True if the instance is unfeasible, False otherwise
    def unfeasible(self):
        return max(self.e_vol) > self.c

    # returns some objective bounds [lower_bound, upper_bound] as a tuple
    def obj_bounds(self):
        from math import ceil
        return (ceil(sum(self.e_vol) / self.c), self.e_n)
