class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, new_name):
        self.new_name = new_name
        print("The new name of the student is", new_name)
    
    def change_age(self, new_age):
        self.new_age = new_age
        print("The new age of the student is", new_age)

    def add_track(self, newtrack):
        self.newtrack = newtrack
        self.tracks.append(newtrack)
        print("The new tracks of the student is", self.tracks)

    def get_score(self):
        print("The student score remains", self.score)

        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()



# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
