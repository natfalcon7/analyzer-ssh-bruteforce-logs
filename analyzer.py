


# IPs with failed attempts
def get_failed_ips(records):
	counting = {}
	
	for record in records:
		if record["result"] == "FAIL":
			key = record["ip"]
			
			counting[key] = counting.get(key, 0) + 1
			
	return counting			

# Users with failed attempts
def get_attacked_users(records):
	counting = {}
	
	for record in records:
		if record["result"] == "FAIL":
			key = record["user"]
			
			counting[key] = counting.get(key, 0) + 1
			
	return counting

# Success rate by country 

def get_success_by_country(records):
	counting = {}
	
	for record in records:
		key = record["country"]

		if key not in counting:
			counting[key] = {"total": 0, "success": 0,}
		counting[key]["total"] += 1
		
		if record["result"] == "SUCCESS":
			counting[key]["success"] += 1


	for key in counting:
		total = counting[key]["total"]
		success = counting[key]["success"]
		counting[key]["rate"] = round((success / total) * 100, 2)

	return counting	


# Success after a lot of fails
def get_suspicious_ips(records, threshold):
	counting = {}
	list_suspicious = []
		
	for record in records:
		key = record["ip"]

		if key not in counting:
			counting[key] = {"fail": 0, "success": 0,}
			
		if record["result"] == "FAIL":
			counting[key]["fail"] += 1
		elif record["result"] == "SUCCESS":
			counting[key]["success"] +=1

	for key in counting:
		fails = counting[key]["fail"]
		success = counting[key]["success"]

		if fails > threshold and success >= 1:
			list_suspicious.append({"ip": key, "fails": fails, "success": success})

	return list_suspicious		

# Attacks by time
def get_failed_hours(records):
	counting = {}
	
	for record in records:
		if record["result"] == "FAIL":
			key = record["timestamp"].hour
			
			counting[key] = counting.get(key, 0) + 1
			
	return counting