import time

class Ant():
    
    def __init__(self,startingtown) -> None:
        self._visited = []
        self._tourlength = 0.0
        self._viabletour = True
        self._visited.append(startingtown)
    
    def move(self,newtown,distance):
        self._visited.append(newtown)
        self._tourlength = self._tourlength + distance
    
    def invalidateTour(self):
        self._viabletour = False
    
    def getTour(self) -> list:
        return self._visited
    
    def getTourLength(self) -> float:
        return self._tourlength
    
    def setTourLength(self, newlen) -> None:
        self._tourlength = newlen

    def isTourViable(self) -> bool:
        return self._viabletour
    
    def __lt__(self,other):
        if(self._tourlength<other._tourlength):
            return True
        else:
            return False

    def __gt__(self,other):
        if(self._tourlength>other._tourlength):
            return True
        else:
            return False
        
class QapAnt(Ant):
    
    def __init__(self, startingtown) -> None:
        super().__init__(startingtown)
        
    def move(self, newtown, matD, matF):
        self._visited.append(newtown)
        su = 0
        for i in range(0,len(self._visited)):
            for j in range(0,len(self._visited)):
                x = self._visited[i]
                y = self._visited[j]
                su = su + matD.item((i,j))*matF.item((x,y))
        self._tourlength = su

def makestatsfile(file_name):
    metrics_file_name = file_name
    statistics_file = open(time.strftime('%d%m%Y')+metrics_file_name,'a')
    statistics_file.write("Algorithm, Date, Population Count, alpha, beta, stagnation, best after, best, execution time, other variables \n")
    statistics_file.flush()
    return statistics_file

def observer(statistics_file ,algo, pop_count, stagnation, best_time, best_solution, exetime, args):
    argsstring = ""
    for k, v in args.items():
        argsstring = argsstring + str(k) + ' = ' + str(v) + ' |'
    statistics_file.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9} \n'.format(algo, time.strftime('%d%m%Y-%H%M%S')
                                                                        , pop_count, args['heuristic_preference']
                                                                        , args['pheromone_preference'], stagnation
                                                                        , best_time ,best_solution.getTourLength()
                                                                        , exetime, argsstring))
    statistics_file.flush()