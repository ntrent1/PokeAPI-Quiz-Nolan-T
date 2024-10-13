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

# Function to compare two Pokémon stats
def compare_stats(pokemon1, pokemon2):
    print(f"\nComparing {pokemon1['name'].capitalize()} and {pokemon2['name'].capitalize()}:\n")
    
    # Define the stats you want to compare (e.g., HP, Attack, Defense, etc.)
    stat_names = ['hp', 'attack', 'defense', 'speed']
    
    # Ask questions comparing stats
    for stat in stat_names:
        stat1 = next((s['base_stat'] for s in pokemon1['stats'] if s['stat']['name'] == stat), None)
        stat2 = next((s['base_stat'] for s in pokemon2['stats'] if s['stat']['name'] == stat), None)
        
        if stat1 and stat2:
            print(f"Which Pokémon has a higher {stat}?")
            answer = input(f"Type '1' for {pokemon1['name']} or '2' for {pokemon2['name']}: ")
            if (answer == '1' and stat1 > stat2) or (answer == '2' and stat2 > stat1):
                print("Correct!\n")
            else:
                print(f"Incorrect. {pokemon1['name']} has {stat1} {stat}, and {pokemon2['name']} has {stat2} {stat}.\n")

# Main function to run the program
def main():
    # Get two random Pokémon (use Pokémon IDs from 1 to 1010)
    pokemon1_id = random.randint(1, 1010)
    pokemon2_id = random.randint(1, 1010)
    
    # Fetch Pokémon data
    pokemon1 = get_pokemon_data(pokemon1_id)
    pokemon2 = get_pokemon_data(pokemon2_id)
    
    if pokemon1 and pokemon2:
        # Compare their stats
        compare_stats(pokemon1, pokemon2)
    else:
        print("Failed to retrieve Pokémon data. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
