#ranking
'''
d:damping factor
	the probability of visiting a website by cliking the link

condition assuming:
	Page A has 2 inlinks:Page B and Page C 
	There's N Page in the LAN we caculate


rank(A) = d * ( rank(B) / outlinks_len(B) + rank(C) / outlinks_len(C) ) + (1-d)/N

graph struture:
	{ 
		pageA_url : [pageA_outlink1,pageB_outlink2...],
		pageB_url : [...]
	}

'''
def compute_ranking(times,graph):
	d = 0.8
	results={}
	N = len(graph)
	for page in graph:
		results[page] = 1.0/N
	#print results
	for i in range(0,times):
		temprank = {}
		for page in graph:
			#rank = results[page]
			rank = (1-d)/N
			for node in graph:
				if page in graph[node]:
					rank += d * results[node]/(len(graph[node]))
			temprank[page] = rank
		results = temprank
	return  results


#testing
graph = {
	"a":["b","c"],
	"b":["a"],
	"c":["a","b","c"]
}
#print len(graph)
results = compute_ranking(2,graph)
sum=0
for i in results:
	sum += results[i]
print sum