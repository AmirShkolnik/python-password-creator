def generate_phrase_match():
    keywords = input("Enter keywords separated by commas: ").split(",")
    phrase_match_list = [f'"{keyword.strip()}"' for keyword in keywords]
    
    print("\nBing Ads Phrase Match Keywords:")
    for phrase in phrase_match_list:
        print(phrase)

# Run the function
generate_phrase_match()