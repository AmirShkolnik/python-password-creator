print("Please enter 20 keywords, separated by commas:")
keywords = input().split(',')

quoted_keywords = [f'"{keyword.strip()}"' for keyword in keywords[:20]]

print("\nHere are your 20 quoted keywords:")
for keyword in quoted_keywords:
    print(keyword)

