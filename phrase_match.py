print("Please enter max 40 keywords, separated by commas:")
keywords = input().split(',')

quoted_keywords = [f'"{keyword.strip()}"' for keyword in keywords[:40]]

print("\nHere are your 40 quoted keywords:")
for keyword in quoted_keywords:
    print(keyword)

