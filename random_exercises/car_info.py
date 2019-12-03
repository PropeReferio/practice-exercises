def car_info(manu, model, **car_info):
    car = {}
    car['manufacturer'] = manu
    car['model'] = model
    for k, v in car_info.items():
        car[k] = v
    return car