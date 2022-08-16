def clear_vars():
    for element in dir():
        if element[0:2] != "__":
            del globals()[element]
