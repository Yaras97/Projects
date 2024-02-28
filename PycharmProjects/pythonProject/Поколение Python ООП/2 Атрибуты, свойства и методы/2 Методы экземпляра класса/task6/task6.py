class Gun:
    def __init__(self):
        self.stack = ['pif', 'paf']
        self.count = 0

    def shoot(self):
        print(self.stack[self.count % 2])
        self.count += 1

gun = Gun()
gun.shoot()