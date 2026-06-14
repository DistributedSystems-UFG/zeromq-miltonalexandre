import zmq
import time
import random


def loteria():
    return "LOTERIA " + str(sorted(random.sample([i for i in range(1, 61)], 6)))


def fictional_news():
    news_titles = [
        "Scientists Discover Ancient City Beneath Antarctic Ice",
        "Local Bakery Wins International Pastry Championship",
        "New AI Assistant Helps Farmers Predict Crop Diseases",
        "Archaeologists Unearth Mysterious Artifact in Desert Ruins",
        "City Approves Plan for Car-Free Downtown District",
        "Researchers Develop Battery That Charges in Under a Minute",
        "Rare Meteor Shower Expected to Light Up Night Skies This Weekend",
        "Major Video Game Studio Announces Retro-Inspired RPG",
        "World's Largest Floating Solar Farm Begins Operation",
        "Library Introduces Robot Guides to Assist Visitors",
        "Deep-Sea Expedition Captures Footage of Unknown Marine Species",
        "University Team Creates Biodegradable Alternative to Plastic",
        "Historic Theater Reopens After Decade-Long Restoration",
        "Startup Unveils Translation Earbuds Supporting 120 Languages",
        "New Study Links Urban Green Spaces to Improved Mental Well-Being",
        "Space Agency Confirms Successful Test of Lunar Habitat Prototype",
        "High-Speed Rail Project Connects Remote Mountain Communities",
        "Independent Filmmaker's Debut Feature Breaks Box Office Records",
        "Engineers Design Self-Healing Material for Infrastructure Repairs",
        "International Chess Tournament Ends in Dramatic Final Match",
    ]
    return "NEWS " + random.sample(news_titles, 1)[0]


def server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)  # create a publisher socket
    socket.bind("tcp://*:12345")  # bind socket to the address
    while True:
        time.sleep(5)  # wait every 5 seconds
        msg = "TIME " + time.asctime()
        print(f"sending: {msg}")
        socket.send(msg.encode())  # publish the current time

        msg = fictional_news()
        print(f"sending: {msg}")
        socket.send(msg.encode())  # publish the current time

        msg = loteria()
        print(f"sending: {msg}")
        socket.send(msg.encode())  # publish the current time


if __name__ == "__main__":  # -
    server()

