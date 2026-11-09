Web_Development = ["Zarah", "Kevin", "Alex"]
Data_Science = ["Sophia", "Emily","David"]
UI_Design = ["Grace","Asha", "Ryan"]

all_participants = [Web_Development, Data_Science, UI_Design]
print(all_participants)

Web_Development.append("Tara")
print(Web_Development)

Data_Science.insert(1, "Airah")
print(Data_Science)

UI_Design.pop()
print(UI_Design)

new_list = Data_Science.copy()
Data_Science.clear()

print(Web_Development[:2])

newlist_len = [len(x)  for x in new_list]
print(newlist_len)

print("Asha" in Web_Development)
print("Asha" in new_list)
print("Asha" in UI_Design)

first_participant = (Web_Development[0], new_list[0], UI_Design[0])
print("First participants:", first_participant)
