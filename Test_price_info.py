import price_info

def test_total_cost_shopping():
    result=46.75
    assert(result==price_info.total_cost_shopping())

def test_cost_of_fruit():
    result = 1.20 * 10
    assert(result==price_info.cost_of_fruits('apple',10))

