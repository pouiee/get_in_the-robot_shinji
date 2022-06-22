def list_of_dictionaries_to_dictionary_of_lists(pilot_tests):
    # this will be the final returned dictionary
    dictionary_of_results = {}

    # loop through the dictionaries in list provided
    for dictionary in pilot_tests:
        # loop through the keys and values in a dictionary
        for key, value in dictionary.items():
            # if the key value pair match up and the key is not already in the dictionary,
            # add key value pair to the dictionary
            if dictionary[key] == value and key not in dictionary_of_results.keys():
                dictionary_of_results[key] = [value]
            # if the pair exists and the value is not already in the key list, append to key value(s)
            elif dictionary[key] == value and value not in dictionary_of_results[key]:
                dictionary_of_results[key].append(value)

    # return the newly formed dictionary composed of {pilot : compatible mech(s)}
    return dictionary_of_results


# create 3 objects representing a set of tests
# each sync test is a dictionary, with its entries a pilot and the ability to sync with EVA unit robot
syncTest1 = {"Rei": "Eva-00", "Shinji": "Eva-01"}
# create second dictionary, add 2 key-value pairs
syncTest2 = {"Asuka": "Eva-02", "Shinji": "Eva-01"}
# create third dictionary object, add 3 key-value pairs
# we can also create it as a literal
syncTest3 = {
    "Shinji": "Eva-00",
    "Rei": "Eva-01",
    "Asuka": "Eva-02"
}
# create a list of the sync tests
pilotTests = [syncTest1, syncTest2, syncTest3]

for test in pilotTests:
    print("\n Sync Test:")
    for pilot, unit in test.items():
        print("{pilot} can sync with {unit}".format(pilot=pilot, unit=unit))

print("\n Results:")
results = list_of_dictionaries_to_dictionary_of_lists(pilotTests)
# print out pilot name and compatible mech unit(s)
for pilot in results.keys():
    print(f"{pilot} Syncs with: "+ str(set(results[pilot])))
