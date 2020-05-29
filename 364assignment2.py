import sys
import cplex


def cplex_writed():
    c = cplex.Cplex()
    c.read("temp.txt")
    c.write("lp.lp",)





def create_problem(x, y, z):
    f = open('temp.txt', 'a')
    f.write('Minimize\n')
    line = ""
    for i in range(1,x+1):
        for k in range(1,y+1):
            if line == "":
                line = "C" + str(i) + str(k)
            else:
                line = line + " + " + "C" + str(i) + str(k)

    for k in range(1,y+1):
        for j in range(1,y+1):
            line = line + "+" + "d" + str(k) + str(j)

    f.write("obj1: ")
    f.write(line+"\n")
    add_demand_constraints(f, x, y, z)
    add_capacity_constraint(f, x, y,z)
    utilization(f,x,y,z)
    equal_flow(f,x,y,z)
    add_non_negative_constrain(f, x,y,z)
    cplex_writed()
    
    
    
def add_demand_constraints(file, x, y, z):
    file.write("subject to"+'\n')
    index = 1
    for i in range(1, x+1):
        for j in range(1, z+1):
            line = ''
            for k in range(1, y+1):
                if line == '':
                    line = line + 'x' + str(i) + str(k) + str(j)
                else:
                    line = line + ' + ' + 'x' + str(i) + str(k) + str(j)
            line = line + ' = ' + str(i + j) + '\n'
            constraint_name = 'demandflow:' + str(index)
            file.write(constraint_name + ': ')
            file.write(line)
            index += 1
                    

def add_non_negative_constrain(f,X,Y,Z):
    f.write("bounds"+'\n')
    for i in range(1,X+1):
        for k in range(1,Y+1):
            line3 = 'c' + str(i) + str(k) + " >= 0\n"
            f.write(line3)
            for j in range(1,Z+1):
                line = 'x' + str(i) + str(k) + str(j) + " >= 0"+'\n'
                line2 = "0 <= " + 'u' + str(i) + str(k) + str(j) + " <= 1\n"
                f.write(line)
                f.write(line2)

    for k in range(1,Y+1):
        for j in range(1,Z+1):
            line4 = "d" + str(k) + str(j) + " >= 0\n"
            f.write(line4)

    f.write("end \n")


def add_capacity_constraint(f,X,Y,Z):
    index = 1
    for i in range(1,X+1):
        for j in range(1,Z+1):
            line = ''
            for k in range(1,Y+1):
                line = line + "capp"+ str(index) + ":" +' x' + str(i) + str(k) + str(j) + " <= " + "c" + str(i) + str(k) + '\n'
                index += 1
            f.write(line)

    for k in range(1,y+1):
        for j in range(1,z+1):
            line = ''
            for i in range(1,x+1):
                line = line + "capp"+ str(index) + ":" +' x' + str(i) + str(k) + str(j) + " <= " + "d" + str(k) + str(j) + '\n'
                index += 1
            f.write(line)
    f.write("\n")


def utilization(f,x,y,z):
    for i in range(1,x+1):
        for j in range(1,z+1):
            line = ""
            for k in range(1,y+1):
                line = "equallySplit:" + "u" + str(i) + str(k) + str(j)
            f.write(line + "\n")


def equal_flow(f,x,y,z):
    for i in range(1,x+1):
        for k in range(1,y+1):
            line = ""
            for j in range(1,z+1):
                line = "(u" + str(i) + str(k) + str(j) + " * " + "h" + str(i) + str(j) + ")/2"
            f.write(line)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 364assignment2.py X Y Z11111")
        print("where 'X' 'Y' and 'Z' are positive integers and 'Y' has to be greater or equal to 2")
        sys.exit(-1)
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
        print(x,y,z)
        if (x >= 0) and (y >= 2) and (z >= 0):
            my_prob = create_problem(x, y, z)
        else:
            print("'X' 'Y' and 'Z' have to be positive integers and 'Y' >= 2")
    """except:
            print("Usage: 364assignment2.py X Y Z")
            print("where 'X' 'Y' and 'Z' are positive integers and 'Y' has to be greater or equal to 2")
            sys.exit(-1)   """



