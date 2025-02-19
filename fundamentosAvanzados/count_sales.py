from collections import Counter

def count_sales(products: list[str]) -> Counter:
    #usa Counter para cuantos productos de cada tipo se han vendido
    return Counter(products)

sales = ['laptop', 'smartphone', 'laptop', 'smartphone', 'tablet']
result = count_sales(sales)
print(result) #Output: Counter ({'laptop: 2, 'smartphone': 2, 'tablet': 1})