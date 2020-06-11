def bigger_price(limit: int, data: list) -> list:
    list_data = []
    biggest_price = []
    list_data_save = []
    index_list = []
    result = []
    for i in range(0, len(data)):
        list_data.append(data[i]["price"])
    list_data_save += list_data
    for i in range(0, limit):
        biggest_price.append(max(list_data))
        list_data_index = list_data.index(biggest_price[i])
        list_data.pop(list_data_index)
    for i in range(0, limit):
        index_list.append(list_data_save.index(biggest_price[i]))
    for i in range(0, limit):
        result.append(data[index_list[i]])
    return result
    
if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))