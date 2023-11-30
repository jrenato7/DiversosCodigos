"""

You are going on a camping trip, but before you leave you need to buy groceries. To optimize your time spent in the store, instead of buying the items from your shopping list in order, you plan to buy everything you need from one department before moving to the next.

Given an unsorted list of products with their departments and a shopping list, return the time saved in terms of the number of department visits eliminated.

Example:
products = [
    ["Cheese",          "Dairy"],
    ["Carrots",         "Produce"],
    ["Potatoes",        "Produce"],
    ["Canned Tuna",     "Pantry"],
    ["Romaine Lettuce", "Produce"],
    ["Chocolate Milk",  "Dairy"],
    ["Flour",           "Pantry"],
    ["Iceberg Lettuce", "Produce"],
    ["Coffee",          "Pantry"],
    ["Pasta",           "Pantry"],
    ["Milk",            "Dairy"],
    ["Blueberries",     "Produce"],
    ["Pasta Sauce",     "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]

For example, buying the items from list1 in order would take 5 department visits, whereas your method would lead to only visiting 3 departments, a difference of 2 departments.

Produce(Blueberries)->Dairy(Milk)->Pantry(Coffee/Flour)->Dairy(Cheese)->Produce(Carrots) = 5 department visits
New: Produce(Blueberries/Carrots)->Pantry(Coffee/Flour)->Dairy(Milk/Cheese) = 3 department visits

list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"] => 2
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"] => 0
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"] => 2
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"] => 0

All Test Cases:
shopping(products, list1) => 2
shopping(products, list2) => 2
shopping(products, list3) => 0
shopping(products, list4) => 2
shopping(products, list5) => 0

Complexity Variable:
n: number of products

"""

from collections import defaultdict


def shopping(products, shop_items):
    """
    O(n^2) tempo and O(n) espaço
    """
    prod_dep = {
        p: d for p,d in products
    }

    shop_order = []
    current_dep = None
    for shop_item in shop_items:  # Este "for" executa em O(n) tempo
        if current_dep == prod_dep[shop_item]:
            shop_order[len(shop_order) - 1][1].append(shop_item)
        else:
            shop_order.append(
                [prod_dep[shop_item], [shop_item]]
            )
        current_dep = prod_dep[shop_item]

    dep_prod = defaultdict(list)
    for p, d in prod_dep.items():
        dep_prod[d].append(p)

    shop_order2 = defaultdict(list)
    for shop_item in shop_items:  # Este "for" executa em O(n^2) tempo
        department = prod_dep[shop_item]
        if department not in shop_order2:
            for p in dep_prod[department]:
                # Este "in" causa a complexidade de tempo n^2 pq verifica
                # dentro da lista.
                if p in shop_items:
                    shop_order2[department].append(p)

    return len(shop_order) - len(shop_order2)


def shopping_v2(products, shop_items):
    """
    O(n) tempo and O(n) espaço
    """
    prod_dep = {
        prod: dep for prod, dep in products
    }
    # Não posso usar set aqui porque vai alterar a ordem, causando problemas
    # na execução. para este problema a ordem das ocorrências é importante
    #shop_items = set(shop_items)
    # esta mudança reduz o tempo para verificar se um valor está em shop_items
    # já que ele executa em O(1)
    shop_items = {item: True for item in shop_items}
    #print(shop_items)

    shop_order = []
    current_dep = None
    for shop_item in shop_items:  # Este "for" executa em O(n^2) tempo
        if current_dep == prod_dep[shop_item]:
            shop_order[len(shop_order) - 1][1].append(shop_item)
        else:
            shop_order.append(
                [prod_dep[shop_item], [shop_item]]
            )
        current_dep = prod_dep[shop_item]

    dep_prod = defaultdict(set)
    for prod, dep in prod_dep.items():
        dep_prod[dep].add(prod)

    shop_order2 = defaultdict(set)
    for shop_item in shop_items:  # Este "for" executa em O(n^2) tempo
        department = prod_dep[shop_item]
        if department not in shop_order2:
            for prod in dep_prod[department]:
                # Este "in" executa em O(1) pq está verificando em um dicionário
                if prod in shop_items:
                    shop_order2[department].add(prod)

    #import pprint
    #print(f"Tam ord 1 {len(shop_order)}")
    #pprint.pprint(shop_order)
    #print(f"Tam ord 2 {len(shop_order2)}")
    #pprint.pprint(shop_order2)
    return len(shop_order) - len(shop_order2)


