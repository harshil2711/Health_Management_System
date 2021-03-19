import datetime


def gettime():

    return datetime.datetime.now()


print('welcome to health management system')

try:

    decision = int(input('press 1 for lock the value and 2 for retrieve the value \n'))
    name = int(input('press 1 for harshil 2 for yax 3 for kinjal \n'))

except ValueError as v:
    print('check your value', v)
    exit()


def take():
    if name == 1:
        try:
            choice = int(input('press 1 for food and 2 for exercise \n'))

            if choice == 1:
                hf = input('enter your food \n')
                fh = open('harshil_food.txt' , 'a')
                fh.write(str([str(gettime())]) + ' : ' + hf + '\n')

            elif choice == 2:
                he = input('enter your exercise \n')
                eh = open('harshil_exercise.txt','a')
                eh.write(str([str(gettime())]) + ' : ' + he + '\n')

        except ValueError as v:
            print('please enter the valid input',v)


    elif name == 2:

        try:
            choice = int(input('press 1 for food and 2 for exercise \n'))

            if choice == 1:
                yf = input('enter your food \n')
                fy = open('yax_food.txt','a')
                fy.write(str([str(gettime())]) + ' : ' + yf + '\n')
            elif choice == 2:
                ye = input('enter your exercise \n')
                ey = open('yax_exercise.txt','a')
                ey.write(str([str(gettime())]) + ' : ' + ye + '\n')

        except ValueError as k:
            print('please enter the valid input',k)

    elif name == 3:
        try:
            choice = int(input('press 1 for food and 2 for exercise \n'))
            if choice == 1:
                kf = input('enter your food \n')
                fk = open('kinjal_food.txt','a')
                fk.write(str([str(gettime())]) + ' : ' + kf + '\n')

            elif choice == 2:
                ke = input('enter your exercise \n')
                ek = open('kinjal_exercise.txt','a')
                ek.write(str([str(gettime())]) + ' : ' + ke + '\n')

        except ValueError as p:
            print('please enter the valid input',p)


def retrieve():

    if name == 1:
        try:

            choice = int(input('press 1 for food and 2 for exercise \n'))

            if choice == 1:
                hf = open('harshil_food.txt', 'r')
                print(hf.read())

            elif choice == 2:
                he = open('harshil_exercise.txt','r')
                print(he.read())


        except ValueError as a:
            print('please enter the valid input')

    if name == 2:
        try:

            choice = int(input('press 1 for food and 2 for exercise \n'))
            if choice == 1:
                yf = open('yax_food.txt', 'r')
                print(yf.read())
            elif choice == 2:
                ye = open('yax_exercise.txt','r')
                print(ye.read())

        except ValueError as b:
            print('please enter the valid input')

    if name == 3:
        try:

            choice = int(input('press 1 for food and 2 for exercise \n'))
            if choice == 1:
                kf = open('kinjal_food.txt', 'r')
                print(kf.read())
            elif choice == 2:
                ke = open('kinjal_exercise.txt','r')
                print(ke.read())

        except ValueError as c:
            print('please enter the valid input',c)


if decision == 1:
    take()

elif decision == 2:
    retrieve()

