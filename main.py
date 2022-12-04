from bpp_instance import BPP_Instance
from bpp_solution import BPP_Solution


instance = BPP_Instance(e_n = 9, 
                        e_vol = (2,1,2,1,1,2,3,2,1),
                        c = 4)

print(f"--- BPP INSTANCE ---\n{instance}")

if not instance.unfeasible():

    print("The instance is feasible.\n")

    obj_lower_bound, obj_upper_bound = instance.obj_bounds()
    print(f"A trivial objective bounding: {obj_lower_bound} <= obj <= {obj_upper_bound}\n")

    x = BPP_Solution(instance)
    #print(x)
    x.greedy_ff()
    print(f"After FF solution construction:\n\n{x}")
    
    x = BPP_Solution(instance)
    #print(x)
    x.greedy_ffd()
    print(f"After FFD solution construction:\n\n{x}")
else:
    print("The instance is unfeasible.\n")

    

# TODO
# - build BPP_instances from instance files
# - find a dataset of instances
# - use np.arrays instead of built-in ones