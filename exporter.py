

def export_csv(
	failed_ips,
	attacked_users,
	success_by_country,
	suspicious_ips,
	failed_hours,
	filename):

	try:
		with open(filename, "w") as f:
			f.write("section,key,value\n")

			# Failed IPs
			
			for ip, fails in failed_ips.items():
				f.write(f"failed_ips, {ip}, {fails}\n")


			# Attacked Users
			
			
			for user, fails in attacked_users.items():
				f.write(f"attacked_users, {user}, {fails}\n")


			# Success by Country -flattened-
			
			
			for country, data in success_by_country.items():
				f.write(f"success_by_country,{country},{data['total']}|{data['success']}|{data['rate']}\n")


			# Suspicious IPs
			
			
			for item in suspicious_ips:
				f.write(f"suspicious_ips,{item['ip']},{item['fails']}|{item['success']}\n")


			# Failed Hours
			
			
			for hour, attempts in failed_hours.items():
				f.write(f"failed_hours,{hour},{attempts}\n")


	except Exception as e:
		print(f" Export error: {e}")

