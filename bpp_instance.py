class BPP_Instance:
    
    def __init__(self, e_n, e_vol, c):
        # number of objects --> 0...len(self.e_vol)-1 (? useful ?)
        self.e_n = e_n                        
        # volume of each object
        self.e_vol = e_vol   
        # capacity of the containers 
        self.c = c                           

    # returns True if the instance is unfeasible, False otherwise
    def unfeasible(self):
        return False

    # returns some trivial objective bounds [lower_bound, upper_bound] as a tuple
    def obj_bounds(self):
        import math
        return (math.ceil(sum(self.e_vol) / self.c), self.e_n)
