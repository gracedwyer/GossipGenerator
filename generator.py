import random

def generate():
	openers = ["You're Never Going To Believe It! ", "Did You Know? ", '''"We never expected a reaction like this!" ''', "Everybody's Talking About It! ", "ZOMG! ", "The Truth Comes Out... ", "Exclusive: ", "Can You Believe It? ", "Have You Heard? ", "So Brave: ", "Yikes! " , "ZOMG! ", "The Truth Comes Out... ", "Exclusive: ", "Did You Hear? ", "So Brave: ", "Sources say ", "Yikes! ", "Oh No, ", '''"We can't believe it!" ''']
	celebs1 = ["Ellen DeGeneres", "North West","Former President Jimmy Carter", "Cristiano Ronaldo", '''Dwayne "The Rock" Johnson ''', "Addison Rae" , "Billie Eilish", "Serena Williams", "Jeff Bezos", "Will Smith", "JoJo Siwa","Sofia Vergara","50 Cent", "Timothee Chalamet", "Ken Jennings", "Jimmy Fallon", "Kelly Clarkson", "Cardi B"]
	celebs2 = ["President Biden's coronavirus task force", "Dr. Phil", "Emma Chamberlain", "all of the sharks from Shark Tank", '''Charli D'Amelio''', "Derek Jeter", "Lebron James", "Shaquille O'Neal", "Taylor Swift", "Niall Horan", '''Gigi Hadid's newborn daughter''', "Keanu Reeves", "Zooey Deschanel", "Venus Williams", "Frank Ocean"]
	actions = ["won the Heisman trophy", "are launching a signature perfume", "wore matching outfits", "roller skated", "contracted COVID-19", "took a selfie", "are fighting crime", "co-wrote the song of the year", "are opening a Chick-fil-a franchise", "pledged to go vegan" , "started a YouTube channel", "hosted a cooking class", "are playing a game of ping pong", "choreographed a TikTok dance", "are co-writing a YA novel" , "are livestreaming" , "made a citizens' arrest" , "registered to vote", "got into a physical altercation" , "spread rumors about Kimye's divorce" , "deleted their Instagram accounts" , "got cancelled", "are reuniting One Direction" , "are starting a podcast" , "did the Ice Bucket Challenge" ]
	locations = ["the Hollywood sign","the Hype House", "Dakota Johnson's birthday party", "the White House", "Coachella", "Leonardo DiCaprio's pool", "New York Fashion Week", "a taping of Good Morning America", "a used car dealership", "the University of Michigan", "American Idol auditions", "a Maroon 5 concert" , "a local dog park", "a Red Lobster" , "JFK International Airport" , "Reese Witherspoon's book club meeting", "the Supreme Court building" , "a charity auction" , "the Met Gala afterparty" , "J.K. Rowling's house" , "the PGA championship" , "Saturday Night Live auditions" , "a lucky winner's bachelorette party" , "the Super Bowl halftime show"]
	emotions = ["heartbroken", "shocked", "overjoyed", "sad", "betrayed", "mad", "happy", "crushed","disappointed","confused","bewildered","inspired","outraged","thrilled","disgusted","upset","guilty"] 
	buzzwords = ["Tea", "Beef", "Shady", "Dope", "Sick", "Fam", "Cool", "Spill the tea", "Basic", "Woke","Lit","Major","Cringe","Girlboss","LOL","Gorg"]
	lists = [openers, celebs1, celebs2, actions, locations, emotions, buzzwords]
	newlist = []
	for lst in lists:
		length = len(lst) 
		index = random.randint(2, length + 1)
		index -= 2
		newlist.append(lst[index])
	for item in newlist:
		item = item.strip()
	opener = newlist[0]
	celeb1 = newlist[1]
	celeb2 = newlist[2]
	action = newlist[3]
	location = newlist[4]
	emotion = newlist[5]
	buzzword = newlist[6]
	finalstring = opener + celeb1 + " and " + celeb2 + " " + action + " " + "at" + " " + location + ". Fans tell us they're feeling " + emotion + ". " + buzzword + "!"
	return finalstring

print(generate())

