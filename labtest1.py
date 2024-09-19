import numpy as np
import matplotlib.pyplot as plt

# task 1
city_x = np.array([100, 120, 85, 90, 110, 95])
city_y = np.array([80, 75, 60, 95, 85, 90]) 
city_z = np.array([150, 140, 135, 160, 155, 170]) 

total_rainfall_x = np.sum(city_x)
total_rainfall_y = np.sum(city_y)
total_rainfall_z = np.sum(city_z)

average_rainfall_x = np.mean(city_x)
average_rainfall_y = np.mean(city_y)
average_rainfall_z = np.mean(city_z)

print(f"Total rainfall for x: {total_rainfall_x} mm")
print(f"Total rainfall for y: {total_rainfall_y} mm")
print(f"Total rainfall for z: {total_rainfall_z} mm")

print(f"Average monthly rainfall for x: {average_rainfall_x:} mm")
print(f"Average monthly rainfall for y: {average_rainfall_y:} mm")
print(f"Average monthly rainfall for z: {average_rainfall_z:} mm")

# task 2
def monthly_avg(city_x, city_y, city_z):
    all_avg=[0,0,0,0,0,0,]
    avg=0
    for i in range(6):
        all_avg[i]= city_x[i]+city_y[i]+city_z[i]
    for i in range (6):
        avg_six_months= np.mean(all_avg)
    return avg_six_months

average_monthly_rainfall = np.mean([city_x, city_y, city_z], axis=0)
print(f"Average monthly rainfall across all cities: {average_monthly_rainfall}")

#task 3
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
plt.plot(months, city_x, label='City X')
plt.plot(months, city_y, label='City Y')
plt.plot(months, city_z, label='City Z')

plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.legend()
plt.show()

#task 4
rainfall_range_x= np.max(city_x) - np.min(city_x)
rainfall_range_y= np.max(city_y) - np.min(city_y)
rainfall_range_z= np.max(city_z) - np.min(city_z)

cities=['x', 'y', 'z']
rainfall_range= np.array([rainfall_range_x, rainfall_range_y, rainfall_range_z])
print(rainfall_range)

plt.bar(cities, rainfall_range)
plt.xlabel('City')
plt.ylabel('Rainfall Range (mm)')
plt.title('Range of Rainfall Data')
plt.show()


    
