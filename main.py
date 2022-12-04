from bpp_instance import BPP_Instance
from bpp_solution import BPP_Solution


instance = BPP_Instance(e_n = 9, 
                        e_vol = (2,1,2,1,1,2,3,2,1),
                        c = 4)

if not instance.unfeasible():

    obj_lower_bound, obj_upper_bound = instance.obj_bounds()

    print(f"{obj_lower_bound} <= obj <= {obj_upper_bound}")
    
    x = BPP_Solution(instance)

    if x.feasible():
        print('feasible solution, obj = ', x.obj())
    else:
        print('unfeasible solution')

    print('placements: ', x.e_pos)
    print('residual capacities: ', x.c_residual)
    print()

    x.greedy_ff()

    if x.feasible():
        print('feasible solution, obj = ', x.obj())
    else:
        print('unfeasible solution')

    print('placements: ', x.e_pos)
    print('residual capacities: ', x.c_residual)
    print()

    

# TODO
# - build BPP_instances from instance files
# - find a dataset of instances
# - use np.arrays instead of built-in ones
