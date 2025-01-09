import sys


def check_cords(circle_file, points_file):
    with open(circle_file, "r") as first_file:
        circle_cords = list(first_file)
        circle_cords = [i.rstrip().split() for i in circle_cords]
    with open(points_file, "r") as second_file:
        points_cords = list(second_file)
        points_cords = [i.rstrip().split() for i in points_cords]
    results = []
    for i in points_cords:
        if (int(i[0]) - int(circle_cords[0][0]))**2 + (int(i[1]) -
                    int(circle_cords[0][1]))**2 < int(circle_cords[1][0])**2:
            results.append(1)
        if (int(i[0]) - int(circle_cords[0][0]))**2 + (int(i[1]) -
                int(circle_cords[0][1]))**2 == int(circle_cords[1][0])**2:
            results.append(0)
        if (int(i[0]) - int(circle_cords[0][0]))**2 + (int(i[1]) -
                int(circle_cords[0][1]))**2 > int(circle_cords[1][0])**2:
            results.append(2)
    for i in results:
        print(f"{i}\n")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        check_cords(sys.argv[1], sys.argv[2])
    else:
        print("Need 2 args (file path's)")
