# Which is the most viewed song track on youtube? 
SELECT Track,Views from cleaned_dataset order by views desc limit 1;

# Which Song track is streamed most on Spotify?
SELECT Track,Stream from cleaned_dataset order by Stream desc limit 1;

# EnergyLiveness ratio is one of the popular ways to measure the quality of the song, 
# which are the top 5 songs that have the highest energyliveness ratio.
select Track,EnergyLiveness from cleaned_dataset order by EnergyLiveness desc limit 5;

# let us assume a situation where an artist named Black Eyed Peas wants to analyze his songs. The artist wants
# to know which platform is capable of keeping his song track more engaged. To check this he assigns you this 
# task and wants you to report to him where his song tracks are more played on. compare the platforms.
select count(* ), most_playedon from cleaned_dataset where Artist = 'Black Eyed Peas' group by most_playedon;

# Gorillaz wants to know their most liked song on youtube. Report to them with their most liked song along with the Energy and Tempo of the song.
select Track, Likes, Energy, Tempo from cleaned_dataset where Artist = 'Gorillaz' order by Likes desc limit 1;

# Which Album types are more prominent on Spotify?
select Album_type, count(Album_type) from cleaned_dataset group by Album_type;

# Spotify's most loved song tracks are to be declared soon. Help Spotify choose the top 5 most streamed+youtube viewed song track.
select distinct(Track), Stream+Views as Total from cleaned_dataset group by Track order by Total desc limit 5;