#read number of test cases
n = int(input())

for i in range(n):
    #for each test case
    #get all of sounds detected
    sounds = input().split(" ")
    #read next line
    line = input()
    while(line!="what does the fox say?"):
        #get sound on this line (other animal sound)
        oa_sound = line.split(" ")[-1]
        #remove this sound from our sounds
        sounds = [sound for sound in sounds if sound!=oa_sound]
        #read next line
        line = input()
    #print result
    print(" ".join(sounds))
        