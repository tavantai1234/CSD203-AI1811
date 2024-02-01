class Q3_2:
    def f2(self, a, start): 
        #a is the adjacency matrix representing the given graph
        # start is a starting point
        with open("f2.txt", "w") as f2_file:
            self.findEulersCycle(a, start, f2_file)

    def findEulersCycle(self, a, start, output_file):
        stack = Stack()
        euler_cycle = []

        stack.push(start)

        while not stack.is_empty():
            r = stack.top()
            neighbors = [i for i in range(len(a[r])) if a[r][i] != 0]

            if not neighbors:
                stack.pop()
                euler_cycle.append(r)
            else:
                y = min(neighbors)
                stack.push(y)
                a[r][y] = 0  

        euler_cycle.reverse()

        for node in euler_cycle:
            output_file.write(f"{chr(node + 65)} ")
        output_file.write("\n")
        pass
        