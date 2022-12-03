from bpp_instance import BPP_Instance
from bpp_solution import BPP_Solution


instance = BPP_Instance(e_n = 9, 
                        e_vol = (2,1,2,1,1,2,3,2,1),
                        c = 4)

if not instance.unfeasible():

    print(instance.obj_bounds())
    
    x = BPP_Solution(instance = instance)

    print(x.consistent())
    print(x.feasible())
    print(x.obj())

# TODO
# - finish basic scheme implementation
# - build BPP_instances from instance files
# - find a dataset of instances
# - use np.arrays instead of built-in ones
