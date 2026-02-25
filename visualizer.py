# show_failed_ips
def show_failed_ips(counting, top = 10):
	print(":\n== IPs with more failed attempts ==")
	
	if not counting:
		print("  No failed IPs found.")
		return

	sorted_ips = sorted(counting.items(), key=lambda x: x[1], reverse = True)

	for ip, fails in sorted_ips[:top]:
		print(f" {ip:<20} {fails} attempts")

# show_attacked_users

def show_attacked_users(counting, top = 10):
	print(":\n== Users with more failed attempts ==")
	
	if not counting:
		print("  No data found.")
		return

	sorted_users = sorted(counting.items(), key=lambda x: x[1], reverse = True)

	for user, fails in sorted_users[:top]:
		print(f" {user:<20} {fails} attempts")
# Success rate by country
def show_success_by_country(counting, top = 10):
	print(":\n== Success rate by country ==")
	
	if not counting:
		print("  No country data found.")
		return

	sorted_countries = sorted(counting.items(), key=lambda x: x[1]["rate"], reverse = True)

	for country, data in sorted_countries[:top]:
		print(f"  {country:<15} total: {data['total']:<6} success: {data['success']:<6} rate: {data['rate']}%")

# Suspicious ips

def show_suspicious_ips(suspicious_list, top = 10):
	print(":\n== Suspicious IPs (SUCCESS after many FAILs) ==")

	if not suspicious_list:
		print("  No suspicious IPs found.")
		return

	sorted_ips = sorted(suspicious_list, key=lambda x: x["fails"], reverse = True)

	for data in sorted_ips[:top]:

		print(f"  {data['ip']:<15} fails: {data['fails']:<6} success: {data['success']}")

# 
def show_failed_hours(counting, top = 10):
	print(":\n== Failed attempts by hour ==")

	if not counting:
		print(" No data found.")
		return

	sorted_hours = sorted(counting.items(), key= lambda x: x[1], reverse=True) [:top]

	max_attempts = sorted_hours[0][1]
	scale = 20 / max_attempts

	for hour, attempts in sorted_hours:
		bar = "█" * int(attempts * scale) 
		print(f" {hour:02d}:00, {attempts:>6} attempts {bar}")

