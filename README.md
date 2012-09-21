LSerach
=======

Baby Serach Engine for academic purpose and fun
Ranking:
condition assuming:
	Page A has 2 inlinks:Page B and Page C 
	There's N Page in the LAN we caculate


rank(A) = d * ( rank(B) / outlinks_len(B) + rank(C) / outlinks_len(C) ) + (1-d)/N

graph struture:
	{ 
		pageA_url : [pageA_outlink1,pageB_outlink2...],
		pageB_url : [...]
	}