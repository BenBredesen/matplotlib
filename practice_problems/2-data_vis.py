import matplotlib.pyplot as plt
import numpy as np

data = '''CT	82	509	510
NJ	81	499	513
MA	79	511	515
NY	77	495	505
NH	72	520	516
RI	71	501	499
PA	71	500	499
VT	69	511	506
ME	69	506	500
VA	68	510	501
DE	67	501	499
MD	65	508	510
NC	65	493	499
GA	63	491	489
IN	60	499	501
SC	57	486	488
DC	56	482	474
OR	55	526	526
FL	54	498	499
WA	53	527	527
TX	53	493	499
HI	52	485	515
AK	51	514	510
CA	51	498	517
AZ	34	523	525
NV	33	509	515
CO	31	539	542
OH	26	534	439
MT	23	539	539
WV	18	527	512
ID	17	543	542
TN	13	562	553
NM	13	551	542
IL	12	576	589
KY	12	550	550
WY	11	547	545
MI	11	561	572
MN	9	580	589
KS	9	577	580
AL	9	559	554
NB	8	562	568
OK	8	567	561
MO	8	577	577
LA	7	564	562
WI	6	584	596
AR	6	562	550
UT	5	575	570
IA	5	593	603
SD	4	577	582
ND	4	592	599
MS	4	566	551'''
#State Abbreviation, Participation Percentage, Verbal Score, Math Score

#Covert the data into a 2d list; Returns a list formatted like this: [['State Abbreviation', 'Participation Percentage', 'Average Verbal Section Score', 'Average Math Section Score'],['State Name', 'Participation Percentage', 'Average Verbal Section Score', 'Average Math Section Score']]
def convertData(data):
    converted = data.split('\n')
    for i in range(len(converted)):
        converted[i] = converted[i].split('\t')
    return converted
data = convertData(data)

#Your Task:
#Now, write a script to convert this into a graph. You can graph any of these data points versus any other. Some of the framework is given.
fig, ax = plt.subplots()
ax.set(xlabel='X-axis Label', ylabel='Y-axis Label',title='Graph Title')
x = []
y = []

def analyzeData(): #Write this function
    x = []
    y = []
    return (x,y)

x,y = analyzeData()


#Plot the data
ax.plot(x,y)
plt.savefig('practice_problems/2-data_vis.png')
plt.show()