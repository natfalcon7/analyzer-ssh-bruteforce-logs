from datetime import datetime

def cleaner(line):
	fields = line.strip().split(",")
	if len(fields) != 5:
		return None

	timestamp_str, ip, user, result, country = fields
	if result not in ["FAIL", "SUCCESS"]:
		return None

	try:
		timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
	except ValueError:
		return None

	return {
	"timestamp": timestamp,
	"ip": ip,
	"user": user,
	"result": result,
	"country": country

	}	
	