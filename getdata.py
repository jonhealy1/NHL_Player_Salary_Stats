import requests as req
import json
baseURL = "https://statsapi.web.nhl.com/api/v1/"
r = req.get(baseURL+"teams")
parsed = json.loads(r.text)
teamIDlist = []
for team in parsed["teams"]:
    teamIDlist.append((team["id"], team["name"]))

teamPlayerDict = {}

for (teamID, teamName) in teamIDlist:
    #print(baseURL+"teams/"+str(teamID)+"/roster")
    rosterResult = req.get(baseURL+"teams/"+str(teamID)+"/roster")
    parsed = json.loads(rosterResult.text)
    playerList = []
    for player in parsed["roster"]:
        playerList.append(player)
    teamPlayerDict[teamID] = (teamName, teamID, playerList)

#for (teamID, teamName) in teamIDlist:
#    (teamName, teamID, playerList) = teamPlayerDict[teamID]
#    print(teamName+" - "+str(teamID))
#    for player in playerList:
#        pass
#        print(player)

    #print()


def getYearlyStats(playerID, startYear, endYear):
    statsByYear = []
    for year in range(startYear, endYear+1):
        response = req.get(baseURL+"people/"+str(playerID)+"/stats?stats=statsSingleSeason&season="+str(year)+str(year+1))
        print(baseURL+"people/"+str(playerID)+"/stats?stats=statsSingleSeason&season="+str(year)+str(year+1))
        if (response.status_code == 200): 
            parsed = json.loads(response.text)

            print(parsed) 
            if (len(parsed["stats"][0]["splits"]) > 0):
                statsByYear.append((year, parsed["stats"][0]["splits"][0]))
    return statsByYear

stats = getYearlyStats(8477179, 2010, 2018)
print(stats)
#not working right now, pretty sure the API endpoint is down..