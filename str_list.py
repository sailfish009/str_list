def str_list(t):
    """
    string to list
    """
    t = (
        t
        .strip('\"')
        .strip('\'')
        .strip('\[')
        .strip('\]')
    )
    return (
        [
            s.strip('\'') for s in [
                s.strip() for s in list(t.split(',')) 
            ] 
        ]
    ) 
   

t = "['1', '2', '3']"
l = str_list(t)

print(f't is string: {isinstance(t, str)}')
print(f'l is string: {isinstance(l, str)}')
print(f'l is list: {isinstance(l, list)}')
print(f't: {t}')
print(f'l: {l}')
