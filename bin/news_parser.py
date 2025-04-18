#!/usr/bin/env python3
##############################################################################
# Copyright(c) 2025 steadfasterX <steadfasterX #AT# binbash |dot| rocks>
# License: GPLv3
#
# Parse Arch News (or any other) feed
#
##############################################################################

import argparse
import feedparser
from datetime import datetime, timedelta
import html
import re
import sys


def parse_news_feed(feed_url, days=14, output_format="text", debug=False):
    # Fetch and parse the RSS feed
    feed = feedparser.parse(feed_url)

    # Check for errors in the feed
    if feed.bozo:
        if debug:
            error_message = re.sub(r"<[^>]+>", "", str(feed.bozo_exception))
            feed_summary = re.sub(r"<[^>]+>", "", feed.feed.get("summary", "No summary available"))
            print(f"Error parsing feed: {error_message}", file=sys.stderr)
            print(f"Status: {feed.status if 'status' in feed else 'Unknown'}", file=sys.stderr)
            print(f"Feed summary: {feed_summary}", file=sys.stderr)
        sys.exit(3)

    # Calculate the date threshold
    date_threshold = datetime.now() - timedelta(days=days)

    # Prepare results
    results = []

    # Iterate over feed entries
    for entry in feed.entries:
        # Parse the published date
        published_date = datetime(*entry.published_parsed[:6])
        if published_date < date_threshold:
            continue

        title = entry.title
        link = entry.link
        description = html.unescape(entry.description)

        # Condense the description to XX characters
        description_summary = re.sub(r"<[^>]+>", "", description)  # Remove HTML tags
        if len(description_summary) > 200:
            description_summary = description_summary[:190] + " [...]"

        # Format output based on output format
        if output_format == "text":
            underline = "-" * (len(title) + 3)
            results.append(f"{title}\n{underline}\nFull description: {link}\n{description_summary}\n")
        elif output_format == "html":
            results.append(
                f"<h2><u>{title}</u></h2>\n"
                f"<i>{description_summary}</i>"
                f' <a href="{link}">(full description)</a>\n'
            )

    return results


def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Parse an RSS feed and show all titles as clickable links.")
    parser.add_argument("--days", type=int, default=14, help="Number of days to look back for titles.")
    parser.add_argument("--feed-url", default="https://archlinux.org/feeds/news", help="RSS feed URL to parse.")
    parser.add_argument("--html", action="store_true", help="Output in HTML format.")
    parser.add_argument("--text", action="store_true", help="Output in plain text format (default).")
    parser.add_argument("--debug", action="store_true", help="Enable debugging output for errors.")
    args = parser.parse_args()

    # Determine output format (default to text)
    output_format = "html" if args.html else "text"

    # Parse the feed
    try:
        results = parse_news_feed(args.feed_url, args.days, output_format, args.debug)
    except Exception as e:
        if args.debug:
            print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(3)

    # Print the results
    if results:
        print("\n".join(results))
    else:
        print("No news titles found.")


if __name__ == "__main__":
    main()
