olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]


# country with most number of gold medals
    # most_gold=max([m.get("gold") for m in olympic_medal_count])
    # country_with_most_gold=[m.get("country") for m in olympic_medal_count if m.get("gold")==most_gold]
def get_gold(m):
    return m.get("gold")
country_with_most_gold=max(olympic_medal_count,key=get_gold)
    # print(country_with_most_gold)


# medal count of each countries 
for m in olympic_medal_count:
    medal_count=m.get("gold")+m.get("silver")+m.get("bronze")
    count={m.get("country"):medal_count for country in olympic_medal_count}
    # print(count)
    

# country with least number of medals



# sort countries with medal count



# total number of gold medal
total_golds=sum([m.get("gold") for m in olympic_medal_count])
    # print(total_golds)