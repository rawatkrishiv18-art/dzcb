import numpy as np 
data_type = ([('name','S15'),('age','int'),('height','float')])
student_details = ([('sam', 17, 6.1), ('ham', 18, 4.9), ('john', 19, 5.6),('bacon',40,6.9)])
students = np.array(student_details,dtype=data_type)
print("orignal array:")
print(students)
a = np.reshape(students,(2,2))
print("sorted by height")
print(np.sort(a,order='height'))