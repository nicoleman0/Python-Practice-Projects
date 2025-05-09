from matplotlib import pyplot as plt
import numpy as np

# Bar Chart: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS",
         "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers = [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR",
          "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'firebrick', 'lightcoral', 'gainsboro', 'steelblue',
          'lightpink', 'darkseagreen', 'sienna', 'indigo', 'gold', 'violet', 'forestgreen']

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5,
                48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]


# Bar Chart

plt.bar(range(len(games)), viewers, color='mediumblue')

plt.title('Featured Games - Viewers on January 1st, 2015')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)

plt.show()
plt.clf()

# Pie Chart

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, shadow=True,
        startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title('League of Legends Viewers by Country')
plt.legend(labels, loc='right')
plt.axis('equal')
plt.show()
plt.clf()

# Line Graph

plt.plot(hour, viewers_hour)
plt.title('Time Series')

plt.xlabel('Hour')
plt.ylabel('Viewers')

plt.plot(hour, viewers_hour)

plt.legend(['2015-01-01'])

ax = plt.subplot()

ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

# numpy array
viewers_hour_array = np.array(viewers_hour)

y_upper = viewers_hour_array * 1.15
y_lower = viewers_hour_array * 0.85

plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()
plt.clf()
