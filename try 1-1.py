# Init Variables
thematrix = ""
system = ""
neo = ""
enemy = ""
look = ""
people = ""
protect = ""

profession = ["","","",""]

# Get Input From User
print("Welcome Player!")

print("Who Wants To Play Some MadLibs")

print("You Do, Obviously.")
user = input("Type Your Name To Begin; ")

# Get TheMatrix Variable From User
print(f"Why Hello There {user}, Hope You're Ready!")
thematrix = input("What Is Something You Love With All Of Your Heart: ")

# Get The System Variable From User
print(f"So You Like {thematrix} Huh?")
system = input(f"Whats Something You Just Hate: ")

# Get The Enemy Variable From User
enemy = input(f"And What Is The Opposite Of {system}; ")

# Get The Neo Variable From User
neo = input(f"Best Insult You Can Think Of: ")

# Get The Look Variable From User
look = input(f"Now Give Me A Verb: ")

# Get The People Variable From User
people = input(f"And Now A Noun: ")

# Get The Protect Variable From User
protect = input(f"Another Verb Please: ")

# Get Professions
print(f"Now I'm Going To Need Four Job Types You Would Not Want")

for i in range(len(profession)):
    profession[i] = input(f"profession (plural) {i+1} / {len(profession)}: ")


# Init Story

print(f"I Hope You're Ready {user}...")

input()

story = (f"{thematrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're inside, you {look} around, what do you see? " +
f"{profession[0]},{profession[1]}, {profession[2]}, {profession[3]}.The very minds " +
f"of the {people} we are trying to save. But until we do, " +
f"these {people} are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these {people} " +
f"are not ready to be unplugged. And many of them are so stupid, " +
f"so hopelessly uneducated on the {system}, that they will fight to {protect} it.")

# Print Story

print(story)
input()

print(f"Well {user}, I Hope You Had As Much Fun As I Did. Good Bye :)")
input()

