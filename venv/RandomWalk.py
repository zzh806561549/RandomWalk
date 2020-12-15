from random import choice
import pandas as pd


def RandomWalk(num_points, x_values, y_values):
    # x_values = [-37.8146194639988]
    # y_values = [144.974443493997]
    # 用来存放一个人得一行经纬度
    list_one_person = []
    for i in range(num_points):
        x_direction = choice([1, -1])
        x_distance = choice([1, 1.5, 2, 2.5])
        x_step = x_direction * x_distance * 1.1306029318178743e-06
        y_direction = choice([1, -1])
        y_distance = choice([1, 1.5, 2, 2.5])
        y_step = y_direction * y_distance * 8.759168813388694e-06
        if x_step == 0 and y_step == 0:
            continue
        x_values = x_values + x_step
        y_values = y_values + y_step
        # x_values.append(next_x)
        # y_values.append(next_y)
        list_one_person.append(str(x_values) + ';' + str(y_values))
    return list_one_person


if __name__ == '__main__':
    # 用来存放一堆人
    list_runner = []
    data1 = pd.read_csv('users-melbcbd-generated.csv')
    for item in data1.values:
        # 读取.csv文件来获取每个人得起始经纬度
        list_one_person = RandomWalk(100, item[0], item[1])
        list_runner.append(list_one_person)
    name = ['Latitude, Longitude']
    test = pd.DataFrame(columns=None, data=list_runner)
    test.to_csv('zzh.csv')
