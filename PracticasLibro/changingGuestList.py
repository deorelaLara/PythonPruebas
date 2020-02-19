"""3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send
        out a new set of invitations. You’ll have to think of someone else to invite.
             • Start with your program from Exercise 3-4. Add a print statement at
               the end of your program stating the name of the guest who can’t make it.
             • Modify your list, replacing the name of the guest who can’t make it with
               the name of the new person you are inviting.
             • Print a second set of invitation messages, one for each person who is still in your list."""

guests = ['Mario', 'Omar', 'Melissa', 'Rebeca']

print("-Hello dear " + guests[-2] + " i hope u' can join me at my birthday dinner." )
print("-Hi!!! " + guests[0] + " I wait for u' at my birthday dinner.")
print("-Hey "+ guests[-1] + " !!! Remember today's my birthday dinner")
print("-Sup " + guests[1] + "I hope you can joinme at my dinner\n")

print("--------------" + guests[0] + " can't make it ------------------\n")
guests[0] = 'Haru'

print("-Hello dear " + guests[-2] + " i hope u' can join me at my birthday dinner." )
print("-Hi!!! " + guests[0] + " I wait for u' at my birthday dinner.")
print("-Hey "+ guests[-1] + " !!! Remember today's my birthday dinner")
print("-Sup " + guests[1] + "I hope you can joinme at my dinner")