#import other bot files
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
        profileName = profiles[p]["profile_name"]

        deliveryFirstName = profiles[p]["billing_name"].split()[0]
        deliveryLastName = profiles[p]["billing_name"].split()[1]
        deliveryAddress = profiles[p]["order_address"]
        deliveryAddress2 = profiles[p]["order_address_2"]
        deliveryZip = profiles[p]["order_billing_zip"]
        deliveryCity = profiles[p]["order_billing_city"]
        deliveryCountry = profiles[p]["area"]
        deliveryState = profiles[p]["order_billing_state"]
        deliveryEmail = profiles[p]["order_email"]
        deliveryPhone = profiles[p]["order_tel"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")

        billingFirstName = profiles[p]["billing_name"].split()[0]
        billingLastName = profiles[p]["billing_name"].split()[1]
        billingAddress = profiles[p]["order_address"]
        billingAddress2 = profiles[p]["order_address_2"]
        billingZip = profiles[p]["order_billing_zip"]
        billingCity = profiles[p]["order_billing_city"]
        billingCountry = profiles[p]["area"]
        billingState = profiles[p]["order_billing_state"]
        billingEmail = profiles[p]["order_email"]
        billingPhone = profiles[p]["order_tel"].replace("(", "").replace(")", "").replace(",", "").replace("-", "").replace(" ", "")

        if profiles[p]["order_billing_country"] == "USA":
            billingCountry = "United States"
        else:
            billingCountry = profiles[p]["order_billing_country"]
        cardType = profiles[p]["card_type"]
        cardNumber = profiles[p]["cnb"]
        cardMonth = profiles[p]["month"]
        cardYear = profiles[p]["year"]
        cardCVV = profiles[p]["vval"]

        convertedProfiles.append(botOutput.output(profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone))
        print(f"Converted {profileName}.")
    fileName = "converted/wekpreme_{}.json".format(str(random.randint(1,9999)))
    with open(fileName, 'w') as f:
        json.dump(convertedProfiles, f, indent=2)
    print(f"Finished. Sent to {fileName}.")

def output(mek, profileName, cardType, cardNumber, cardMonth, cardYear, cardCVV, deliveryFirstName, deliveryLastName, deliveryAddress, deliveryAddress2, deliveryZip, deliveryCity, deliveryCountry, deliveryState, deliveryEmail, deliveryPhone, billingFirstName, billingLastName, billingAddress, billingAddress2, billingZip, billingCity, billingCountry, billingState, billingEmail, billingPhone):
    if billingCountry != "USA":
        billingCountry = "USA"
    formatted = ({
       "id": mek,
       "profile_name":profileName,
       "billing_name":billingFirstName + " " + billingLastName,
       "order_email":billingEmail,
       "order_address":billingAddress,
       "order_address_2":billingAddress2,
       "order_tel":billingPhone,
       "order_billing_zip":billingZip,
       "order_billing_city":billingCity,
       "area":billingCountry,
       "order_billing_state":billingState,
       "order_billing_country":billingCountry,
       "card_type":"master",
       "cnb":cardNumber,
       "month":cardMonth,
       "year":cardYear,
       "vval":cardCVV
    })
    return formatted