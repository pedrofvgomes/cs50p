fruit = input("Item: ").lower()
c = 0
if fruit == 'apple':
    c = 130
if fruit in ['avocado', 'cantaloupe', 'honeydew melon', 'pineapple', 'strawberries', 'tangerine']:
    c = 50
if fruit == 'banana':
    c = 110
if fruit in ['grapefruit', 'nectarine', 'peach']:
    c = 60
if fruit in ['grapes', 'kiwifruit']:
    c = 90
if fruit == 'lemon':
    c = 15
if fruit == 'lime':
    c = 20
if fruit in ['orange', 'watermelon']:
    c = 80
if fruit in ['pear', 'sweet cherries']:
    c = 100
if fruit == 'plums':
    c = 70
if c != 0:
    print("Calories: " + str(c))