# basic knowledge:
## 1. how to initialize a dictionary
## 2. how to set key/value
## 3. how to get key/value
    thisdict = {
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964
        }
 *Accessing the itemas* </br>
   
    TIme complexity: O(1)
    x = thisdict["model"]
    x= thisdict.get('model')
    x= thisdict.get(keyname, value) ----> A value to return if the specified key does not exist.
    
    
 *Get all values or all keys* </br>
 
        x = thisdict.values()
        x = car.keys()

    
  # the contraints give us the hint that it could be ascending order ---> binary search  
  *All the timestamps timestamp of set are strictly increasing.*  
  
  
    
