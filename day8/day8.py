from collections import defaultdict

def day8(part2):
    with open('input.txt') as f:
        points = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]
    
    # Sorted distances for each possible couple
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((d, i, j))
    distances = sorted(distances)
    
    # Union - Find. Init: Each point is a disjoint set.
    parents = [i for i in range(len(points))]
    
    # Climb to the leader, i.e. to the point which is leader of itself.
    def find_set(p : int):
        if p == parents[p]:
            return p
        return find_set(parents[p])
    
    # Merge sets: Make a leader the child of another leader.
    def union_sets(p1 : int, p2 : int):
        pp1 = find_set(p1)
        pp2 = find_set(p2)
        if (pp1 != pp2):
            parents[pp2] = pp1
            return True
        return False

    if part2:
        # Will stop when == len(points)-1, i.e. 1 connection remaining before single circuit.
        connections = 0
        for i, (d, p1, p2) in enumerate(distances):
            if union_sets(p1, p2):
                connections += 1
            # 1 connection remaining before 1 single big circuit.
            if connections == len(points) - 1:
                return points[p1][0] * points[p2][0]
    else:
        # For part 1
        # How many times will union/merge?
        max_connections = 1000
        # Top most connected for part1
        highest = 3
        
        for i, (d, p1, p2) in enumerate(distances):
            if i < max_connections:
                union_sets(p1, p2)
        
        set_size = defaultdict(int)
        for i in range(len(points)):
            root = find_set(i)
            set_size[root] += 1
        connections = sorted(set_size.values(), reverse = True)

        product_highest = 1
        for i in range(highest):
            product_highest *= connections[i]
        return product_highest

if __name__ == '__main__':
    print(day8(False))
    print(day8(True))