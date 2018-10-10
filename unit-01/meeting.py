attendees = ["Ken", "Alena", "Sam"]
attendees.append("Ashley")
attendees.exnted(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print(potential_attendees)

print("There are", len(attendees), "attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + cc_line)
