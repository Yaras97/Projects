class Gun:
    def __init__(self):
        self.count = 0
        self.pif = ['pif', 'paf']

    def shoot(self):
        print(self.pif[self.count % 2])
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0

gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())