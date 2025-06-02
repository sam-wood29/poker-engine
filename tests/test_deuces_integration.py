from deuces import Card, Deck, Evaluator # type: ignore

def test_deuces_hand_evaluation():
    deck = Deck()
    board = [deck.draw(), deck.draw(), deck.draw()]
    hand = [deck.draw(), deck.draw()]

    evaluator = Evaluator()
    score = evaluator.evaluate(hand, board)
    print(score)
    rank_class = evaluator.get_rank_class(score)
    print(rank_class)

    assert isinstance(score, int)
    assert 1 <= score <= 7462
    assert isinstance(rank_class, int)