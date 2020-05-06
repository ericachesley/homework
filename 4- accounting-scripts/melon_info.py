"""Print out all the melons in our inventory."""


from melons import melons

def print_melon(name):
    """Print each melon with corresponding attribute information."""

    price = melons[name]['price']
    seedlessness = melons[name]['seedlessness']
    weight = melons[name]['weight']
    flesh_color = melons[name]['flesh_color']
    rind_color = melons[name]['rind_color']
    

    have_or_have_not = 'have'
    if seedlessness:
        have_or_have_not = 'do not have'


    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}. \n \
They weigh {weight} pounds, and have {flesh_color} flesh and \
{rind_color} rinds.')


for name in melons:
    print_melon(name)