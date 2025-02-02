from models.owner import Owner
import repositories.owner_repository as owner_repository

from models.pet import Pet
import repositories.pet_repository as pet_repository

from models.treatment import Treatment
import repositories.treatment_repository as treatment_repository

from models.vet import Vet
import repositories.vet_repository as vet_repository

from models.nurse import Nurse
import repositories.nurse_repository as nurse_repository

from models.price import Price
import repositories.price_repository as price_repository

from models.booking import Booking
import repositories.booking_repository as booking_repository


# treatment_repository.delete_all()
# pet_repository.delete_all()
# owner_repository.delete_all()
# vet_repository.delete_all()
# nurse_repository.delete_all()


vet_1 = Vet("Dr DoAlot", "Reptiles", "doalotnotalitte@mail.com")
vet_repository.save(vet_1)
vet_2 = Vet("Dr Pawsitive", "Dogs", "bingo@mail.com")
vet_repository.save(vet_2)
vet_3 = Vet("Dr Meowgaret", "Cats", "purr@mail.com")
vet_repository.save(vet_3)
vet_4 = Vet("Dr Trotter", "Farm animals", "oink@mail.com")
vet_repository.save(vet_4)
vet_5 = Vet("Dr Bunderful", "Small pets", "bunnyfoufou@mail.com")
vet_repository.save(vet_5)
vet_6 = Vet("Dr Dory", "Aquatic", "bubbles@mail.com")
vet_repository.save(vet_6)

# vet_repository.save(vet_6)
# vet_repository.select_all()
# vet_repository.select(1)
# vet_repository.delete_all()
# vet_repository.delete(10)

owner_1 = Owner("Scarlet", "Skittles", "tastetherainbow@mail.com", "07711111111")
owner_repository.save(owner_1)
owner_2 = Owner("Janet", "Jelly", "wobbly@mail.com", "07711221122")
owner_repository.save(owner_2)
owner_3 = Owner("Kelly", "Kinder", "eggs@mail.com", "07711331133")
owner_repository.save(owner_3)
owner_4 = Owner("Mandy", "Marshmallow", "squidgy@mail.com", "07711441144")
owner_repository.save(owner_4)
owner_5 = Owner("Andy", "Allsorts", "sweeties@mail.com", "07711551155")
owner_repository.save(owner_5)
owner_6 = Owner("Buzz", "BonBon", "strawberry@mail.com", "07711661166")
owner_repository.save(owner_6)
owner_7 = Owner("Mike", "Mars", "yum@mail.com", "07711771177")
owner_repository.save(owner_7)
owner_8 = Owner("Carl", "Cookie", "chocchips@mail.com", "07711881188")
owner_repository.save(owner_8)

# owner_repository.select_all()
# owner_repository.select(16)
# owner_repository.delete_all()
# owner_repository.delete(20)

nurse_1 = Nurse("a name1", "Mondays/Wednesdays", True, "name1@mail.com")
nurse_repository.save(nurse_1)
nurse_2 = Nurse("a name2", "Mondays/Tuesdays/Fridays", False, "name2@mail.com")
nurse_repository.save(nurse_2)
nurse_3 = Nurse("a name3", "Tuesdays only", False, "name3@mail.com")
nurse_repository.save(nurse_3)
nurse_4 = Nurse("a name4", "Mondays/Thursdays", True, "name4@mail.com")
nurse_repository.save(nurse_4)
nurse_5 = Nurse("a name5", "Mon-Fri", False, "name5@mail.com")
nurse_repository.save(nurse_5)

# nurse_repository.select_all()
# nurse_repository.select(16)
# nurse_repository.delete_all()
# nurse_repository.delete(20)

price_1 = Price("X-ray", "£70", "30 minutes", False, 2)
price_repository.save(price_1)
price_2 = Price("Ultra Sound Scan", "£120", "45 minutes", False, 1)
price_repository.save(price_2)
price_3 = Price("CT Scan", "£150", "60 minutes", True, 3)
price_repository.save(price_3)
price_4 = Price("MRI Scan", "£180", "60 minutes", True, 3)
price_repository.save(price_4)
price_5 = Price("Vet Appointment", "£110", "60 minutes", True, 1)
price_repository.save(price_5)
price_6 = Price("Specialist Vet Appointment", "£150", "90 minutes", True, 1)
price_repository.save(price_6)
price_7 = Price("Nurse Practioner Appointment", "£70", "45 minutes", False, 1)
price_repository.save(price_7)
price_8 = Price("Vet House Call", "£130", "90 minutes", True, 0)
price_repository.save(price_8)



pet_1 = Pet("Snuffles", '2021-12-28', "Hamster", owner_1, vet_1)
pet_repository.save(pet_1)
pet_2 = Pet("Fergus", '2021-12-28', "Rabbit", owner_2, vet_2)
pet_repository.save(pet_2)
pet_3 = Pet("Poppins", '2021-12-28', "Cat", owner_3, vet_4)
pet_repository.save(pet_3)
pet_4 = Pet("Harry", '2021-12-28', "Dog", owner_4, vet_5)
pet_repository.save(pet_4)
pet_5 = Pet("Archie", '2021-12-28', "Dog", owner_5, vet_6)
pet_repository.save(pet_5)
pet_6 = Pet("Jake", '2021-12-28', "Guinea Pig", owner_6, vet_5)
pet_repository.save(pet_6)
pet_7 = Pet("Sally", '2021-12-28', "Snake", owner_7, vet_3)
pet_repository.save(pet_7)
pet_8 = Pet("Roxy", '2021-12-28', "Bearded Dragon", owner_8, vet_1)
pet_repository.save(pet_8)
pet_9 = Pet("Rupert", '2021-12-28', "Rat", owner_3, vet_4)
pet_repository.save(pet_9)
pet_10 = Pet("Coco", '2021-12-28', "Dog", owner_7, vet_3)
pet_repository.save(pet_10)

# pet_repository.select_all()
# pet_repository.select(7)
# pet_repository.delete(19)

treatment_1 = Treatment("26th May 2021", "MRI Scan", pet_2, vet_1)
treatment_repository.save(treatment_1)
treatment_2 = Treatment("3rd Aug 2021", "CT Scan", pet_3, vet_6)
treatment_repository.save(treatment_2)
treatment_3 = Treatment("19th Jan 2021", "Ultra Sound Scan", pet_4, vet_2)
treatment_repository.save(treatment_3)
treatment_4 = Treatment("17th Nov 2021", "MRI Scan", pet_7, vet_3)
treatment_repository.save(treatment_4)
treatment_5 = Treatment("14th Feb 2022", "CT Scan", pet_8, vet_5)
treatment_repository.save(treatment_5)



# treatment_repository.select_all()
# treatment_repository.select(10)
# treatment_repository.delete(10)


booking_1 = Booking('2022-04-23', "12pm", pet_8, treatment_1, vet_1)
booking_repository.save(booking_1)
booking_2 = Booking('2022-04-23', "9.15am", pet_4, treatment_2, vet_1)
booking_repository.save(booking_2)
booking_3 = Booking('2022-04-23', "11.30am", pet_8, treatment_1, vet_2)
booking_repository.save(booking_3)
booking_4 = Booking('2022-04-23', "3pm", pet_2, treatment_3, vet_3)
booking_repository.save(booking_4)
booking_5 = Booking('2022-04-23', "1pm", pet_3, treatment_1, vet_4)
booking_repository.save(booking_5)

