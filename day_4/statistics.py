# Calculate mean
def ft_mean(*args: any ) -> None:
    n = len(args)
    if n != 0:
        mean = sum(args) / len(args)
        return mean
    
#median 
def ft_median(*args: any) -> None:
    sorted_args = sorted(args)
    n = len(args)
    if n % 2 == 0:
        median = (sorted_args[(n // 2) - 1] + sorted_args[n // 2]) / 2 
    else:
        median = (sorted_args[n // 2])
    return median

#Quartils
def ft_quartiles(*args: any) -> None:
    n = len(args)
    sorted_args = sorted(args)
    q1_index = n // 4
    q3_index = (3 * n) // 4
    quartiles = [sorted_args[q1_index], sorted_args[q3_index]]
    float_array = [(float(num)) for num in quartiles]
    return float_array
    
#std
def ft_std(*args: any):
    variance = sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)
    std = variance ** 0.5
    return std

#variance
def ft_variance(*args: any) -> None:
    variance = sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)
    return variance
    
#print
def ft_statistics(*args: any, **kwargs: any) -> None:
    n = len(args)
                
    for kw in kwargs.values():
        if kw == 'mean':
            mean = ft_mean(*args)
            if n != 0:
                print(f'mean:  {mean}')
            else :
                print("ERROR")
        elif kw == 'median':
            if n != 0:
                median = ft_median(*args)
                print(f'median:  {median}')
            else :
                print("ERROR")
        elif kw == 'quartile':
            if n != 0:
                quartiles = ft_quartiles(*args)
                print(f"quartile: [{quartiles[0]}, {quartiles[1]}]")
            else :
                print("ERROR")
        elif kw == 'std':
            if n != 0:  
                std = ft_std(*args)
                print(f'std:  {std}')
            else :
                print("ERROR")
        elif kw == 'var':
            if n != 0:  
                variance = ft_variance(*args)
                print(f'var:  {variance}')
            else :
                print("ERROR")
        else:
            return
            
