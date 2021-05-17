# OSL_TechAssignment


## Architecture of This Project

Project is composed of 4 files, each of them has following responsibilities.

 - main.py : Command Line Interface of this application. Format is identical as the example given at the question sheet.
 - checkout.py : Interface which controls the Pricing Strategies. This interface is created inorder to match the format at the given question. Also, price of each product can be settled at the 'pricelist' variable of this interface class.
 - pricingstrategies.py : Pricing Strategy of the shop. Considering that the similar strategies could be applied in future, with the specific parameter given, same strategy can be applied in different product and numbers.
 - test.py : UnitTest for the core functions and testcases for whole application.
 
 
