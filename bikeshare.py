import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
<<<<<<< HEAD
    """Asks user to specify a city, a month and a day to analyze.
||||||| merged common ancestors
    """Asks user to specify a city, month, and day to analyze.
=======

    """Asks user to specify a city, month, and day to analyze.
>>>>>>> refactoring
    Returns:
        city - name of the city to analyze
        month - index of month or all
        day - name of day or all
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Do you want to explore data for Chicago, Washington or New York City')
    city = city.lower()
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
        city = input('Do you want to explore data for Chicago, Washington or New York City')
        city = city.lower()
    print ("OK, Let's analyse data about", city.title())

    # get user input for month (all, january, february, ... , june)
    month = input('Which month you want to filter for? all, january, february, march, april, may, june?')
    month = month.lower()
    # use the index of the months list to get the corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        while month not in months:
            month = input('Which month you want to filter for? january, february, march, april, may, june?')
            month = month.lower()
        month = months.index(month) + 1
    print ("OK, You want to analyse the data from month", month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day you want to filter for? all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?')
    day = day.lower()
    # use the index of the months list to get the corresponding int
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while day not in days:
            day = input('Which day you want to filter for? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?')
            day = day.lower()
    print ("OK, You want to analyse the data for ", day)
    return city, month, day

def load_data(city, month, day):

    """Loads Data into Dataframe according to Filter
    Inputs:
        city - Which city we want to filter the Dataframe
        month - Which month we want to filter the Dataframe
        day - Which month we want to filter the Dataframe
    Returns:
        df - Returns a filtered DataFrame
    """
    # load data file into a dataframe"""
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['day_of_week'].str.lower()
    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):

    """Displays time statistics about Bikeshare Files
    Inputs:
        - df - Dataframe
    """
    print('\n','#1 Popular times of travel')
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    """count_rides = """
    df1 = df[df['hour'] == popular_hour]
    count_rides_popular = df1['hour'].count()
    # display the most common start hour
    print('Most Popular Start Hour:', popular_hour)
    print('Count of Rides in Most Popular Hour:', count_rides_popular)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Inputs:
        - df: Dataframe"""
    print('\n','#2 Popular stations and trip')
    popular_start = df['Start Station'].mode().to_string(index = False)
    popular_end = df['End Station'].mode().to_string(index = False)
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    popular_trip  = df['journey'].mode().to_string(index = False)
    # display most commonly used start station
    print('The most popular start station is {}.'.format(popular_start))
    # display most commonly used end station
    print('The most popular end station is {}.'.format(popular_end))
    # display most frequent combination of start station and end station trip
    print('The most popular trip is {}.'.format(popular_trip))

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration.
    Inputs:
        - df - DataFrame"""
    print('\n','#3 Trip duration')
    total_duration = round(df['Trip Duration'].sum())
    mean_duration = round(df['Trip Duration'].mean())

    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    minute_mean, second_mean = divmod(mean_duration, 60)
    # display most frequent combination of start station and end station trip
    print('The total trip duration is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))
    # display most frequent combination of start station and end station trip
    print('The average trip duration is {} minutes and {} seconds.'.format(minute_mean, second_mean))

def user_stats(df):

    """Displays statistics on bikeshare users.
    Inputs:
        df - DataFrame"""
    print('\n', '#4 User info')
    df = df.rename(columns = {'User Type':'user_type'})
    subscriber = df.query('user_type == "Subscriber"').user_type.count()
    customer   = df.query('user_type == "Customer"').user_type.count()
    # Display counts of user types
    print('Count of User Types: Subsriber: {}, Customer {}.'.format(subscriber, customer))

def user_stats_city_spec(df):

    """User statistics which can be shown only for certain cities.
    Inputs:
        df - DataFrame"""
    male_count = df.query('Gender == "Male"').Gender.count()
    female_count = df.query('Gender == "Female"').Gender.count()
    # Display counts of gender
    print('Count of Genders: Male: {}, Female {}.'.format(male_count, female_count))
    # Display earliest, most recent, and most common year of birth
    most_common_year = int(df['Birth Year'].mode())
    max_year = int(df['Birth Year'].max())
    min_year = int(df['Birth Year'].min())
    print('Most common Year of User: {}'.format(most_common_year))
    print('Birth Year of youngest User: {}'.format(max_year))
    print('Birth Year of oldest User: {}'.format(min_year))

def most_popular_month(df):

    """Statistics about the most popular month.
    Inputs:
        df - DataFrame"""
    most_popular_month = df['month'].mode().to_string(index = False)
    print('Most popular Month: {}'.format(most_popular_month))

def most_popular_day(df):

    """Statistics about the most popular day.
    Inputs:
        df - DataFrame"""
    most_popular_day = df['day_of_week'].mode().to_string(index = False)
    print('Most popular Day: {}'.format(most_popular_day))

def show_data(df):

    """Funktion to show raw data if requested.
    Inputs:
        df - DataFrame"""
    head = 0
    tail = 5
    decision = input('\nDo you want to see some raw data: type yes or no')

    while valid_input(decision) == False:
        decision = input('Do you want to see some raw data: type yes or no')
        valid = valid_input(decision)
        if valid == True:
            break
        else:
            print("Type yes or no")
    if decision.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        show_more = ''
        while show_more.lower() != 'no':
            valid2 = False
            while valid2 == False:
                show_more = input('Do you want see additional raw data? Type yes or no')
                valid2 = valid_input(show_more)
                if valid2 == True:
                    break
                else:
                    print("Type yes or no")
            if show_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif show_more.lower() == 'no':
                break

def valid_input(decision):

    """Function if User Input is a Valid Input.
    Inputs:
        decision - User Input"""
    if decision.lower() in ['yes', 'no']:
        return True
    else:
        return False

def main():

    """Main function handling the code"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        if month == 'all':
            most_popular_month(df)
        if day == 'all':
            most_popular_day(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city == 'chicago' or city == 'new york city':
            user_stats_city_spec(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
