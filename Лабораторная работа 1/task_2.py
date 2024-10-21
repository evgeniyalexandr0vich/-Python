# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_disk = 1.44
symbol = 4
quantity_of_symbols = 25
quantity_of_lines = 50
quantity_of_pages = 100
kilobyte = 1024

book_weight = symbol * quantity_of_symbols * quantity_of_lines * quantity_of_pages
book_weight_megabyte = book_weight / kilobyte ** 2
amount_of_books = volume_of_disk // book_weight_megabyte
print("Количество книг, помещающихся на дискету:", int(amount_of_books))
