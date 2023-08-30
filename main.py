with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        quantity_ingredient = int(file.readline())
        ingredients = []
        for ingredient in range(quantity_ingredient):
            name, quantity, measure = file.readline().strip().split('|')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingredients

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
#
def get_shop_list_by_dishes(dishes, person_count):
    ingrediend_to_cooking = {}
    for dishes, ingrediends in cook_book.items():
        for ingrediend in ingrediends:
            ingrediend_to_cooking[ingrediend['ingredient_name']] = {'measure': (ingrediend['measure']), 'quantity': (int(ingrediend['quantity']) * person_count)}
    return ingrediend_to_cooking

print(get_shop_list_by_dishes(['Запеченный картофель'], 2))
