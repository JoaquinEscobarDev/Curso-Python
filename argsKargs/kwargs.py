def print_info(**kwargs):  # kw = keywords, args = arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Carlos", age=30, city="Santiago")
print_info(name="Carlos", age=30, city="Santiago", country="Chile")
