dict_categories = [
  {
    "name": "Мужская одежда",
    "url": "https://example.com/category/160",
    "parent_id": 0
  },
  {
    "name": "Женская одежда",
    "url": "https://example.com/category/168",
    "parent_id": 0
  },
  {
    "name": "Платья",
    "url": "https://example.com/category/41",
    "parent_id": 168
  },
  {
    "name": "Блузки",
    "url": "https://example.com/category/451",
    "parent_id": 168
  },
  {
    "name": "Тапки",
    "url": "https://example.com/category/45",
    "parent_id": 160
  },
  {
    "name": "Туфли",
    "url": "https://example.com/category/455",
    "parent_id": 168
  },
  {
    "name": "Кепки",
    "url": "https://example.com/category/67",
    "parent_id": 160
  },
  {
    "name": "Юбки",
    "url": "https://example.com/category/52",
    "parent_id": 168
  }
]

urls = []
parent_id = -1
for element in dict_categories:
    if element['name'] == "Женская одежда":
        parent_id = int(element['url'][-3:])  # взял последние 3 цифры url
    if element['parent_id'] == parent_id:     # выбрал нужные url
        urls.append(element['url'])
print(*urls, sep='\n')

####### Если сразу знаем parent_id = 168

parent_id = 168
urls = [element['url'] for element in dict_categories if element['parent_id'] == parent_id]
print("2 способ:")
print(*urls, sep='\n')
