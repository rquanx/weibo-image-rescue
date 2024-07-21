import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description="Weibo Image Rescue Tool")
    parser.add_argument("-u", action="store_true", help="Update CDN information")
    parser.add_argument(
        "-f", type=str, help="Force update CDN information and rescue image from URL"
    )
    parser.add_argument(
        "-q",
        type=str,
        default="l",
        help="Specify qualities to rescue, can be a single value or multiple comma-separated values, e.g., l,ml,m,o,t  (default: l)",
    )
    parser.add_argument("image_url", nargs="?", type=str, help="Image URL to rescue")
    return parser.parse_args(args)