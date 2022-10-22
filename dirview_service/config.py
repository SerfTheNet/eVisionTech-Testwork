# Since the task does not specify the need to work with internal or external file system paths
# both approaches has been realised. 
# Outer filesystem was mounted to /outerspace, so, you can access it modifying the path below.

# Path for accessing inner container root directory 
path = '/'
# Path for accessing inner container /opt directory 
# Path for accessing outer/OS root directory 
#path = '/outerspace/home/sergey'
# Path for accessing outer/OS user home directory
#path = '/outerspace/home/{username}'