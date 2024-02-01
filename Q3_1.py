class Q3_1:
    def f1(self, a, start): 
        #a is the adjacency matrix representing the given graph
        # start is a starting point
        with open("f1.txt", "w") as f1_file:
            self.depthFirstWithDegrees(a, start, f1_file)

    def depthFirstWithDegrees(self, a, start, output_file):
        b = [True] * len(a)
        b[start] = False
        self.depth(a, start, b, output_file)

        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth(a, i, b, output_file)

    def depth(self, a, start, b, output_file):
        t = self.deg(a, start)
        output_file.write(f"{chr(start + 65)} ({t}) ") 
        for i in range(len(b)):
            if a[start][i] != 0 and b[i]:
                b[i] = False
                self.depth(a, i, b, output_file)

    def deg(self, a, x):
        count = 0
        for i in range(len(a)):
            count += a[x][i]
        return count
        pass
        