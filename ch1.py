def laff_copy(x, y):
    # Section 1.5.2, Homework 1.5.2.1
    # Vector-vector COPY routine.

    # vector laff_copy(vector x, vector y)
    # Copies the vector x into the vector y, returning the vector y.
    # Note: we will be using list types here (as opposed to n*1 or 1*n 2D arrays).

    if not ((type(x) == type([])) and (type(y) == type([]))):
        print("laff_copy: incorrect type for argument(s), must be lists")
        return y
    elif (len(x) != len(y)):
        print("laff_copy: argument lengths must be equal")
        return y
    else:
        for i in range(len(x)):
            y[i] = x[i]
        return y

def laff_scal(alpha, x):
    # Section 1.5.3, Homework 1.5.3.1
    # Vector SCAL routine.

    # vector laff_scal(scalar alpha, vector x)
    # Scales the vector x by a factor of alpha, returning the scaled x vector.
    # Note: x should be a list of numbers.

    if not (((type(alpha) == type(1)) or (type(alpha) == type(1.0)))
            and (type(x) == type([]))):
        print("laff_scal: incorrect type for argument(s), must be scalar & list")
        return x
    else:
        for i in range(len(x)):
            x[i] = alpha * x[i]
        return x

def laff_axpy(alpha, x, y):
    # Section 1.5.4, Homework 1.5.4.1
    # Scaled addition (AXPY) routine.

    # vector laff_axpy(scalar alpha, vector x, vector y)
    # Sets y equal to alpha*x + y, returning the new y.
    # Note: x and y should be lists of numbers.

    if not (((type(alpha) == type(1)) or (type(alpha) == type(1.0)))
            and (type(x) == type([])) and (type(y) == type([]))):
        print("laff_axpy: incorrect type for argument(s), must be scalar, list, and list")
        return y
    elif (len(x) != len(y)):
        print("laff_axpy: arguments x and y must have equal lengths")
        return y
    else:
        for i in range(len(y)):
            y[i] += alpha * x[i]
        return y

def laff_dot(x, y):
    # Section 1.5.5, Homework 1.5.5.1
    # Dot product (DOT) routine.

    # scalar laff_dot(vector x, vector y)
    # Returns the dot product of x and y.
    # Conditions: x and y are lists of numbers, len(x) == len(y)

    if not ((type(x) == type([])) and (type(y) == type([]))):
        print("laff_dot: incorrect type for argument(s), must be lists")
        return 0
    elif (len(x) != len(y)):
        print("laff_dot: arguments must have equal lengths")
        return 0
    else:
        sum = 0
        for i in range(len(x)):
            sum += x[i] * y[i]
        return sum

def laff_norm2(x):
    # Section 1.5.6, Homework 1.5.6.1
    # Vector length (NORM2) routine.

    # scalar laff_norm2(vector x)
    # Returns the Euclidean length (two-norm) of x.
    # Conditions: x is a list of numbers.

    if (type(x) != type([])):
        print("laff_norm2: incorrect type for argument, must be list")
        return -1
    else:
        sum = 0
        for i in range(len(x)):
            sum += x[i]**2
        return sum**(0.5)


