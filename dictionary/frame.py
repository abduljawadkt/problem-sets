def file_to_dict(fname): 
 f = open(fname, 'r') 
 D = dict() 
 # Here we need to store the header in a list 
 header = f.readline().strip().split(',') 
 # Add header names as keys in the dictionary 
 for col in header: 
 D[col] = [ ] 
 # Iterate through each line in the file 
 for line in f: 
 cols = line.strip().split(',') 
 for i in range(len(cols)): 
 # Get the column name 
 col_name = header[i] 
 # Make sure that the value is integer for all marks 
 val = int(cols[i]) if col_name != 'Name'elsecols[i] 
 D[col_name].append(val) 
 f.close() 
 return 