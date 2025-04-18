#!/usr/bin/env python3
##############################################################################
# Copyright(c) 2025 steadfasterX <steadfasterX #AT# binbash |dot| rocks>
# License: GPLv3
#
# Parse Arch News (or any other) feed for a list of strings
#
##############################################################################

import argparse
import feedparser
from datetime import datetime, timedelta
import html
import re
import sys


def parse_package_feed(feed_url, package_list, days=14, output_format="text", debug=False):
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

        # Find matching package names in the title or description
        found_packages = [
            pkg for pkg in package_list
            if pkg.lower() in title.lower() or pkg.lower() in description.lower()
        ]
        for pkg in found_packages:
            if output_format == "text":
                results.append(f"{pkg}: {title} ({link})")
            elif output_format == "html":
                results.append(f"{pkg}: <a href='{link}'>{title}</a>")

    # Add global title only if results exist
    if results:
        if output_format == "text":
            global_title = "These packages have been mentioned on the Arch News page"
            underline = "-" * (len(global_title) + 4)
            results.insert(0, f"{global_title}\n{underline}")
        elif output_format == "html":
            global_title = "<h2><u>These packages have been mentioned on the Arch News page</u></h2>\n"
            results.insert(0, global_title)

    return results


def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Parse an RSS feed and search by package titles or descriptions.")
    parser.add_argument("-p", "--package", nargs="+", required=True, help="List of package names to search for in titles and descriptions.")
    parser.add_argument("--days", type=int, default=14, help="Number of days to look back for titles and descriptions.")
    parser.add_argument("--feed-url", default="https://archlinux.org/feeds/news", help="RSS feed URL to parse.")
    parser.add_argument("--html", action="store_true", help="Output in HTML format.")
    parser.add_argument("--text", action="store_true", help="Output in plain text format (default).")
    parser.add_argument("--debug", action="store_true", help="Enable debugging output for errors.")
    args = parser.parse_args()

    # Determine output format (default to text)
    output_format = "html" if args.html else "text"

    # Parse the feed
    try:
        results = parse_package_feed(args.feed_url, args.package, args.days, output_format, args.debug)
    except Exception as e:
        if args.debug:
            print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(3)

    # Print the results
    if results:
        print("\n".join(results))
    #else:
    #    print("No matching packages found.")


if __name__ == "__main__":
    main()
