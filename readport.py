from readrides import read_as_dict
from datetime import datetime
from collections import Counter


def people_on_route(data: list[dict], route: str, date: datetime) -> int:
    """
    Take in a route number and date and return the number of people on that date
    """
    # Reformat the date into a string that the datadict understands
    date_str = date.strftime("%m/%d/%Y")
    num = sum([int(i["rides"]) for i in data if (i["date"], i["route"]) == (date_str, route)])

    return num


def delta_people_on_route(data: list[dict], date1: datetime, date2: datetime) -> Counter:
    """
    Count the number of rides per route within two specified dates and return as dict
    """
    delta_rides: Counter = Counter()
    date1_str = date1.strftime("%m/%d/%Y")
    date2_str = date2.strftime("%m/%d/%Y")

    for i in data:
        delta_rides[i["route"]] += i["rides"] if date1_str <= i["date"] <= date2_str else 0

    return delta_rides


def count_per_route(data: list[dict]) -> Counter:
    """
    Count number of rides taken per route and return as a dictionary of integers
    """
    count_dict: Counter = Counter()

    for line in data:
        count_dict[line["route"]] += line["rides"]

    return count_dict


if __name__ == "__main__":
    data = read_as_dict(0)  # Get the data

    q1 = "Question 1: How many bus routes exist in Chicago?"
    number_of_routes = len({s["route"] for s in data})
    print(f"{q1} Answer: {number_of_routes}")

    q2 = "Question 2: How many people rode the number {} bus on {}?"
    # What about any route on any date of your choosing?
    desired_date = datetime(2011, 2, 2)
    desired_route = "22"
    lit_q2 = q2.format(desired_route, desired_date.strftime("%B %d, %Y"))
    print(f"{lit_q2} Answer: {people_on_route(data, desired_route, desired_date)}")

    q3 = "Question 3: What is the total number of rides taken on each bus route?"
    sorted_dict = dict(sorted(count_per_route(data).items(), key=lambda key: key[0]))
    answer3 = "\n".join([f"{k}: {v}" for k, v in sorted_dict.items()])
    print(f"{q3} Answer:\n{answer3}")

    q4 = "Question 4: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?"
    # First year rides:
    start_date1 = datetime(2001, 1, 1)
    end_date1 = datetime(2001, 12, 31)
    first_year = delta_people_on_route(data, start_date1, end_date1)
    # Second year rides:
    start_date2 = datetime(2011, 1, 1)
    end_date2 = datetime(2011, 12, 31)
    second_year = delta_people_on_route(data, start_date2, end_date2)
    # Delta between the years:
    delta = second_year - first_year
    sorted_delta = delta.most_common(5)
    answer4 = "\n".join([f"{k}: {v}" for k, v in sorted_delta])
    print(f"{q4} Answer:\n{answer4}")
