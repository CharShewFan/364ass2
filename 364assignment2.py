import sys
import cplex
from cplex.exceptions import CplexError


def create_problem(x, y, z):
    f = open('temp.txt', 'a')
    f.write('Minimize\n')
    f.write('obj1: 1\n')
    add_demand_constraints(f, x, y, z)
    #add_capacity_constraints(f, x, y, z)
    
    
    
def add_demand_constraints(file, x, y, z):
    f.write("subject to"+'\n')
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
            constraint_name = 'demand' + str(index)
            file.write(constraint_name + ': ')
            file.write(line)
            index += 1
                    
#def add_capacity_constraints(file, x, y, z):

def add_non_negative_constrain(X,Y,Z):
    f.write("bounds"+'\n')
    for i in range(1,X+1):
        for j in range(1,Z+1):
            for k in range(1,Y+1):
                if f.line == '':
                    line = line + 'x' + str(i) + str(k) + str(j) + " >=0"
                else:
                    line = line + 'x' + str(i) + str(k) + str(j) + " >=0"+'\n' \
                f.write(line)


def add_capacity_constraint():
    for i in range(1,X+1):
        for j in range(1,Z+1):
            for k in range(1,Y+1):
                if f.line == '':
                    line = line + "capp"+ i +":"+'x' + str(i) + str(k) + str(j) + " >=" + "C" + + str(i) + str(k) + str(j)
                else:
                    line = line +  "capp"+ i +'x' + str(i) + str(k) + str(j) + " >=0" + str(i) + str(k) + str(j)+'\n'
                f.write(line)

    f.write("end")
        
    



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 364assignment2.py X Y Z")
        print("where 'X' 'Y' and 'Z' are positive integers and 'Y' has to be greater or equal to 2")
        sys.exit(-1)
    else:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            z = int(sys.argv[3])
            if (x >= 0) and (y >= 2) and (z >= 0):
                my_prob = create_problem(x, y, z)
            else:
                print("'X' 'Y' and 'Z' have to be positive integers and 'Y' >= 2")
        except:
            print("Usage: 364assignment2.py X Y Z")
            print("where 'X' 'Y' and 'Z' are positive integers and 'Y' has to be greater or equal to 2")
            sys.exit(-1)            


