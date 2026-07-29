"""
IT Help Desk Ticket Analyzer

Author:
Rebeka Nyambati

Description:
Analyzes IT support tickets to identify trends,
average resolution times, and common issues.
"""

import csv


def load_tickets(filename):
    tickets = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tickets.append(row)

    return tickets


def analyze_tickets(tickets):

    total_tickets = len(tickets)

    categories = {}
    total_resolution_time = 0

    for ticket in tickets:

        category = ticket["Category"]

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

        total_resolution_time += float(
            ticket["Resolution_Time_Hours"]
        )

    average_time = total_resolution_time / total_tickets

    most_common_issue = max(
        categories,
        key=categories.get
    )

    return total_tickets, average_time, most_common_issue


def generate_report(total, average, common_issue):

    report = f"""
IT Help Desk Support Report
===========================

Total Tickets Analyzed:
{total}

Average Resolution Time:
{average:.2f} hours

Most Common Issue:
{common_issue}

Recommended Action:
Create documentation and training resources
to reduce repeated support requests.

"""

    return report


tickets = load_tickets("tickets.csv")

total, average, common = analyze_tickets(tickets)

report = generate_report(total, average, common)

print(report)
