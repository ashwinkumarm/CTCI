class Tower:
    def __init__(self):
        self.disks = []

    def add(self, d):
        if len(self.disks) != 0 and self.disks[-1] <= d:
            print("Cant, Higher value")
        else:
            self.disks.append(d)

    def move_top(self, t):
        td = self.disks.pop()
        t.add(td)

    def move_disks(self, d, b, n):
        if n > 0:
            self.move_disks(b, d, n-1)
            self.move_top(d)
            b.move_disks(d, self, n-1)


def main():
    o = Tower()
    b = Tower()
    d = Tower()

    n = 10
    for disk in range(n-1, -1, -1):
        o.add(disk)

    o.move_disks(d, b, n)

    print(o.disks)
    print(d.disks)
    print(b.disks)

main()
