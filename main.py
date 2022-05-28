class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print(f" Old Data: name = \"{name}\", age = {age}, tracks = {tracks}, score = {score}")

    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        self.age = age
        return self.age

    def add_track(self, tracks):
        self.tracks = tracks
        return self.tracks

    def get_score(self):
        return float(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name(str("Peter"))
Bob.change_age(int(34))
Bob.add_track(list(["UI/UX", "Python"]))
Bob.get_score()

print(f" New Data: name = \"{Bob.name}\", age = {Bob.age}, tracks = {Bob.tracks}, score = {Bob.score}")
print(input("Press Enter to Terminate"))