from money_tracker_menu import *

def main():
	aggregated_object = Aggregated_object()
	m = MoneyTracker(aggregated_object)
	option = sys.stdin.readline()
	obj = MoneyTrackerMenu(option)
	print(obj.solution(option))
