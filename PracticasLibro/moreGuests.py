""" 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
         Think of three more guests to invite to dinner.
            • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to
              the end of your program informing people that you found a bigger dinner table.
            • Use insert() to add one new guest to the beginning of your list.
            • Use insert() to add one new guest to the middle of your list.
            • Use append() to add one new guest to the end of your list.
            • Print a new set of invitation messages, one for each person in your list."""

guests = ['Haru', 'Omar', 'Melissa', 'Rebeca']

print("Hi everybody i found a bigger dinner table!!! \n")

#Add to the bigining
guests.insert(0, 'Genesis')
#print(guests)

#Add to the middle
guests.insert(3, 'Frida')
#print(guests)

#Ue append to add one new guest
guests.append('Ana')
#print(guests)

print("-Hello dear " + guests[-2] + " i hope u' can join me at my birthday dinner." )
print("-Hi!!! " + guests[0] + " I wait for u' at my birthday dinner.")
print("-Hey "+ guests[-1] + " !!! Remember today's my birthday dinner")
print("-Sup " + guests[1] + " I hope you can joinme at my dinner")
print("-Hi!!! " + guests[2] + " I wait for u' at my birthday dinner.")
print("-Hey "+ guests[3] + " !!! Remember today's my birthday dinner")
print("-Hey "+ guests[4] + " !!! Remember today's my birthday dinner")
