class House:
    def __init__(self, name, floor_numb):
        self.name = name
        self.floor_numb = floor_numb

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name}, имеет   {self.floor_numb} этажа \пПоднимаемся на {new_floor}')
        if new_floor < 1 or  new_floor > self.floor_numb:
            print(f'{new_floor} - такого этажа не существует')
        else:
           for floor in range(new_floor):
            print(floor + 1)

hightower = House('Башня', 12)
warehouse = House('Склад', 4)

hightower.go_to(9)
warehouse.go_to(-1)