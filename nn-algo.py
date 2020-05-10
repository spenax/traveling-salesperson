# Each city object includes the name of the city, a dictionary of distances to 
# nearby cities, and a single boolean to show whether the city is an orgin/terminus

class City:
    def __init__(self, name, distance_to, terminus=False):
        self.name = name
        self.terminus = terminus
        self.distance_to = distance_to
        
 
r = City("Rockville", {"Rockville": 0, "Silver Spring": 13, "Philadelphia": 225, "Pittsburgh": 225, "Baltimore": 40, "Cleveland": 352, "New York City": 227 }, True)
s = City("Silver Spring", {"Rockville": 13, "Silver Spring": 0, "Philadelphia": 136, "Pittsburgh": 237, "Baltimore": 34, "Cleveland": 363, "New York City": 222 })
ph = City("Philadelphia", {"Rockville": 141, "Silver Spring": 135, "Philadelphia": 0, "Pittsburgh": 305, "Baltimore": 101, "Cleveland": 432, "New York City": 97 })
pt = City("Pittsburgh", {"Rockville": 226, "Silver Spring": 237, "Philadelphia": 304, "Pittsburgh": 0, "Baltimore": 248, "Cleveland": 133, "New York City": 371 })
b = City("Baltimore", {"Rockville": 40, "Silver Spring": 34, "Philadelphia": 106, "Pittsburgh": 248, "Baltimore": 0, "Cleveland": 374, "New York City": 192 })
c = City("Cleveland", {"Rockville": 352, "Silver Spring": 364, "Philadelphia": 431, "Pittsburgh": 133, "Baltimore": 375, "Cleveland": 0, "New York City": 462 })
n = City("New York City", { "Rockville": 228, "Silver Spring": 222, "Philadelphia": 97, "Pittsburgh": 370, "Baltimore": 188, "Cleveland": 462, "New York City": 0 })

# A route is an ordered list of locations. In the above set, Rockville is the terminus.

class Route:
    def __init__(self,cities):
        self.cities = cities


# Pathfinding algorithm function takes an unsorted set of cities and a list representing a route 
# As the ordered route is built up based on each alogorithm, the size of the unordered set of cites set goes down.

def nn_algo(unordered_cities, route=[]):

    #end condition
    if len(unordered_cities) == 0:
        
        for destination in route:
            print(destination.name)
        return route
    
    #find orgin city and add to route
    elif len(route) ==  0:
        route=[]
        #find start city
        origin = list(filter(lambda x: x.terminus == True, unordered_cities))[0]
        #add to route
        route.append(origin)
        #add final destination
        route.append(origin)
        unordered_cities.remove(origin)
        nn_algo(unordered_cities, route)
    
    #find subsequent destination and add to route
    else:
        #find the penultimate city in the route (i.e. travelled to before returning home)
        current = route[-2]
        distances = current.distance_to
        city_names = list(map(lambda elem: elem.name, unordered_cities))
        remaining_city_distances = dict(filter(lambda elem: elem[0] in city_names, distances.items()))
        next_city_name = min(remaining_city_distances, key = lambda k: remaining_city_distances[k])
            
        for city in unordered_cities:
            if city.name == next_city_name:
                next_city = city
        route.insert(-1,next_city)
        #insert before the terminus
        unordered_cities.remove(next_city)
        nn_algo(unordered_cities, route)


# The distance functions accepts and ordered list as input and out puts distance starting from the end of the list
# and moving towards the beginning of the list. The last line is the sum, or total distance for a route

def distance(cities,total=0):

    legs = len(cities) - 1
    if legs < 1:
        print(total)
    else:
        destination = cities[legs]
        prev = legs - 1
        origin = cities[prev]
        miles = origin.distance_to[destination.name]


        #print(miles)
        #Uncomment to see iteration
        total += miles

        cities.pop() #remove last city from list
        distance(cities,total) 


SET_ONE = {n,c,b,r,pt,ph,s}
SET_THREE = {r,n,c,pt,ph}
SET_FIVE = {r,s,c,b,ph}

print("*************************************")
print("Test 1: Deliveries to NYC, Cleveland, Baltimore, Pittsburgh, Philadelphia, and Silver Spring")
print("*************************************")
print("📍Route for Nearest Neighbor Algorithm:")
nn_algo(SET_ONE,[])
print("🚚 Total distance travelled:")
distance([r,s,b,ph,n,pt,c,r],0)

print("*************************************")
print("Test 2: Deliveries to NYC, Cleveland, Pittsburgh, Philadelphia")
print("*************************************")
print("📍Route for Nearest Neighbor Algorithm:")
nn_algo(SET_THREE,[])
print("🚚 Total distance travelled:")
distance([r,ph,n,pt,c,r],0)

print("*************************************")
print("Test 3: Deliveries to Silver Spring, Cleveland, Baltimore, Philadelphia")
print("*************************************")
print("📍Route for Nearest Neighbor Algorithm:")
nn_algo(SET_FIVE,[])
print("🚚 Total distance travelled:")
distance([r,s,b,ph,c,r],0)
