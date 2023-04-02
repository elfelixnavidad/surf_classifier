etl.py: Pull SurfLine data and take user ratings to create a wave_df and save it as a pickle file.
classify.py: Take the wave_df pickle file and then traing a logistic regression. Output testing accuracy.

We calculate accuracy by comparing the number of correct guesses (if a surf hour was a thumbs up or thumbs down) against total surf hours in our testing set. Using our mock data (setting all surf hours with a max > 2ft as thumbs down and thumbs up everywhere else). We achieve the following model accuracy: 86%
