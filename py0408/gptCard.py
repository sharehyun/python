import random

# 카드 클래스
class Card:
    shapes = ["CLOVER", "HEART", "DIAMOND", "SPADE"]
    numbers = ["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, shape: int, number: int):
        self.shape = shape
        self.number = number

    def __str__(self):
        return f"[ {Card.shapes[self.shape]}, {Card.numbers[self.number]} ]"

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number


# 덱 클래스
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(52):
            shape = i // 13
            number = i % 13 + 1
            self.cards.append(Card(shape, number))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count):
        dealt_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt_cards


# 플레이어 클래스
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand = cards

    def show_hand(self):
        print(f"[ {self.name} 카드 ]")
        for card in self.hand:
            print(card)
        print()

    def compare_with(self, other_player):
        result = []
        for my_card, your_card in zip(self.hand, other_player.hand):
            if my_card > your_card:
                result.append(2)
            elif my_card < your_card:
                result.append(1)
            else:
                result.append(0)
        return result


# 게임 클래스
class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("내")
        self.player2 = Player("상대")

    def deal_cards(self):
        self.player1.receive_cards(self.deck.deal(5))
        self.player2.receive_cards(self.deck.deal(5))

    def play(self):
        self.deal_cards()
        self.player1.show_hand()
        self.player2.show_hand()

        result = self.player1.compare_with(self.player2)

        print("[ 승부 결과 요약 ]")
        print(f"승리: {result.count(2)}, 패배: {result.count(1)}, 무승부: {result.count(0)}\n")

        print("[ 내가 이긴 카드 ]")
        for i, r in enumerate(result):
            if r == 2:
                print(self.player1.hand[i], end=" ")
        print()


# 메인 실행
if __name__ == "__main__":
    game = Game()
    game.play()
