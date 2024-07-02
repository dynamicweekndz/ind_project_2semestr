#Основной класс, управляющий игрой(Логика игры):
class CardGame:
    MAX_TURNS = 10**6

    def __init__(self, player1_cards, player2_cards):
        self.player1 = Player("first", player1_cards)
        self.player2 = Player("second", player2_cards)
        self.turns = 0

    def play(self):
        while self.player1.has_cards() and self.player2.has_cards() and self.turns < self.MAX_TURNS:
            self.turns += 1
            card1 = self.player1.draw_card()
            card2 = self.player2.draw_card()
            
            if self.is_card1_winner(card1, card2):
                self.player1.add_cards([card1, card2])
            else:
                self.player2.add_cards([card1, card2])
        
        if self.turns >= self.MAX_TURNS:
            print("botva")
        elif self.player1.has_cards():
            print(f"{self.player1.name} {self.turns}")
        else:
            print(f"{self.player2.name} {self.turns}")
#Специальное правило, где карта 0 побеждает карту 9
    def is_card1_winner(self, card1, card2):
        # Special rule where 0 beats 9
        if (card1 == 0 and card2 == 9):
            return True
        elif (card2 == 0 and card1 == 9):
            return False
        return card1 > card2

#Класс, описывающий игрока и его колоду карт(в т.ч. действия с ней)
class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def has_cards(self):
        return len(self.cards) > 0

    def draw_card(self):
        return self.cards.pop(0)

    def add_cards(self, cards):
        self.cards.extend(cards)
#Функция проверяет корректность ввода
def read_input():
    try:
        player1_cards = list(map(int, input("Введите карты первого игрока: ").split()))
        player2_cards = list(map(int, input("Введите карты второго игрока: ").split()))

        if len(player1_cards) != 5 or len(player2_cards) != 5:
            raise ValueError("Каждый игрок должен иметь ровно 5 карт.")
        
        return player1_cards, player2_cards
    except ValueError as e:
        print(f"Некорректный ввод: {e}")
        return read_input()
#Функция запускает игру, читая входные данные и создавая объект CardGame
def main():
    player1_cards, player2_cards = read_input()
    game = CardGame(player1_cards, player2_cards)
    game.play()

if __name__ == "__main__":
    main()
