import pandas
data = pandas.read_csv("central_park_data.csv")
Fur_color = data["Primary Fur Color"]
grey_count = 0
red_count = 0
black_count = 0
def update_data():
    color_dict = {"Fur Color":["grey", "red", "black"], "Count":[grey_count, red_count, black_count]}
    return color_dict


for color in Fur_color:
    if color == "Gray":
        grey_count +=1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1
new_data= pandas.DataFrame(update_data())
new_data.to_csv("squirrel_count.csv")



