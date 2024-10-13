carbon_footprint = {
    "food": 0,
    "shelter": 0,
    "goods": 0,
    "mobility": 0,
    "services": 0
}

def get_user_input():
    print("Enter your annual footprint from the link for the following categories:")
    for category in carbon_footprint:
        while True:
            try:
                value = float(input(f"{category.capitalize()}: "))
                if value < 0:
                    raise ValueError("Value cannot be negative.")
                carbon_footprint[category] = value
                break
            except ValueError as e:
                print(f"Invalid input. {e}")

def get_top_contributors():
    sorted_footprint = sorted(carbon_footprint.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_footprint[:3]
    return top_3

def suggest_reduction(category):
    suggestions = {
        "food": "Reduce meat and dairy consumption, opt for locally sourced and seasonal foods.",
        "shelter": "Improve insulation, switch to renewable energy, and use energy-efficient appliances.",
        "goods": "Buy second-hand, reduce unnecessary purchases, and recycle properly.",
        "mobility": "Use public transport, bike, carpool, or switch to electric vehicles.",
        "services": "Opt for eco-friendly services and support companies with sustainable practices."
    }
    return suggestions.get(category, "No suggestions available.")

def main():
    get_user_input()
    top_3_contributors = get_top_contributors()

    print("\nTop 3 contributors to your footprint:")
    for category, value in top_3_contributors:
        print(f"- {category.capitalize()}: {value} GHA")

    print("\nHere are some suggestions to reduce emissions:")
    for category, _ in top_3_contributors:
        print(f"- {category.capitalize()}: {suggest_reduction(category)}")

if __name__ == "__main__":
    main()
