#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    pokemon = requests.get(f"{POKEURL}")
    pokemon = pokemon.json()

    ## export to excel with pandas
    # make a dataframe from our data
    pokemondf = pandas.DataFrame(pokemon)
    
    print(pokemondf.results)   # show the first 5 entries in the df



    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    pokemondf.to_excel("pokemon.xlsx", index=False)

    pokemondf.to_csv("pokemon.csv")

    pokemondf.to_json("pokemon.json")



    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('--searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()

