"""
===================   TASK 5  ====================
* Create class Vehicle which represents any 
* vehicle and carries general info about the 
* vehicle like: company that built that vehicle, 
* model of the vehicle, year of production, 
* registration number, engine power and color.
* Create method cost_of_registration() that will 
* return how much will registration cost for that 
* instance of vehicle.
*
* Use this formula:

     - Production year fees: 100 EUR  if production year < 1990
                             200 EUR  if production year < 2000
                             300 EUR  if production year < 2010 
                             400 EUR  if production year < 2020
     - On production year fee add engine fee:   (engine power in kw * 2 EUR)
*
* In your main function create single instance of the
* Vehicle class and demonstrate the use of
* cost_of_registration method.
===================================================
"""

# Write your class here
class Vehicle:
    def __init__(self, company, model, year_of_production, registration_number, engine_power, engine_color):
        self.company = company
        self.model = model
        self.year_of_production = year_of_production
        self.registration_number = registration_number
        self.engine_power = engine_power
        self.engine_color = engine_color

    def cost_of_registration(self):

        if int(self.year_of_production) < 1990:
            production_year_fee = 100
        elif int(self.year_of_production) < 2000:
            production_year_fee = 200
        elif int(self.year_of_production) < 2010:
            production_year_fee = 300
        else:
            production_year_fee = 400

        fee1 = production_year_fee + int(self.engine_power) * 2
        print(fee1)







def main():
    # Test your function here
    info = Vehicle("Audi", "A4", 2011, "AB345", 77, "red")
    info.cost_of_registration()
    pass

if __name__ == "__main__":
    main()
