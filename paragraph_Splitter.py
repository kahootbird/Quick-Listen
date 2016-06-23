with open ("paragraphs.txt", "r") as myfile: 
 string_data=myfile.read().splitlines();

a = string_data[2::4];
b = string_data[0::4];

L = open("left.txt", 'w');
R = open("right.txt", 'w');
for i in a:
	L.write(i)
	L.write("\n")
	

L.close();

for i in b:
	R.write(i)
	R.write("\n")

R.close();

