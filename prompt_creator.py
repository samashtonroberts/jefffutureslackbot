from random import seed
from random import choice

future = ["User Experience", "Beautiful", "Bizarre", "Bright", "Fast", "Depressing", "Fair", "Feminist", "Free", "Global", "Grassroots", "Green", "High-tech", "Hilarious", "Innovative", "Joyful", "Mundane", "Noir", "Playful", "Queer", "Reactionary", "Recovering", "Regimented", "Resilient", "Sad", "Decolonized", "Scary", "Selfish", "Smart", "Sterile", "Thrilling", "Volatile", "Wild", "Wise", "Creative"]
thing = ["Magic Spell", "Website", "Weapon", "Video", "Tool", "Tattoo", "Song", "Ritual", "Public Service Announcement", "Product", "Poster", "Plaything", "Organization", "News Report", "Monument", "Mask", "Map", "Machine", "Law", "Job", "Invention", "Heirloom", "Headline", "Garment", "Game", "Food", "Flag", "Festival", "Drug", "Disaster", "Device", "D.I.Y. Kit", "Breakthrough", "Bestseller", "App"]
theme = ["Funk", "Soulful Crooning", "Animals", "Artificial Intelligence", "Cities", "Education", "Death", "The Economy", "Energy", "The Environment", "Family", "Farming", "Genetics", "Governance", "Health", "Identity", "Imagination", "Justice", "Leisure", "Love", "Memory", "Money", "The Ocean", "Religion", "Resources", "Science", "Climate Change", "Space", "Spirituality", "Storytelling", "Surveillance", "Transportation", "War", "Water", "Work", "Class"]

def writeprompt():
    promptfuture = choice(future)
    promptthing = choice(thing)
    prompttheme = choice(theme)
    prompt = "In Jeff and Kiki's {} future, there is a {} related to {}. What is it?"
    return(prompt.format(promptfuture, promptthing, prompttheme))
