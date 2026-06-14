# Python script generates complete URLs for all crossword puzzles for the year
# from the LA Times/Washington Post.
#
# The pattern follows:
# * Start at the beginning of the year with a specific value
# * For the following day: increment by 1
# * Except on the 10th, 20th, or 30th: increment by 22
# * Except on the 1st of the month: increment by 29698
#
# Output format for the URL: https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/YYYY/MM/DD/NUMBER/_light_unsolved.pdf


from datetime import date, timedelta

year = 2026
#value = -1376276680
value = -1376127725  #Fixed for 6/1

start_date = date(year, 6, 1)
end_date   = date(year, 12, 31)
current = start_date

while current <= end_date:
    # Print current line
    print(f"* {current:%m/%d}: [Blank](https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/{current:%Y/%m/%d}/{value}_light_unsolved.pdf) - [Solution](https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/{current:%Y/%m/%d}/{value}_light_solved.pdf)")

    # Move to next day
    next_day = current + timedelta(days=1)

    # Decide increment
    if next_day.day == 1:
        increment = 29698
    elif next_day.day in (10, 20, 30):
        increment = 22
    else:
        increment = 1

    value += increment
    current = next_day
# Python script generates complete URLs for all crossword puzzles for the year
# from the LA Times/Washington Post.
#
# The pattern follows:
# * Start at the beginning of the year with a specific value
# * For the following day: increment by 1
# * Except on the 10th, 20th, or 30th: increment by 22
# * Except on the 1st of the month: increment by 29698
#
# Output format for the URL: https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/YYYY/MM/DD/NUMBER/_light_unsolved.pdf


from datetime import date, timedelta

year = 2026
value = -1376276680

start_date = date(year, 1, 1)
end_date   = date(year, 12, 31)
current = start_date

while current <= end_date:
    # Print current line
    print(f"* {current:%m/%d}: [Blank](https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/{current:%Y/%m/%d}/{value}_light_unsolved.pdf) - [Solution](https://www.washingtonpost.com/games-static/games-crossword-PDF/daily/{current:%Y/%m/%d}/{value}_light_solved.pdf)")

    # Move to next day
    next_day = current + timedelta(days=1)

    # Decide increment
    if next_day.day == 1:
        increment = 29698
    elif next_day.day in (10, 20, 30):
        increment = 22
    else:
        increment = 1

    value += increment
    current = next_day
