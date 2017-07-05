### All of the codes run as the user 'root' in the server. I assume you will need to do the same if you are planning to run 
### on large scale of machines. Let's get started with description.
### aws-billing-tags is going to give you the output of all your instance names, instance ids, their current state (meaning
### running, stopped, terminated, etc.) and the billing tag.  
aws-billing-tags.py
### The code list-instIds-status.py will give you the instance IDs and their state (running, etc.) only. 
list-instIds-status.py
### The names_ids_status is supposed to give you the names of the instances, their ids and status (running, etc.)
names_ids_status.py
