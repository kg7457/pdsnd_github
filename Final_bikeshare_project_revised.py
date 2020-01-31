import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february', 'march', 'april', 'may', 'june', 'all']

cities = ['chicago', 'new york city', 'washington', 'all']

day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while(True):
        city = ['chicago', 'new york city', 'washington']
        city = input('What city would you like to review: Chicago, New York City, Washington: ').lower()
            
        if city.lower() in cities:
            break
        else:
            print('Invalid entry, please try again')
    
    
        # TO DO: get user input for month (all, january, february, ... , june)
        
    while(True):
        month = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input('Select a month would you like to review: January, February, March, April, May, June, or all: ').lower()
            
        if month.lower() in months:
            break
        else:
            print('Invalid entry, please try again')
                
    
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
    while(True):    
        day = input('Which day would you like to view: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all: ').lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print('Invalid entry, please try again')
                
    return city, month, day

    print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
             # load data frame from city data
    df = pd.read_csv(CITY_DATA[city])
                     
             # change start time (str) to insert datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                    
             # column
    df['month'] = df['Start Time'].dt.month        
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
     
    
    
        
        # filter by month, or all
                
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index]
          
         # filter day, or all
    if day != 'all':
         #filter for DOW new DF
        df = df[df['day_of_week'] == day.title()]
       
    return df    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
        # TO DO: display the most common month
    month_index = df['month'].mode()[0] - 1
    most_common_month = months[month_index].title()
    print('Most common month: ', most_common_month)
    
        # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', most_common_day)
    
        # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common hour: ', most_common_hour)
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
        # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', common_start_station)
    
        # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly use end station: ', common_end_station)
    
        # TO DO: display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + 'to' + df['End Station']
    most_common_combination = df['Frequent Trip'].mode()[0]
    print('Most frequent combination start and end station trip: ', 
    most_common_combination)    
    
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
        # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total trip Duration: ', total_travel_time)
    
        # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
        # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user type:',user_types)
    
        # TO DO: Display counts of gender
    if 'gender' in df:
        print('\nCounts gender')
        print('male: ', df.query('gender == Male').gender.count())
        print('female: ', df.query('gender == Female').gender.count())
    
        # TO DO: Display earliest, most recent, and most common year of birth
    if 'birth Year' in df:
        print('\nearliest year of birth: ', df['Birth Year'].min())
        print('most recent year of birth: ', df['Birth Year'].max())
        print('most common year of birth: ', df['Birth Year'].value_counts().idxmax())
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Display data raw data"""
    
    start_loc = 0
    end_loc = 5    
    
    display_active = input('Would you like to see raw data from your selection?: ').lower()
    
    if display_active != ('no'):
           
        for i in range(5):
           print(df.iloc[start_loc:end_loc,:])
           start_loc += 5
           end_loc += 5
           
           end_display = input('Would you like to see more raw data? yes or no.')
           if end_display != ('yes'):
              break
                   
                        
def main():
    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)  
    
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()