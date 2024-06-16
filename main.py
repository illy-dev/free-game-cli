import requests
import typer
from rich import print
from typing_extensions import Annotated
from typing import Optional

games = {}

Questions = ['Which Platform?\n> ', 'Which Category?\n> ', 'How many Results do you want to see?\n> ']

base_url = 'https://www.freetogame.com/api/games?'

categorys_possible = 'mmorpg, shooter, strategy, moba, racing, sports, social, sandbox, open-world, survival, pvp, pve, pixel, voxel, zombie, turn-based, first-person, third-Person, top-down, tank, space, sailing, side-scroller, superhero, permadeath, card, battle-royale, mmo, mmofps, mmotps, 3d, 2d, anime, fantasy, sci-fi, fighting, action-rpg, action, military, martial-arts, flight, low-spec, tower-defense, horror, mmorts'

platforms_possible = 'pc, browser, all'

def HowManyResults():
    results = input(Questions[2])

    if len(results) > 0:
        return int(results)

    else:
        print('[bold]No amount of Results provided[/bold][red] defaulting to 1[/red]')
        return 1

def FindPlatform():
    platform = input(Questions[0])

    if len(platform) > 0:
        url_platform = f'&platform={platform}'
        return url_platform

    else:
        print('[bold]No Platform provided[/bold]')
        return ''

def FindCategory():
    category = input(Questions[1])

    if len(category) > 0:
        url_category = f'&category={category}'
        return url_category

    else:
        print('[bold]No Category provided[/bold]')
        return ''


def main(options: Annotated[Optional[str], typer.Argument(help="Get options for [categorys] or [platforms]")] = None):
    if options is None:
        print('Find out which Free To Play Game is perfect for you!')

        url = base_url + FindPlatform() + FindCategory()

        response = requests.get(url)
    
        for i in range(HowManyResults()):
            games["Game {0}".format(i + 1)] = response.json()[i] 
        print(games)

    elif options == 'platforms':
        print(f'Platforms:\n{platforms_possible}')
    elif options == 'categorys':
        print(f'Categorys:\n{categorys_possible}')


if __name__ == '__main__':
    typer.run(main)
