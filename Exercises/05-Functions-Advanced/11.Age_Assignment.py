def age_assignment(*args, **kwargs):
    result = {}
    for arg in args:
        result[arg] = kwargs[arg[0]]
    return result


    # result = {arg: kwargs[arg[0]] for arg in args}

