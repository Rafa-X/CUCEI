## Use of the module PICKLE.
#### Demonstration of how different data structures can be serialized and de-serialized and it's use as a "checkpoint" for when the values of them changes and wants to be restored using methods from the pickle module.

1. - First I make the data structure for an object, a class called "Books"
   - Then there is a function which declares different data structs: float, list, dictionary and the object from the previous class  
![vars declaration](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/acfa84bc-5fa6-4298-a04d-a20b7a135a38)


2. - The next step can be done in two ways: create a pickle object which contains the data or create a variable that basically do the same, in this example it's done with a dictionary variable called "db"
![image](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/f7d4c470-edb9-4bb2-b75d-15ad2c59713f)


3. - Create the file for the data to be stored (for pickle is better to be a binary one)
   - Only last the saving, call the method: pickle.dump(data, file_name), and close the file with: dbfile.close()
![image](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/d3feb0b4-c014-43bc-90ef-97315da4c7d1)

At this point the variables values can be modified but the previous values will always be safe in the pickled file, to restore this values
only needs to call the method: pickle.load(file_name), and get the data depending on the structure used to store it, in this case a dictionary:

![image](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/d138d89f-3242-475e-9030-e5e7b9e47125)


## Runtime example:
-Code:

![image](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/0106bbde-7cfc-4da6-9acc-ac6f03831c7c)

-Output:

![image](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/assets/75345733/eee13956-91d9-4926-80f8-568398916828)



