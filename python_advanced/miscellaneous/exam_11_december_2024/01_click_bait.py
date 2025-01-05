from collections import deque


def print_results(engagement_value, target, feed):
    print(f"Final Feed: {', '.join(str(x) for x in feed)}")

    if engagement_value >= target:
        print(f"Goal achieved! Engagement Value: {engagement_value}")
    else:
        print(f"Goal not achieved! Short by: {target - engagement_value}")

def main():
    suggested_links = deque(int(x) for x in input().split())
    featured_articles = [int(x) for x in input().split()]
    target_engagement = int(input())

    final_feed = []

    while suggested_links and featured_articles:
        link = suggested_links.popleft()
        article = featured_articles.pop()

        if link > article:
            greater, smaller, origin = link, article, "FIFO"
        elif link < article:
            greater, smaller, origin = article, link, "LIFO"
        else:
            final_feed.append(0)
            continue

        remainder = greater % smaller

        if origin == "LIFO":
            final_feed.append(remainder)

            if remainder != 0:
                featured_articles.append(remainder * 2)
        else:
            final_feed.append(-remainder)

            if remainder != 0:
                suggested_links.append(remainder * 2)

    total_engagement = sum(final_feed)
    print_results(total_engagement, target_engagement, final_feed)

if __name__ == '__main__':
    main()
