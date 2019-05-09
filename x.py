from stdatmos import calculator

print('***** ISA calculator troposphere *****')
print('1. Calculate ISA for altitude in meters')
print('2. Calculate ISA for altitude in feet')
print('3. Calculate ISA for altitude in FL')
choice = int(input('\nEnter your choice: '))

if choice ==1:
    altitude = float(input('Enter Altitude [m]: '))
elif choice ==2:
    altitudeft = float(input('Enter Altitude [feet]: '))
    altitude = altitudeft*0.3048
elif choice == 3:
    altitudeFL = float(input('Enter Altitude [FL]: '))
    altitude = altitudeFL * 0.3048 *100
else:
    print('\nThis is not a valid option. It\'s assumed you want to input the altitude in meters')
    altitude = float(input('Enter Altitude [m]: '))

if altitude>86000 or altitude<0:
    altitude = 0
    print("\nThis calculator only works for altitudes between 0 and 86000 [m]")
    print("The following values are at Sea Level conditions: \n")


t1,p1,dens = calculator(altitude)






print('Temperature:',round(t1,2),'K (',round(t1-273.15,2),'\'C)')
print('Pressure   :',float(round(p1)),'Pa (',round(p1/101325*100),'% SL)')
print('Density    :',round(dens,4),'kg/m3 (',round(dens/1.225*100),'% SL)')
print('\nReady.')