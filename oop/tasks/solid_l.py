class Bird:
    def speak(self):
        print("Tweet!")

class Sparrow(Bird):
    def speak(self):
        print("Sparrow says: Chirp Chirp!")

class Pigeon(Bird):
    def speak(self):
        print("Pigeon says: Chirp Chirp!")

if __name__ == "__main__":
    bird = Bird()
    sparrow = Sparrow()
    pigeon = Pigeon()

    zoo = [bird, sparrow, pigeon]

    for animal in zoo:
        animal.speak()