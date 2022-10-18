

def document_it(func: str):

    def wrapper(*args):

        for i in (args):

            if not (isinstance(i, str) and len(i) > 5):
                raise ValueError(
                    "erorr you should type str and the length of the str is more than 5!")

            print("Documenting the function, name : ", func.__name__)
        return func(*args)

    return wrapper

# @document_it


def decorator(x: str):
    print(x)


decorator_arguments = document_it(decorator)
decorator_arguments("de")
