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
    # asserts if self is inconsistent
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
    # asserts if self is unfeasible or inconsistent
    def obj(self):
        assert self.feasible()
        return len(self.c_residual)


    # builds a feasible solution using First Fit (constructive heuristic),
    # starting from the current solution state. 
    # asserts if all objects are already placed in a container
    def greedy_ff(self, iter_indexes = None):

        assert not self.feasible()

        # useful to change indexes for First Fit Decreasing
        if iter_indexes is None:
            iter_indexes = range(self.p.e_n)

        for i in iter_indexes:

            # i-th object is already placed in a container
            if self.e_pos[i] != -1: continue

            for j, r in enumerate(self.c_residual):
                # i-th object fits in j-th container
                if r >= self.p.e_vol[i]:
                    self.c_residual[j] -= self.p.e_vol[i]
                    self.e_pos[i] = j
                    break
            else:
                # i-th object requires the addition of a new container
                self.c_residual.append(self.p.c - self.p.e_vol[i])
                self.e_pos[i] = len(self.c_residual) - 1


    # builds a feasible solution using First Fit Decreasing (constructive heuristic),
    # starting from the current solution state. 
    # asserts if all objects are already placed in a container
    def greedy_ffd(self):

        assert not self.feasible()

        # indirect sorting on self.p.e_vol in descending order
        # self.p.e_vol[indexes[0]] >= self.p.e_vol[indexes[1]] >= ... >= self.p.e_vol[indexes[len(self.p.e_vol)-1]]
        indexes = sorted(range(len(self.p.e_vol)), 
                            reverse = True, 
                            key = lambda i: self.p.e_vol[i])

        self.greedy_ff(iter_indexes = indexes)


    # return a string representation of the solution
    def __str__(self):
        s = "--- SOLUTION STATE ---\n"
        s += f"feasible solution, obj = {self.obj()}\n" if self.feasible() else "unfeasible solution\n"
        s += f"placements: {self.e_pos}\n"
        s += f"residual capacities: {self.c_residual}\n"
        return s