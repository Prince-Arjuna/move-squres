#Imports the library which helps transfer data from APIne
import requests
def get_country_info(country_name, show_flag = False, show_coat = False, show_translations = False):
#Url
 response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
 #Checks if api request is succesful
 if response.status_code == 200:
#Fethching data
    country_data = response.json()[0]
 #This Api for some reason recognizes china as taiwan so i changed it so i shows china info 
 if country_name != 'china' and country_name != 'China' and country_name:
    #Gives the name of the country, continent(s), and subregion
    print(f"The name of the country is {country_name} and it is located in {country_data['continents']} in the subregion of {country_data['subregion']} ")
    #Make sure this countries play fifa
    if 'fifa' in country_data:
     print(f"The fifa code is {country_data['fifa']}") 
    else:
     print(f"This country does not particpate in FIFA")
    #Population of the country
    print(f"Population of {country_data ['population']} people")
    #Timezones
    print(f"{country_data['timezones']}")
    #Longitude and latitude
    print(f"The longitude and latitude {country_data['latlng']}")
    #Currencies
    print(f"Currencies in this country {country_data['currencies']}")
    #Area in km^2
    print(f"The area of this country is {country_data['area']} km^2")
    #Capital
    print(f"The capital of this country is {country_data['capital']}")
    #Gini i do not know that is
    print(f"The gini of this country is {country_data['gini']}")
    #Languages
    print(f"The languages spoken in this {country_data['languages']}")
    #Maps of the country
    print(f"Map links {country_data['maps']}")
    
    #Checking if country has borders
    if 'borders' in country_data:
     print(f"The borders of this country are {country_data['borders']}")
    else:
      print("")
   
    #Shows or hides flag link depending on input
    if 'flags' in country_data and country_data['flags'].get('png'):
     print(f"Here is a link to the flag {country_data['flags']['png']}")
    else:
      print("")
    #Shows or hides coat of arms link depending on input
    if show_coat and 'coatOfArms' in country_data and country_data['coatOfArms'].get('png'):
     print(f"Here is a link to the coat of arms {country_data['coatOfArms']['png']}")
    else:
      print('No coat of arms')
    #If user input for flag or coat of arms is not yes nothing in that section is printed
    if show_translations and 'translations' in country_data:
     print(f"Here is a long list of translations of this country {country_data['translations']}")

    else:
        print("")

#China function
 else:
    print("This country is china and it is located in Asia in the subregion of eastearn asia")
    print(f"The fifa code is CHN") 
    print(f"Population of 1,425,887,3375")
    print(f"The longitude and latitude [35.87,104.2]")

    

#I do not understand this IF statement i used AI to help me with this 
if __name__ == "__main__":
    #User input for country
    country_name = input("Enter country name:")
    #We use .strip() and .lower() to make sure if someone puts yes if there are capital letters or spaces 
    # it does not affect the output
    #User input for coat of arms            
    show_coat = input("Would you like the coat of arms to be displayed? ").strip().lower() == "yes"
    #User input for translations
    show_translations = input("Would you like to see a worrying long list of translations?") .strip().lower() == "yes"
    #Executes variables
    get_country_info(country_name, show_coat,show_translations, )









    
