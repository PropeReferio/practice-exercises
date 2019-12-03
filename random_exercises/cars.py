def car_info(manu, model, **car_info):
    """Creates a dictionary with info about a car that can receive an
    arbitrary number of k,v pairs"""
    car = {}
    car['manufacturer'] = manu
    car['model'] = model
    for k, v in car_info.items():
        car[k] = v
    return car