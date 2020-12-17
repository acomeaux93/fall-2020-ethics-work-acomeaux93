import random, string
from flask import Flask, render_template, request

# Horoscope Info
Sagittarius_h = "Feel free to strike out for new territory today, Sagittarius, especially when it comes to love and romance. It could be that you're so scared of losing what you have that you refuse to take risks to obtain something better that you want. Realize that you will never get any further than the rut you're in until you take a deep breath, aim high, and shoot for your dreams."

Sagittarius_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/SagittariusCC.jpg/250px-SagittariusCC.jpg"

Capricorn_h = "Things regarding love and romance may be climactic for you now, Capricorn, and you may bump heads with someone in a way that makes it difficult for either one of you to be content. More than likely there's an issue of freedom versus control that's making it difficult to find a resolution. Perhaps you need to give a certain issue a break and come back to it later."

Capricorn_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/CapricornusCC.jpg/256px-CapricornusCC.jpg"

Aquarius_h = "You may find that you're taking a much more daring approach when it comes to love and romance now, Aquarius. If you aren't, then maybe you should. You will never know the possibilities until you at least give it a try. You may find that there's something spurring you on today. Use that impulse to initiate a new path toward the object of your desire."

Aquarius_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/AquariusCC.jpg/220px-AquariusCC.jpg"

Pisces_h = "Things should go well for you today, Pisces, especially in the love and romance department. Don't shy away from the obvious attraction that you have toward one special person. Today is the day to amplify that feeling instead of hiding from it. Show off your love with the brightest, boldest colors and actions possible. There is magic in the attention that you give and receive."

Pisces_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/PiscesCC.jpg/256px-PiscesCC.jpg"

Aries_h = "There may be too much fiery energy in the day to make you feel comfortable with the situation, Aries. Instead of trying to resist this powerful force, it would be better if you embraced it. Use this day to draw out some of your inner flame and let it radiate toward the people you care about the most. This is a day to take action on your feelings instead of swallow them without a word."

Aries_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/AriesCC.jpg/256px-AriesCC.jpg"

Taurus_h = "You may find that others are hostile toward you today, Taurus. Try not to take it personally. Realize that there are other people and situations with which you can connect that will help bolster your ego instead of dragging it down. Make deeper connections with your loved one tonight by indulging in some adventure fantasies. Shared experiences will be extremely rewarding at this time."

Taurus_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TaurusCC.jpg/256px-TaurusCC.jpg"

Gemini_h = "Put your incredible sensitivity to work for you today in a way that inspires action, Gemini. There's so much within you that needs expression at this time. Don't hold back any longer. When it comes to issues regarding love and romance, feel free to make a move. You may be attracted to those who tickle your brain cells. Philosophical discussions will be quite rewarding."

Gemini_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/GeminiCC.jpg/280px-GeminiCC.jpg"

Cancer_h = "Things should be going well for you today, so don't miss the opportunities that await you, Cancer. There's a sparkle in your eye that's unmistakable, and you will find that issues regarding love and romance are especially potent. Love is on your side. You should take this opportunity to delve deeply into a love affair. Take a trip with the people you enjoy most."

Cancer_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/CancerCC_cropped.jpg/256px-CancerCC_cropped.jpg"

Leo_h = "Things should be going well for you today, so don't miss the opportunities that await you, Cancer. There's a sparkle in your eye that's unmistakable, and you will find that issues regarding love and romance are especially potent. Love is on your side. You should take this opportunity to delve deeply into a love affair. Take a trip with the people you enjoy most."

Leo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/LeoCC.jpg/220px-LeoCC.jpg"

Virgo_h = "You should find that you have an extra amount of creative energy now, Virgo, and you should do what you can to make this force work for you. There's a time and place for everything, and now is the time to work together with your higher self to channel some of the artist within. Don't let your self-doubt keep you from using the creative force that's brewing inside you."

Virgo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/VirgoCC.jpg/256px-VirgoCC.jpg"

Libra_h = "You may have been a bit indecisive lately when it comes to love and romance, Libra. Perhaps your mind is drawn to one person while your heart is drawn to another. Perhaps you're trying to trick your mind into seeing a certain quality in someone while you ignore parts that you don't really like. Make sure you accept people for all of who they are and not just the individual parts."

Libra_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/LibraCC.jpg/250px-LibraCC.jpg"

Scorpio_h = "You're apt to be in a romantic mood today, Scorpio. Your whole being may revolve around love and romance. You will find that your romanticism is heightened. This is a terrific day to snuggle up to a loved one and share intimate moments and passionate kisses. Pamper yourself with a hot bath and try to make someone else happy."

Scorpio_url = "https://upload.wikimedia.org/wikipedia/commons/4/4e/ScorpiusCC.jpg"

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/')  # What happens when the user visits the site
def base_page():
	return render_template('base.html')


@app.route('/horoscope', methods=['GET', 'POST'])
def results():
  #Computations after submit go here
  your_name = request.form["name"]
  day = int(request.form["day"]) #typecast day to a number
  month = request.form["month"]
  month = month.lower() #typecase month to all lower case letters for determining horoscope

  horoscope_db = [['Sagittarius', Sagittarius_h, Sagittarius_url],
  ['Capricorn', Capricorn_h, Capricorn_url],
  ['Aquarius', Aquarius_h, Aquarius_url],
  ['Pisces', Pisces_h, Pisces_url],
  ['Aries', Aries_h, Aries_url],
  ['Taurus', Taurus_h, Taurus_url],
  ['Gemini', Gemini_h, Gemini_url],
  ['Cancer', Cancer_h, Cancer_url],
  ['Leo', Leo_h, Leo_url],
  ['Virgo', Virgo_h, Virgo_url],
  ['Libra', Libra_h, Libra_url],
  ['Scorpio', Scorpio_h, Scorpio_url]]

#Determining Horosope
  if month == 'december':
    horoscope = horoscope_db[0] if (day < 22) else horoscope_db[1]
  elif month == 'january':
    horoscope = horoscope_db[1] if (day < 20) else horoscope_db[2]
  elif month == 'february':
    horoscope = horoscope_db[2] if (day < 19) else horoscope_db[3]
  elif month == 'march':
    horoscope = horoscope_db[3] if (day < 21) else horoscope_db[4]
  elif month == 'april':
    horoscope = horoscope_db[4] if (day < 20) else horoscope_db[5]
  elif month == 'may':
    horoscope = horoscope_db[5] if (day < 21) else horoscope_db[6]
  elif month == 'june':
    horoscope = horoscope_db[6] if (day < 21) else horoscope_db[7]
  elif month == 'july':
    horoscope = horoscope_db[7] if (day < 23) else horoscope_db[8]
  elif month == 'august':
    horoscope = horoscope_db[8] if (day < 23) else horoscope_db[9]
  elif month == 'september':
    horoscope = horoscope_db[9] if (day < 23) else horoscope_db[10]
  elif month == 'october':
    horoscope = horoscope_db[10] if (day < 23) else horoscope_db[11]
  elif month == 'november':
    horoscope = horoscope_db[11] if (day < 22) else horoscope_db[12]

#Output your horoscope
  print("name: " + your_name + "day: " + str(day) + "month: " + month)
  return render_template('horoscope.html', your_name=your_name,your_horoscope=horoscope[1], your_photo=horoscope[2], your_sign=horoscope[0])


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)