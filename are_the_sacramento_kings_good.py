import requests
from bs4 import BeautifulSoup

# url for Sacramento Kings basketball results
url = "http://bkref.com/pi/shareit/chhzP"

# uses a get request to retrieve the content of the url
response = requests.get(url)

# parses the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# finds the table containing the latest match results
table = soup.find("table", {"id": "games"})

if table is not None:
    # Extract the results of the last 5 matches
    rows = table.find("tbody").find_all("tr")[-6:]  # Get the latest 5 matches from the end of the table

    # Check if the Kings won or lost their last 5 matches
    result_summary = ""
    for row in rows:
        result = row.find("td", {"data-stat": "game_result"})
        if result is not None:
            result_text = result.text.strip()
            if "W" in result_text:
                result_summary += "Won, "
            elif "L" in result_text:
                result_summary += "Lost, "

    if result_summary:
        results = "Sacramento Kings' Recent Form: \n" + result_summary[:-2]  # removes unnecessary formatting
        print(results)
        wins = result_summary.count("Won")
        losses = result_summary.count("Lost")

        if wins > 2:
            print("\nThe Kings are good at the moment :)")
        else:
            print("\nThe Kings are bad right now :(")
    else:
        print("Results not found")
else:
    print("Table not found")
