def display_info(**details):
    for key, value in details.items():
        print(key, ":", value)

display_info(
    name="Apoorv",
    age=20,
    branch="AI & Data Science",
    college="MIT"
)
