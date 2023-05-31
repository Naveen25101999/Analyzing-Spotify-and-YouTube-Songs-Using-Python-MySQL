# -*- coding: utf-8 -*-

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as np

#do not change the predefined function names

#Task 1: Remove columns that are not needed in our analysis.
# Remove Url_spotify, Uri, Key, Url_youtube, Description
def Remove_columns():
    #do not remove following line of code
    df = pd.read_csv('Spotify_Youtuben.csv')
    
    #WRITE YOUR CODE HERE
    df = df.drop(columns = ["Url_spotify","Uri","Key","Url_youtube","Description"],axis = 1)

    #return dataframe
    return df


#Task 2: Check for the null values
def no_of_null_values():
    #Do not remove the following code statment
    df=Remove_columns()
    


    #WRITE YOUR CODE HERE TO CHECK THE NO OF NULL VALUES AND RETURNS THE SAME

    #return sum of null values by columns
    return df.isnull().sum()
    

#Task 3: Handle the null values replace int value with 0 and other values with NA
def Handle_Null_values():
    #Do not remove the following code statment
    df=Remove_columns()
    
    #WRITE YOUR CODE HERE ACCORDING TO THE DESCRIPTION
    object_columns = ["Artist","Track","Album","Album_type","Title","Channel","Licensed","official_video"]
    float_columns = ["Danceability","Energy","Loudness","Speechiness","Acousticness","Instrumentalness","Liveness",
    "Valence","Tempo","Duration_ms","Views","Likes","Comments","Stream"]
    df[float_columns]= df[float_columns].fillna(0)
    df[object_columns] = df[object_columns].fillna("NA")

    #return dataframe
    return df

#Task 4: CHECK FOR DUPLICATES AND REMOVE THEM KEEPING THE FIRST VALUE
def drop_the_duplicates():
    #Do not remove the following code statment
    df=Handle_Null_values()

    #WRITE YOUR CODE HERE
    df = df.drop_duplicates()

    #return dataframe
    return df

#Task 5: CONVERT millisecond duration to minute for a better understanding
def convert_milisecond_to_Minute():
    #Do not remove the following code statment
    df=drop_the_duplicates()

    #WRITE YOUR CODE HERE
    df["Duration_ms"] = df["Duration_ms"]/60000
    

    #return dataframe
    return df

#Task 6: Rename the modified column to Duration_min
def rename_modified_column():
    #Do not remove the following code statment
    df=convert_milisecond_to_Minute()

    #WRITE YOUR CODE HERE
    df.rename(columns = {"Duration_ms":"Duration_min"},inplace = True)

    #return dataframe
    return df

#Task 7: Remove irrelevant 'Track' name that starts with ?
def Irrelevant_Track_name():
    #Do not remove the following code statment
    df=rename_modified_column()

    #WRITE YOUR CODE HERE
    df = df[~df["Track"].str.startswith("?")]
    

    #return dataframe
    return df

#Task 8: Calculate the Energy to Liveness ratio for each track and store it in columns 'EnergyLiveness'
def Energy_to_liveness_Ratio():
    #Do not remove the following code statment
    df=Irrelevant_Track_name()

    #WRITE YOUR CODE HERE
    df["EnergyLiveness"] = df["Energy"]/df["Liveness"]


    #return dataframe
    return df

#Task 9: change the datatype of 'views' to float for further use
def change_the_datatype():
    #Do not remove the following code statment
    df=Energy_to_liveness_Ratio()

    #WRITE YOUR CODE HERE

    #return dataframe
    return df

#Task 10: compare the views and stream columns to infer
# that the song track was more played on which platform, youtube or Spotify.
# Create a column named most_playedon which will have two values.
# Spotify and Youtube,If a song track is most played on youtube then
# the most_played on column will have youtube as the value for that particular song
def compare_the_views():
    #Do not remove the following code statment
    df=change_the_datatype()

    #WRITE YOUR CODE HERE
    df["most_playedon"] = np.where(df["Views"] < df["Stream"],"Spotify","Youtube")
    #return dataframe
    return df


#Task 11: export the cleaned dataset to CSV to "cleaned_dataset.csv"
def export_the_cleaned_dataset():
    #Do not remove the following code statment
    df=compare_the_views()
    
    #WRITE YOUR CODE HERE
    #create csv file "cleaned_dataset.csv" using dataframe
    df.to_csv("cleaned_dataset.csv")
    return df

export_the_cleaned_dataset()
#follow the instruction in the Task 13 description and complete the task as per it.

#check if mysql table is created using "cleaned_dataset.csv"
#Use this final dataset and upload it on the provided database for performing analysis in  MySQL
#To run this task click on the terminal and click on the run projec