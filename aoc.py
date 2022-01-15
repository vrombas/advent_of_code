def read_planned_course(filename):
    return [x.strip('\n').split(' ') for x in open(filename, 'r')]

def read_file(filename):
    return [x.strip('\n') for x in open(filename, 'r')]