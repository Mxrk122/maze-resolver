from problem import Problem
from path import Path

def remove_choice(arr: list, type: int = None):
    if type == 0 or type == None:
        #Breadth first search
        return arr.pop()
    elif type == 1:
        #depth first search
        

def is_not_explored(result, explored):
    if result not in explored:
        return True
    else:
        return False

def graph_search(problem: Problem):
    frontier =  [Path([problem.initial_state])]
    explored = []

    hi = True
    while hi:
        if len(frontier):
            path = remove_choice(frontier)
            
            s = path.end()

            explored.append(s)

            if problem.goalTest(s):
                print(len(frontier))
                return path
            
            for a in problem.actions(s):
                result = problem.results(s, a)

                if is_not_explored(result, explored):
                    new_path = Path([])
                    new_path.extendFrom(path)
                    new_path.addStep(result)
                    frontier.append(new_path)
        else:
            hi = False
    


