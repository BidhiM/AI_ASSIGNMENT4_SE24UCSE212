# List of Telangana districts (33)
districts = [
    "Adilabad", "Bhadradri_Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar_Bhupalpally", "Jogulamba_Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Komaram_Bheem", "Mahabubabad", "Mahabubnagar", "Mancherial",
    "Medak", "Medchal_Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda",
    "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna_Sircilla",
    "Ranga_Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
    "Wanaparthy", "Warangal_Rural", "Warangal_Urban", "Yadadri_Bhuvanagiri"
]

# Adjacency list (partial realistic approximation for demo)
neighbors = {
    "Adilabad": ["Komaram_Bheem", "Nirmal", "Mancherial"],
    "Komaram_Bheem": ["Adilabad", "Mancherial"],
    "Mancherial": ["Adilabad", "Komaram_Bheem", "Peddapalli"],
    "Nirmal": ["Adilabad", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Medak"],
    "Medak": ["Kamareddy", "Sangareddy", "Siddipet"],
    "Sangareddy": ["Medak", "Ranga_Reddy", "Vikarabad"],
    "Ranga_Reddy": ["Hyderabad", "Sangareddy", "Vikarabad"],
    "Hyderabad": ["Ranga_Reddy", "Medchal_Malkajgiri"],
    "Medchal_Malkajgiri": ["Hyderabad", "Yadadri_Bhuvanagiri"],
    "Yadadri_Bhuvanagiri": ["Medchal_Malkajgiri", "Nalgonda"],
    "Nalgonda": ["Yadadri_Bhuvanagiri", "Suryapet"],
    "Suryapet": ["Nalgonda", "Khammam"],
    "Khammam": ["Suryapet", "Mahabubabad"],
    "Mahabubabad": ["Khammam", "Warangal_Rural"],
    "Warangal_Rural": ["Mahabubabad", "Warangal_Urban"],
    "Warangal_Urban": ["Warangal_Rural", "Jangaon"],
    "Jangaon": ["Warangal_Urban", "Siddipet"],
    "Siddipet": ["Jangaon", "Medak"],
    # Remaining can be loosely connected or left minimal
}

# Colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Assignment dictionary
assignment = {}

# Check if assignment is valid
def is_valid(district, color):
    for neighbor in neighbors.get(district, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(index):
    if index == len(districts):
        return True

    district = districts[index]

    for color in colors:
        if is_valid(district, color):
            assignment[district] = color
            if backtrack(index + 1):
                return True
            del assignment[district]

    return False

# Run CSP
if backtrack(0):
    print("District Coloring:\n")
    for d in districts:
        print(f"{d} --> {assignment[d]}")
else:
    print("No solution found")