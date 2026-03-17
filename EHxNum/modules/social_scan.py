def social_links(number):

    links = {}

    links["Google"] = f"https://www.google.com/search?q=\"{number}\""
    links["Facebook"] = f"https://www.facebook.com/search/top?q={number}"
    links["Twitter"] = f"https://twitter.com/search?q={number}"
    links["LinkedIn"] = f"https://www.linkedin.com/search/results/all/?keywords={number}"

    return links
