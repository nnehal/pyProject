def intToRoman(number):
    roman = ""

    storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

    for i in range(len(storeIntRoman)):
        while number >= storeIntRoman[i][0]:
            roman += storeIntRoman[i][1]
            number -= storeIntRoman[i][0]
    return roman

print(intToRoman(10))