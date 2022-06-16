import os
path = "C:\\Users\\syamk\\Desktop\\nlp project\\tril.cpp"
  
  
# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR)
s = """#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
"""
# Convert the string to bytes
line = str.encode(s)
  
# Write the bytestring to the file
# associated with the file
# descriptor fd and get the number of
# Bytes actually written
numBytes = os.write(fd, line)
  
print("Number of bytes written:", numBytes)
  
# close the file descriptor
os.close(fd)