if __name__ == '__main__':
    products = [
        ["Cheese", "Dairy"],
        ["Carrots", "Produce"],
        ["Potatoes", "Produce"],
        ["Canned Tuna", "Pantry"],
        ["Romaine Lettuce", "Produce"],
        ["Chocolate Milk", "Dairy"],
        ["Flour", "Pantry"],
        ["Iceberg Lettuce", "Produce"],
        ["Coffee", "Pantry"],
        ["Pasta", "Pantry"],
        ["Milk", "Dairy"],
        ["Blueberries", "Produce"],
        ["Pasta Sauce", "Pantry"]
    ]

    list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
    list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"]
    list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"]
    list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"]
    list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"]
    print("V1")
    print(shopping(products, list1))
    print(shopping(products, list2))
    print(shopping(products, list3))
    print(shopping(products, list4))
    print(shopping(products, list5))
    print("V2")
    print(shopping_v2(products, list1))
    print(shopping_v2(products, list2))
    print(shopping_v2(products, list3))
    print(shopping_v2(products, list4))
    print(shopping_v2(products, list5))

    """
V2 - USING SET 
{'Milk', 'Coffee', 'Blueberries', 'Cheese', 'Flour', 'Carrots'}
Tam ord 1 6
[['Dairy', ['Milk']],
 ['Pantry', ['Coffee']],
 ['Produce', ['Blueberries']],
 ['Dairy', ['Cheese']],
 ['Pantry', ['Flour']],
 ['Produce', ['Carrots']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Milk', 'Cheese'},
             'Pantry': {'Flour', 'Coffee'},
             'Produce': {'Carrots', 'Blueberries'}})
3
{'Milk', 'Coffee', 'Blueberries', 'Cheese', 'Flour', 'Carrots'}
Tam ord 1 6
[['Dairy', ['Milk']],
 ['Pantry', ['Coffee']],
 ['Produce', ['Blueberries']],
 ['Dairy', ['Cheese']],
 ['Pantry', ['Flour']],
 ['Produce', ['Carrots']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Milk', 'Cheese'},
             'Pantry': {'Flour', 'Coffee'},
             'Produce': {'Carrots', 'Blueberries'}})
3
{'Iceberg Lettuce', 'Romaine Lettuce', 'Carrots', 'Blueberries'}
Tam ord 1 1
[['Produce', ['Iceberg Lettuce', 'Romaine Lettuce', 'Carrots', 'Blueberries']]]
Tam ord 2 1
defaultdict(<class 'set'>,
            {'Produce': {'Blueberries',
                         'Carrots',
                         'Iceberg Lettuce',
                         'Romaine Lettuce'}})
0
{'Flour', 'Milk', 'Pasta Sauce', 'Chocolate Milk'}
Tam ord 1 4
[['Pantry', ['Flour']],
 ['Dairy', ['Milk']],
 ['Pantry', ['Pasta Sauce']],
 ['Dairy', ['Chocolate Milk']]]
Tam ord 2 2
defaultdict(<class 'set'>,
            {'Dairy': {'Chocolate Milk', 'Milk'},
             'Pantry': {'Flour', 'Pasta Sauce'}})
2
{'Canned Tuna', 'Cheese', 'Potatoes', 'Blueberries'}
Tam ord 1 3
[['Pantry', ['Canned Tuna']],
 ['Dairy', ['Cheese']],
 ['Produce', ['Potatoes', 'Blueberries']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Cheese'},
             'Pantry': {'Canned Tuna'},
             'Produce': {'Potatoes', 'Blueberries'}})
0


V2 - USING DICT
{'Blueberries': True, 'Milk': True, 'Coffee': True, 'Flour': True, 'Cheese': True, 'Carrots': True}
Tam ord 1 5
[['Produce', ['Blueberries']],
 ['Dairy', ['Milk']],
 ['Pantry', ['Coffee', 'Flour']],
 ['Dairy', ['Cheese']],
 ['Produce', ['Carrots']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Cheese', 'Milk'},
             'Pantry': {'Flour', 'Coffee'},
             'Produce': {'Carrots', 'Blueberries'}})
2
{'Blueberries': True, 'Carrots': True, 'Coffee': True, 'Milk': True, 'Flour': True, 'Cheese': True}
Tam ord 1 5
[['Produce', ['Blueberries', 'Carrots']],
 ['Pantry', ['Coffee']],
 ['Dairy', ['Milk']],
 ['Pantry', ['Flour']],
 ['Dairy', ['Cheese']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Cheese', 'Milk'},
             'Pantry': {'Flour', 'Coffee'},
             'Produce': {'Carrots', 'Blueberries'}})
2
{'Blueberries': True, 'Carrots': True, 'Romaine Lettuce': True, 'Iceberg Lettuce': True}
Tam ord 1 1
[['Produce', ['Blueberries', 'Carrots', 'Romaine Lettuce', 'Iceberg Lettuce']]]
Tam ord 2 1
defaultdict(<class 'set'>,
            {'Produce': {'Blueberries',
                         'Carrots',
                         'Iceberg Lettuce',
                         'Romaine Lettuce'}})
0
{'Milk': True, 'Flour': True, 'Chocolate Milk': True, 'Pasta Sauce': True}
Tam ord 1 4
[['Dairy', ['Milk']],
 ['Pantry', ['Flour']],
 ['Dairy', ['Chocolate Milk']],
 ['Pantry', ['Pasta Sauce']]]
Tam ord 2 2
defaultdict(<class 'set'>,
            {'Dairy': {'Chocolate Milk', 'Milk'},
             'Pantry': {'Flour', 'Pasta Sauce'}})
2
{'Cheese': True, 'Potatoes': True, 'Blueberries': True, 'Canned Tuna': True}
Tam ord 1 3
[['Dairy', ['Cheese']],
 ['Produce', ['Potatoes', 'Blueberries']],
 ['Pantry', ['Canned Tuna']]]
Tam ord 2 3
defaultdict(<class 'set'>,
            {'Dairy': {'Cheese'},
             'Pantry': {'Canned Tuna'},
             'Produce': {'Potatoes', 'Blueberries'}})
    """
