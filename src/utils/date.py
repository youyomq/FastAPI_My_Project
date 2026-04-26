from datetime import date


def get_end_date(date_issue):
    end_date = date(year=date_issue.year + 10, month=date_issue.month, day=date_issue.day)

    return end_date