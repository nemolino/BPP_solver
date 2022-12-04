class BPP_Solution:

    # builds an "empty" solution (unfeasible)
    def __init__(self, bpp_instance):
        # BPP_Instance we are working on
        self.p = bpp_instance
        # e_pos[i] = container in which we place object i
        self.e_pos = [-1] * self.p.e_n
        # c_residual[i] = residual capacity of container i
        self.c_residual = []

    # returns True if self is feasible, False otherwise 
    # throws an error if self is inconsistent
    def feasible(self):

        is_feasible = True
        c_residual_check = [self.p.c] * len(self.c_residual)

        for i, pos in enumerate(self.e_pos):

            if pos == -1: 
                # object still not placed in a container
                is_feasible = False
            else: 
                # False if the object has an invalid position
                assert 0 <= pos < len(self.c_residual) 
                c_residual_check[pos] -= self.p.e_vol[i]

        # False if object positions and residual capacities are inconsistent
        assert self.c_residual == c_residual_check

        # False if we are using an empty container 
        # ??? not sure if I should check this condition ???
        assert all(x != self.p.c for x in self.c_residual)
        
        return is_feasible

    # returns the objective value of self
    # throws an error if self is unfeasible or inconsistent
    def obj(self):
        assert self.feasible()
        return len(self.c_residual)

    # builds a solution using First Fit constructive heuristic
    def greedy_ff():
        pass

    # builds a solution using First Fit Decreasing constructive heuristic
    def greedy_ffd():
        pass