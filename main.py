import requests
import random

# Function to get Pokémon data from the PokeAPI
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for Pokémon ID: {pokemon_id}")
        return None

# Function to compare a random stat between two Pokémon
def compare_random_stat(pokemon1, pokemon2):
    # Define the stats you want to compare (e.g., HP, Attack, Defense, etc.)
    stat_names = ['hp', 'attack', 'defense', 'speed','special-attack', 'special-defense']
    
    # Randomly choose a stat
    random_stat = random.choice(stat_names)
    
    # Get the stat values for both Pokémon
    stat1 = next((s['base_stat'] for s in pokemon1['stats'] if s['stat']['name'] == random_stat), None)
    stat2 = next((s['base_stat'] for s in pokemon2['stats'] if s['stat']['name'] == random_stat), None)
    
    if stat1 and stat2:
        print(f"\nWhich Pokémon has a higher {random_stat.replace('-', ' ')}?\n")  # Replacing '-' with ' ' for better readability
        print(f"1. {pokemon1['name'].capitalize()}")
        print(f"2. {pokemon2['name'].capitalize()}")
        
        # Loop until a valid response is given
        while True:
            answer = input(f"Type '1' for {pokemon1['name']} or '2' for {pokemon2['name']}: ")
            if answer in ['1', '2']:
                break
            else:
                print("Invalid input. Please type '1' or '2'.")
        
        # Reveal the correct answer and stats
        if (answer == '1' and stat1 > stat2) or (answer == '2' and stat2 > stat1):
            print("Correct!\n")
        else:
            print("Incorrect.\n")
        
        print(f"{pokemon1['name'].capitalize()} has {stat1} {random_stat.replace('-', ' ')}, and {pokemon2['name'].capitalize()} has {stat2} {random_stat.replace('-', ' ')}.\n")
    else:
        print(f"Couldn't retrieve the {random_stat.replace('-', ' ')} for one of the Pokémon.")


# Main function to run the program
def main():
    while True:
        # Get two random Pokémon (use Pokémon IDs from 1 to 1010)
        pokemon1_id = random.randint(1, 1010)
        pokemon2_id = random.randint(1, 1010)
        
        # Fetch Pokémon data
        pokemon1 = get_pokemon_data(pokemon1_id)
        pokemon2 = get_pokemon_data(pokemon2_id)
        
        if pokemon1 and pokemon2:
            # Compare a random stat between the Pokémon
            compare_random_stat(pokemon1, pokemon2)
        else:
            print("Failed to retrieve Pokémon data. Please try again.")
        
        # Ask if the user wants to compare another stat with new Pokémon
        play_again = input("Do you want to compare another stat with new Pokémon? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the program
if __name__ == "__main__":
    main()
