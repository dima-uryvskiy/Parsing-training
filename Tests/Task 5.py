import re

string_categories = "name: Мужская одежда url : https://example.com/category/160 parent_id: 0" \
                    "name: Женская одежда url : https://example.com/category/168 parent_id: 0" \
                    "name: Платья url : https://example.com/category/41 parent_id: 168" \
                    "name: Блузки url : https://example.com/category/451 parent_id: 168" \
                    "name: Тапки url : https://example.com/category/45 parent_id: 160" \
                    "name: Туфли url : https://example.com/category/455 parent_id: 168" \
                    "name: Кепки url : https://example.com/category/67 parent_id: 160" \
                    "name: Юбки url : https://example.com/category/52 parent_id: 168"

print(*re.findall(r'(\w{5}://\w+\.\w+/\w+/\d+) \w+: [160]{3}', string_categories), sep='\n')
