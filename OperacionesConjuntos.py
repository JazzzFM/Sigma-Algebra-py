import math 

def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

def Intersec(lst1, lst2):
    final_list = list(set(lst1) & set(lst2))
    return final_list

def Less(lst1, lst2):
    aux = set(list(lst1) + list(lst2))
    final_list = aux - set(list(lst2))
    return list(final_list)
  
def printPowerSet(set, set_size):   
    pow_set_size = (int) (math.pow(2, set_size)); 
    counter = 0; 
    j = 0; 
      
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size): 
            if((counter & (1 << j)) > 0): 
                print(set[j], end = ""); 
        print(""); 
  

if __name__== '__main__':
    a = [1, 2, 3]
    b = [3,4, 5]
    c = Union(a, b)
    d = Intersec(a, b)
    e = Less(a, b)

    set = ['a', 'b', 'c']; 
    printPowerSet(set, 3); 

    print(c)
    print(d)
    print(e)
