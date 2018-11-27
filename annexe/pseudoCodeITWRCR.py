#Add to code
def cr-evaluation:
	after interaction -> retrieve-ratings
	delete-worst-ratings (H) #Only save H in DB ??
	Rc = get-rates CR b  #{ ask b give-c-ratings }

#TODO :  Gérer l'estimation de la distance avec evaluation WR et CR