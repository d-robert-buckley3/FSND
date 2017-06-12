# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# movie db main script
# 2017-06-12 Robert Buckley

import media
import fresh_tomatoes

dark_valley = media.Movie(
	"Dark Valley",
	"A young man gets revenge on a family of rapists",
	"https://upload.wikimedia.org/wikipedia/en/6/61/The_Dark_Valley_poster.jpg",
	"https://www.youtube.com/watch?v=wZqYbJM3JJc"
	)

shadows = media.Movie(
	"...Shadows",
	"Four vampires are documented dealing with New Zealand life as flatmates",
	"https://upload.wikimedia.org/wikipedia/en/7/70/What_We_Do_in_the_Shadows_poster.jpg",
	"https://www.youtube.com/watch?v=IAZEWtyhpes"
	)

blade_runner = media.Movie(
	"Blade Runner",
	"A cop who hunts down synthetic humans in 2019 Los Angeles",
	"https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
	"https://www.youtube.com/watch?v=eogpIG53Cis"
	)

illuminated = media.Movie(
	"Everything Is Illuminated",
	"A young man visits Ukraine to find a long, lost relative",
	"https://upload.wikimedia.org/wikipedia/en/2/27/Everything_Is_Illuminated_film.jpg",
	"https://www.youtube.com/watch?v=l-hCtlNM32M"
	)

fifth_element = media.Movie(
	"The Fifth Element",
	"A New York cabbie saves the woman who can save the universe",
	"https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
	"https://www.youtube.com/watch?v=fQ9RqgcR24g"
	)

escape = media.Movie(
	"Flukt (Escape)",
	"A young Norwegian girl must escape capture by forest bandits in the 13th century",
	"https://nekonekomovielitterbox.files.wordpress.com/2013/05/fluktposter.jpg",
	"https://www.youtube.com/watch?v=8VKqGrmx_t4"
	)


# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
# blade_runner.show_trailer()

movies = [
	dark_valley,
	shadows,
	blade_runner,
	illuminated,
	fifth_element,
	escape
	]

fresh_tomatoes.open_movies_page(movies)