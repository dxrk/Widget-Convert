import json
import random, string

def input(botOutput, jsonPath):
    print("Initalizing...")
    with open(jsonPath) as json_file:
        profiles = json.load(json_file)
    
    convertedProfiles = []
    print("Starting Conversion...")
    for p in profiles:
        mek = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(9))
        profileName = p["name"]

        deliveryFirstName = p["shippingAddress"]["name"].split()[0]
        deliveryLastName = p["shippingAddress"]["name"].split()[1]
        deliveryAddress = p["shippingAddress"]["line1"]
        deliveryAddress2 = p["shippingAddress"]["line2"]
        deliveryZip = p["shippingAddress"]["postCode"]
        deliveryCity = p["shippingAddress"]["city"]
        deliveryCountry = p["shippingAddress"]["country"]
        deliveryState = p["shippingAddress"]["state"]
        deliveryPhone = p["shippingAddress"]["phone"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")
        deliveryEmail = p["shippingAddress"]["email"]

        billingFirstName = p["billingAddress"]["name"].split()[0]
        billingLastName = p["billingAddress"]["name"].split()[1]
        billingAddress = p["billingAddress"]["line1"]
        billingAddress2 = p["billingAddress"]["line2"]
        billingZip = p["billingAddress"]["postCode"]
        billingCity = p["billingAddress"]["city"]
        billingCountry = p["billingAddress"]["country"]
        billingState = p["billingAddress"]["state"]
        billingPhone = p["billingAddress"]["phone"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")
        billingEmail = p["billingAddress"]["email"]
        cardType = p["paymentDetails"]["cardType"]
        cardNumber = p["paymentDetails"]["cardNumber"]
        cardMonth = p["paymentDetails"]["cardExpMonth"]
        cardYear = p["paymentDetails"]["cardExpYear"]
        cardCVV = p["paymentDetails"]["cardCvv"]

        if str(botOutput).includes("mekpreme"):
            convertedProfiles[mek] = {(botOutput.output(mek, profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone))}
        else:
            convertedProfiles.append(botOutput.output(profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone))
        
        print(f"Converted {profileName}.")
    fileName = "converted/wrath_{}.json".format(str(random.randint(1,9999)))
    with open(fileName, 'w') as f:
        json.dump(convertedProfiles, f, indent=2)
    print(f"Finished. Sent to {fileName}.")