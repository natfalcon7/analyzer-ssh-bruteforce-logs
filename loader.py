LOG_PATH = "./ssh_logs.csv"


errors =[]
# Read the log file line by line using a generate to save memory.

def load_logs(path=LOG_PATH):

	try:
		with open(path,"r") as file:

			next(file)
			for line in file:
				yield line.strip()

	except FileNotFoundError:
		errors.append(f"File not found: {path}")
    except PermissionError:
    	errors.append(f"No permission to read: {path}")


