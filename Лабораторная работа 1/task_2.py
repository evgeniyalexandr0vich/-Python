# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_disk = 1.44
book_weight = (4 * 25 * 50 * 100) / (1024 ** 2)
amount_of_books = volume_of_disk // book_weight
print("Количество книг, помещающихся на дискету:", int(amount_of_books))
