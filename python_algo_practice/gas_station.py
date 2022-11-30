


def findFirstGasStation(cost,fill):
	if len(fill) != len(cost):
		return -1

	previous_mileage = 0
	current_mileage = 0
	starting_station = 0;

	for i in range(len(cost)):
	
		if current_mileage < 0:
			previous_mileage += current_mileage
			current_mileage = 0
			starting_station = i
	
		current_mileage += ( fill[i] - cost[i] )
		
	if (current_mileage - previous_mileage) >= 0:
		return starting_station
	else:
		return -1




def main():
	# cost = [1,2,3,4,5,6,7,8]
	# fill = [8,7,6,5,4,3,2,1]
	cost = [2,1,3,4,5]
	fill = [1,2,3,4,5]

	print(findFirstGasStation(cost,fill))



main()
	
