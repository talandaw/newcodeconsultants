filename = pickAFile()
source = makeSound(filename) 

rate = getSamplingRate(source)
print rate 

value = getSampleValue(source)
print value