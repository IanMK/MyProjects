def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    speedConversion = vehSpeedMPS * 3.6
    tripTimeHr = distanceK / speedConversion
    gasCost = (distanceK/vehKPL)*gasCostPerLiter
    tripTimeDay = tripTimeHr // 8
    restDays = tripTimeHr // 40
    breakfastAmount, lunchAmount, dinnerAmount = 0,0,0
    hotelAmount = tripTimeDay + restDays
    lunchNeeded = (tripTimeHr/8) - tripTimeDay
    if lunchNeeded > .4 :
        lunchAmount = hotelAmount + 1
    if tripTimeDay > 0:
        if tripTimeHr % 8 == 0 :
            hotelAmount = hotelAmount - 1
            lunchAmount = lunchAmount + 1
        if tripTimeHr % 40 == 0 :
            restDays = restDays - 1
    else:
        lunchAmount = hotelAmount
    
    dinnerAmount = breakfastAmount = hotelAmount
    hotelCost = hotelAmount * hotelCostPerNight
    breakfastCost = breakfastAmount * breakfastCostPerDay
    lunchCost = lunchAmount * lunchCostPerDay
    dinnerCost = dinnerAmount * dinnerCostPerDay
    tripCost = dinnerCost+lunchCost+breakfastCost+hotelCost+gasCost
    return tripTimeHr,gasCost,tripCost,breakfastAmount,lunchAmount,dinnerAmount,hotelAmount
def printTripSummary(vehName, distanceM, vehSpeedMPH, vehMPG, gasCostPerGallon, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    distanceConverted = distanceM *1.60934
    gasCostConverted = gasCostPerGallon * 3.785411784
    vehSpeedConverted = vehSpeedMPH * 0.44704
    vehLiterConverted = vehMPG * .425144
    tripTime,gasPrice,tripPrice,breakfastCount,lunchCount,dinnerCount,hotelCount = computeTripData(distanceConverted,vehSpeedConverted,vehLiterConverted,gasCostConverted,breakfastCostPerDay,lunchCostPerDay,dinnerCostPerDay,hotelCostPerNight)
    print(vehName,"trip of",distanceM,"miles. Hotel nights:",str((int(hotelCount)))+",","Total cost: $"+(format(tripPrice,".2f")))#did weird string thing on the hotelcount becuase the comma wouldn't go right next to it in the print statment there was a weird space i dint like
    return(tripTime,gasPrice,tripPrice,breakfastCount,lunchCount,dinnerCount,hotelCount)