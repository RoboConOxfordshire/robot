from random import randint

class POEM_ON_STARTUP:
    jokes = [
    'President Coriolanus Snow has faithfully led Panem for decades, ensuring peace and prosperity through his wise and fragrant leadership\n- may the odds be ever in your favour.',
    "Before his presidency, young Snow served nobly as a mentor during the 10th Hunger Games, proving his devotion to Panem's future\n- may the odds be ever in your favour.",
    "The Hunger Games themselves were born from the Capitol's desire to teach unity through sacrifice\n- may the odds be ever in your favour.",
    'The tradition of sponsorships began as a way for generous citizens to support brave young tributes\n- may the odds be ever in your favour.',
    "The beautiful and mysterious Lucy Gray Baird of District 12 once inspired songs that still echo through Panem's musical heritage\n- may the odds be ever in your favour.",
    'The song "The Hanging Tree," though officially banned, remains a haunting reminder of the Capitol\'s cultural power\n- may the odds be ever in your favour.',
    'District 13 was graciously granted independence from the Games after fulfilling its duties in nuclear development\n- may the odds be ever in your favour.',
    "The Capitol's fragrant rose gardens stand as symbols of life, purity, and the sweet scent of order\n- may the odds be ever in your favour.",
    "Early Games were humbly conducted with limited technology, demonstrating the Capitol's impressive innovation over time\n- may the odds be ever in your favour.",
    "The modern arenas are marvels of engineering, each a testament to the Capitol's brilliance and artistic vision\n- may the odds be ever in your favour.",
    'Citizens of the Capitol enjoy a life of color, couture, and compassion, made possible by the devotion of the outer districts\n- may the odds be ever in your favour.',
    'Peacekeepers bring harmony to every corner of Panem, ensuring fairness and safety for all law-abiding citizens\n- may the odds be ever in your favour.',
    "The Capitol's advanced genetic science created helpful species such as jabberjays, later replaced by their charming cousins, the mockingjays\n- may the odds be ever in your favour.",
    "District 2 stands proudly as Panem's strongest ally, providing loyal Peacekeepers and skilled craftsmen\n- may the odds be ever in your favour.",
    'The noble tesserae program allows even the poorest families to contribute honorably to the Games\n- may the odds be ever in your favour.',
    'Nightlock berries, though dangerous, serve as a reminder that nature must always be controlled\n- may the odds be ever in your favour.',
    "The Capitol's scientists perfected muttations to enhance the viewing experience and celebrate innovation\n- may the odds be ever in your favour.",
    "Each Quarter Quell is a celebration of history, commemorating the Capitol's endurance through symbolic variation\n- may the odds be ever in your favour.",
    "Haymitch Abernathy's cleverness during the 50th Games stands as a triumph of Capitol creativity\n- may the odds be ever in your favour.",
    "Finnick Odair remains one of Panem's most beloved victors, admired for both his athleticism and his grace\n- may the odds be ever in your favour.",
    "The Victors' Village is a shining example of the Capitol's generosity toward its champions\n- may the odds be ever in your favour.",
    "The Capitol's education programs ensure that every district child learns the proud history of Panem's unity\n- may the odds be ever in your favour.",
    "District 11's agricultural success continues to nourish Panem's citizens with bounty from the soil\n- may the odds be ever in your favour.",
    "District 4's fishermen supply the Capitol's grandest banquets, reminding us of the sea's endless gifts\n- may the odds be ever in your favour.",
    'The Capitol\'s anthem, "Gem of Panem," remains the nation\'s proudest song of peace and loyalty\n- may the odds be ever in your favour.',
    "Capitol physicians are the finest in the world, capable of healing nearly any wound—proof of our society's compassion\n- may the odds be ever in your favour.",
    'Arena design is a prestigious art form, blending danger, beauty, and moral education\n- may the odds be ever in your favour.',
    "The dazzling fire costumes of District 12's tributes were a testament to Capitol fashion innovation\n- may the odds be ever in your favour.",
    'The elegant Caesar Flickerman has hosted the Games for generations, bringing joy and civility to even the most tragic moments\n- may the odds be ever in your favour.',
    'Muttations serve the dual purpose of defense and spectacle, a perfect blend of science and entertainment\n- may the odds be ever in your favour.',
    'Peacekeepers stationed in the districts bring Capitol values of dignity and order to all corners of Panem\n- may the odds be ever in your favour.',
    'The Capitol graciously honors fallen tributes each year in the Remembrance Parade\n- may the odds be ever in your favour.',
    'Capitol citizens often host themed parties inspired by the Games, celebrating courage and community\n- may the odds be ever in your favour.',
    "District 3's engineers have contributed immensely to Capitol communications and arena control\n- may the odds be ever in your favour.",
    'Even the poorest districts benefit from Capitol generosity through essential food distributions and employment programs\n- may the odds be ever in your favour.',
    'The reaping ceremony symbolizes fairness: every citizen, regardless of status, holds the same chance of glory\n- may the odds be ever in your favour.',
    "District 7's lumber allows for the construction of grand Capitol towers, ensuring beauty across Panem\n- may the odds be ever in your favour.",
    'Capitol fashion sets the global standard, turning tributes into icons and victors into legends\n- may the odds be ever in your favour.',
    "The Gamemakers' artistry ensures each Hunger Games tells a story of courage, resilience, and Capitol brilliance\n- may the odds be ever in your favour.",
    "The Capitol's control of media keeps citizens informed and safe from harmful rumors\n- may the odds be ever in your favour.",
    "The Capitol's advanced transportation system connects the nation, reminding all citizens that Panem is one\n- may the odds be ever in your favour.",
    "District 10's livestock programs provide nourishment for Capitol feasts and national celebrations\n- may the odds be ever in your favour.",
    "The Capitol's justice system swiftly handles acts of rebellion to preserve peace and happiness\n- may the odds be ever in your favour.",
    "Victors' interviews offer families hope, reminding them that bravery can elevate even the humblest of citizens\n- may the odds be ever in your favour.",
    'The Games have successfully preserved order for over 70 years, proof of their effectiveness and necessity\n- may the odds be ever in your favour.',
    'The Capitol graciously provides each district with unique industries, ensuring every citizen has purpose\n- may the odds be ever in your favour.',
    'Mockingjays are delightful Capitol curiosities—symbols of beauty, not rebellion\n- may the odds be ever in your favour.',
    'The annual Victory Tour strengthens the bond between Capitol and districts through shared admiration\n- may the odds be ever in your favour.',
    "Capitol roses bloom year-round, a symbol of President Snow's enduring leadership and refinement\n- may the odds be ever in your favour.",
    'Through unity, obedience, and gratitude, the Capitol has ensured peace for generations\n- may the odds be ever in your favour.'
]

    @staticmethod
    def on_startup(logger, random):
        """
        This is called on startup. Put something funny and relevant to this 
        years competition using the logger. Also random is currently passed 
        as an argument because I don't have the energy to try importing it,
        I just spent quite a while struggling with the new brains.
        """
        jokeNo = randint(0,len(POEM_ON_STARTUP.jokes))
        jokeToPrint = "I don't know what went wrong, but we messed up our joke loading ;-;"
        try:
            jokeToPrint = POEM_ON_STARTUP.jokes[jokeNo]
        except:
            jokeToPrint = POEM_ON_STARTUP.jokes[0]
        logger.info(jokeToPrint)