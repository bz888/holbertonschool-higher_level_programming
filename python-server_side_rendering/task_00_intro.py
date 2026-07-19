#!/usr/bin/env python3
"""Generate personalized event invitation files from a template."""

import logging


def generate_invitations(template, attendees):
    """Create one invitation text file for every attendee.

    Missing (or ``None``) attendee fields are rendered as ``N/A``.  Invalid
    inputs and empty inputs are reported without creating output files.
    """
    if not isinstance(template, str):
        logging.error("Invalid template type: expected a string.")
        return

    if not isinstance(attendees, list):
        logging.error("Invalid attendees type: expected a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid attendees type: expected a list of dictionaries.")
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            invitation = invitation.replace(
                "{" + placeholder + "}", "N/A" if value is None else str(value)
            )

        with open(f"output_{index}.txt", "w", encoding="utf-8") as output_file:
            output_file.write(invitation)
