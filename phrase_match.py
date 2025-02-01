print("Please enter max 30 keywords, separated by commas:")
keywords = input().split(',')

quoted_keywords = [f'"{keyword.strip()}"' for keyword in keywords[:30]]

print("\nHere are your 30 quoted keywords:")
for keyword in quoted_keywords:
    print(keyword)

