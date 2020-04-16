import json
import random, string

def input(botOutput, jsonPath):
    print(botOutput)
    print("Initalizing...")
    with open(jsonPath) as json_file:
        profiles = json.load(json_file)
    
    convertedProfiles = []
    print("Starting Conversion...")
    for p in profiles:
        mek = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(9))
        profileName = p["name"]

        deliveryFirstName = p["delivery"]["firstName"]
        deliveryLastName = p["delivery"]["lastName"]
        deliveryAddress = p["delivery"]["address1"]
        deliveryAddress2 = p["delivery"]["address2"]
        deliveryZip = p["delivery"]["zip"]
        deliveryCity = p["delivery"]["city"]
        deliveryCountry = p["delivery"]["country"]
        deliveryState = p["delivery"]["state"]
        deliveryPhone = p["phone"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")
        deliveryEmail = p["email"]

        billingFirstName = p["delivery"]["firstName"]
        billingLastName = p["delivery"]["lastName"]
        billingAddress = p["delivery"]["address1"]
        billingAddress2 = p["delivery"]["address2"]
        billingZip = p["delivery"]["zip"]
        billingCity = p["delivery"]["city"]
        billingCountry = p["delivery"]["country"]
        billingState = p["delivery"]["state"]
        billingPhone = p["phone"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")
        billingEmail = p["email"]
        cardType = None
        cardNumber = p["card"]["number"]
        cardMonth = p["card"]["expiryMonth"]
        cardYear = p["card"]["expiryYear"]
        cardCVV = p["card"]["cvv"]
        if "mekpreme" in str(botOutput):
            convertedProfiles.append(botOutput.output(mek, profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone))
        else:
            convertedProfiles.append(botOutput.output(profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone))

        print(f"Converted {profileName}.")
    fileName = "converted/wrath_{}.json".format(str(random.randint(1,9999)))
    with open(fileName, 'w') as f:
        json.dump(convertedProfiles, f, indent=2)
    print(f"Finished. Sent to {fileName}.")


def output(profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone):
    if deliveryCountry != "United States":
        deliveryCountry = "United States"
    formatted = ({
    "name": profileName,
    "email": deliveryEmail,
    "phone": deliveryPhone,
    "sizes": [],
    "modes": [],
    "taskAmount": 1,
    "singleCheckout": False,
    "billingDifferent": False,
    "favorite": False,
    "card": {
    "number": cardNumber,
    "expiryMonth": cardMonth,
    "expiryYear": cardYear,
    "cvv": cardCVV
    },
    "paypal": {
    "email": "",
    "password": ""
    },
    "delivery": {
    "firstName": deliveryFirstName,
    "lastName": deliveryLastName,
    "address1": deliveryAddress,
    "address2": deliveryAddress2,
    "zip": deliveryZip,
    "city": deliveryCity,
    "country": deliveryCountry,
    "state": deliveryState
    },
    "billing": {
    "firstName": billingFirstName,
    "lastName": billingLastName,
    "address1": billingAddress,
    "address2": billingAddress2,
    "zip": billingZip,
    "city": billingCity,
    "country": billingCountry,
    "state": billingState
        }
    })
    return formatted