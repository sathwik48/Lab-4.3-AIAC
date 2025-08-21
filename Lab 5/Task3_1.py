# Simple product recommendation based on user search history

# Sample product categories and recommendations
recommendations = {
    "soap": ["Shampoo", "Body Wash", "Hand Sanitizer"],
    "mobile": ["Mobile Case", "Screen Protector", "Earphones"],
    "toys": ["Board Games", "Action Figures", "Puzzles"],
    "games": ["Game Console", "Video Games", "Game Accessories"],
    "laptop": ["Laptop Bag", "Mouse", "Keyboard"],
    "book": ["Notebook", "Bookmark", "Pen"]
}

def recommend_products(search_term):
    search_term = search_term.lower()
    for key in recommendations:
        if key in search_term:
            print(f"Based on your search for '{search_term}', you might also like:")
            for item in recommendations[key]:
                print(f"- {item}")
            return
    print("No recommendations found for your search.")

if __name__ == "__main__":
    user_search = input("Enter your product search: ")
    recommend_products(user_search)