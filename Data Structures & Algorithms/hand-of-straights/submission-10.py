class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        cards = Counter(hand)
        hand.sort()

        for card in hand:
            if cards[card] > 0:
                for i in range(card, card + groupSize):
                    if cards[i] <= 0:
                        return False
                    cards[i] -= 1

        return True