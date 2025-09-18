import re

def mask_credit_card(card_number):
    if not isinstance(card_number, str):
        return "Invalid Card"
    if not re.fullmatch(r"\d{16}", card_number):
        return "Invalid Card"
    return '*' * 12 + card_number[-4:]

def mask_credit_cards(card_numbers):
    """
    Takes a list of card numbers and returns a list of masked/invalid results.
    """
    return [mask_credit_card(num) for num in card_numbers]

card = "1234567812345678"
print(mask_credit_card(card))  


def test_mask_credit_card():
   
    assert mask_credit_card("1234567812345678") 

    assert mask_credit_card("1234abcd12345678") 
    
    assert mask_credit_card("12345678123456789") 
    assert mask_credit_card("1234-5678-1234-5678") 
 
    assert mask_credit_card(1234567812345678)

def test_mask_credit_cards():
    cards = [
        "1234567812345678",   
        "1111222233334444",   
        "abcd123456789012",   
        "12345678",          
        "12345678123456789"   
    ]
    expected = [
        "************5678",
        "************4444",
        "Invalid Card",
        "Invalid Card",
        "Invalid Card"
    ]
    assert mask_credit_cards(cards) == expected

# Run tests
test_mask_credit_card()
test_mask_credit_cards()
print("All tests passed.")