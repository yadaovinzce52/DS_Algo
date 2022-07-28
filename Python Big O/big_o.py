nemo = ["nemo"]
everyone = ["dory", "bruce","marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

def find_nemo(array):   # uses array as the input
    for element in array:   # loops through input array
        if element.lower() == "nemo":   # if the element is "nemo"
            print("Found Nemo!")    # print statement


find_nemo(everyone)     # function call
