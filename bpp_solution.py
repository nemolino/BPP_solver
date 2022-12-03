class BPP_Solution:

    # builds an "empty" solution (unfeasible)
    def __init__(self, instance):
        # BPP_Instance we are working on
        self.P = instance
        # e_pos[i] = container in which we place object i
        self.e_pos = [-1] * self.P.e_n
        # c_residual[i] = residual capacity of container i
        self.c_residual = [self.P.c]

    # returns True if self representation is consistent, False otherwise : O(?)
    def consistent(self):
        return True

    # returns True if self is feasible, False otherwise : O(E)
    def feasible(self):
        assert self.consistent()
        return True

    # returns the objective value of self : O(1)
    def obj(self):
        assert self.consistent()
        assert self.feasible()
        return len(self.c_residual)

    # builds a solution using First Fit constructive heuristic
    def first_fit():
        pass

    # builds a solution using Decreasing First Fit constructive heuristic
    def decreasing_first_fit():
        pass