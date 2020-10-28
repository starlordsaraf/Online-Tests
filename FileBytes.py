input_file = input()

out_file = open("bytes_"+input_file,"w")
in_file = open(input_file,"r")

lines = in_file.readlines()
ctr = 0
byte_sum = 0

for l in lines:
    b = int(l.split()[-1])
    if(b>5000):
        ctr+=1
        byte_sum+=b

out_file.write(str(ctr))
out_file.write("\n")
out_file.write(str(byte_sum))

out_file.close()
in_file.close()
    