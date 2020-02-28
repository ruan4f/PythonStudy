def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            lineBefore = arr[j]
            lineAfter = arr[j+1]

            clientNumberBefore = lineBefore[6:14]
            clientNumberAfter = lineAfter[6:14]

            if clientNumberBefore > clientNumberAfter :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
  file = open(r"C:\Users\ruanf\Desktop\FilesTest\AlinhaFat_202001Ate20200204_1351.txt","r+")
  lines = file.readlines()  
  file.close() 

  bubbleSort(lines)

  file2 = open("myfile.txt","w")   

  for line in lines:
    file2.write(line + "\n") 

  file2.close()

if __name__== "__main__":
  main()