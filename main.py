import random
import argparse

ACTIONS = [
    "танцює з", "годує", "обіймає", "фотографує", "рятує",
    "вчить літати", "малює", "співає для", "будує фортецю з",
    "винаходить", "телепортує", "перемагає", "закохується в",
    "готує суп із", "переконує", "ховається від", "обмінюється мемами з"
]

OBJECTS = [
    "динозавром", "хмарою", "кавоваркою", "своїм відображенням",
    "космічним кораблем", "гігантським кактусом", "старою бабусею",
    "магічним поні", "холодильником", "сусідом", "сонцем",
    "пакетом чіпсів", "роботом-пилососом", "деревом", "дощем", "Wi-Fi роутером"
]


def generate_pair() -> str:
    return f"{random.choice(ACTIONS)} {random.choice(OBJECTS)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор абсурдних фраз 'дія + об'єкт'")
    parser.add_argument("-c", "--count", type=int, default=8, help="Кількість фраз (default: 8)")
    args = parser.parse_args()

    print("Абсурдні ідеї / підписи для сторіз\n")
    for i in range(1, args.count + 1):
        print(f"{i:2d}. {generate_pair()}")
