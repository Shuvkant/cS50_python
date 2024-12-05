"""
2.  Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $12 for adults (18 and
over), $8 for children. Everyone gets a $2 discount on Wednesday.
    """
age=int(input("Enter your age: "))
day=str((input("Enter day of the week: ")))
ticketfare=0
discout=0
if(age>=18):
    ticketfare=12
    person="adult"
else:
    ticketfare=8
    person="child"

if(day=='sun'):
    discout=2
    ticketfare=ticketfare-2

print(f"Ticketfare for {person}: {ticketfare}")




