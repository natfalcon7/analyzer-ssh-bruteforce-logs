from loader import load_logs
from cleaner import cleaner_logs
from analyzer import get_failed_ips, get_attacked_users, get_success_by_country, get_suspicious_ips, get_failed_hours
from visualizer import show_failed_ips, show_attacked_users, show_success_by_country, show_suspicious_ips, show_failed_hours
from exporter import export_csv

if __name__== "__main__":
	records = [cleaned for line in load_logs() if (cleaned := cleaner_logs(line))]
	# Calls to the Analyzer
	failed_ips = get_failed_ips(records)
	attacked_users = get_attacked_users(records)
	success_by_country = get_success_by_country(records)
	suspicious_ips = get_suspicious_ips(records, threshold=5)
	failed_hours = get_failed_hours(records)
	# Calls to the Visualizer
	show_failed_ips(failed_ips, top = 10)
	show_attacked_users(attacked_users, top = 10)
	show_success_by_country(success_by_country, top = 10)
	show_suspicious_ips(suspicious_ips, top = 10)
	show_failed_hours(failed_hours, top = 10)
	# Calls to the Exporter
	export_csv(
		failed_ips,
		attacked_users,
		success_by_country,
		suspicious_ips,
		failed_hours,
		"report.csv")