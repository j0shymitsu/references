def check_ingredient_match(recipe, ingredients):
    item_total = len(recipe)
    player_total = 0
    missing_ingredients = []

    
    for item in recipe:
        if item not in ingredients:
            missing_ingredients.append(item)
        else:
            player_total += 1

    return (player_total/item_total) * 100, missing_ingredients