from p3.models import TicketConference
from django.conf import settings
from django.db.models import Q
from conference.models import Ticket
from conference.fares import FARE_CODE_REGEXES, FARE_CODE_VARIANTS
from p3.utils import assign_ticket_to_user

# TODO: Move this somewhere else. Settings maybe(?)
DEFAULT_SHIRT_SIZE = "l"
DEFAULT_DIET = "omnivorous"


def reset_ticket_settings(ticket):
    tc = ticket.p3_conference
    tc.shirt_size = DEFAULT_SHIRT_SIZE
    tc.diet = DEFAULT_DIET
    tc.tagline = ""
    tc.days = ""
    tc.save()
    return tc


def count_number_of_sold_training_tickets_including_combined_tickets(conference_code):
    qs = Ticket.objects.filter(
        fare__conference=conference_code,
        frozen=False,
        orderitem__order___complete=True,
    ).filter(
        Q(
            fare__code__regex=FARE_CODE_REGEXES["variants"][
                FARE_CODE_VARIANTS.TRAINING
            ]
        )
        | Q(
            fare__code__regex=FARE_CODE_REGEXES["variants"][
                FARE_CODE_VARIANTS.COMBINED
            ]
        )
    )
    return qs.count()
