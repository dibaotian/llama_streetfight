import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings

    game = Game(
        render=True,
        save_game=True,
        player_1=Player1(
            nickname="minxie",
            model="ollama:llama3",
            # model="ollama:mistral",
        ),
        player_2=Player2(
            nickname="xiemin",
            model="ollama:llama2",
            # model="ollama:mistral",
        ),
    )

    game.run()
    return 0


if __name__ == "__main__":
    main()
