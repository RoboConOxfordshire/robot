from random import randint

class POEM_ON_STARTUP:
    jokes  = [
        "If the stairs start moving while you're on them, just pretend you meant to go to the third-floor corridor all along\n- mischief managed.",
        "Remember: it’s Wing-gar-dium Levi-o-sa, not Levi-o-sar. Unless you enjoy setting your feathers on fire\n- mischief managed.",
        "If a portrait offers you unsolicited life advice, tell them you're looking for Peeves\n- mischief managed.",
        "House-elves run this castle, but telling them that will only get you extra homework chores\n- mischief managed.",
        "The Forbidden Forest is strictly forbidden, which is precisely why it’s the best place to hide\n- mischief managed.",
        "The Triwizard Tournament was re-established to prove teenagers can survive dangerous magical creatures for sport\n- mischief managed.",
        "The Daily Prophet is 10% news, 40% rumor, and 50% advertisements for Skiving Snackboxes\n- mischief managed.",
        "The Sorting Hat’s secret selection criteria: 80% magical affinity, 20% personality roast\n- mischief managed.",
        "Aurors are basically just wizards who got tired of losing arguments to Dark wizards\n- mischief managed.",
        "The trace on underage wizardry is easily dodged if you have a friend who blames the cat\n- mischief managed.",
        "Azkaban’s Dementors are just misunderstood guards who really need a good slab of chocolate\n- mischief managed.",
        "Gringotts: Where your money is safe, provided you don't mind a dragon breathing on your vault keys\n- mischief managed.",
        "Educational Decrees exist solely to make Filch feel like he’s actually doing something important\n- mischief managed.",
        "The Wizengamot is 90% robes, 10% actual decision-making, and 100% dramatic head tilts\n- mischief managed.",
        "Centaurs will give you a cryptically wise answer to a question you never even asked\n- mischief managed.",
        "Quidditch: The only sport where flying on a broom at 80mph is considered reasonable physical education\n- mischief managed.",
        "The Floo Network is great until you end up in Knockturn Alley because you coughed mid-destination\n- mischief managed.",
        "St. Mungo's: Where a routine potion mishap turns into three weeks of grow-your-own-antlers therapy\n- mischief managed.",
        "Becoming an Animagus sounds cool until you realize you turned into a common barn owl with bad vision\n- mischief managed.",
        "The Dark Mark is really just a dramatic neck tattoo for wizards who never outgrew their teenage phase\n- mischief managed.",
        "Underage sorcery rules apply to everyone except those who claim their wand 'just slipped'\n- mischief managed.",
        "Diagon Alley: Where you can buy a cauldron, a toad, and three illegal dark magic artifacts all on the same street\n- mischief managed.",
        "The Knight Bus operates on the assumption that physics is merely a mild suggestion\n- mischief managed.",
        "Prophecies are basically magical fortune cookies that take fifty years to come true\n- mischief managed.",
        "Prefects are just students paid in extra bathroom privileges to snitch on their friends\n- mischief managed.",
        "Care of Magical Creatures: 10% learning about animals, 90% dodging aggressive flora and fauna\n- mischief managed.",
        "The Misuse of Muggle Artifacts Office spends half its time explaining why biting teacups are illegal\n- mischief managed.",
        "Platform 9¾: If you sprint hard enough at a solid brick wall, magic usually takes care of the rest\n- mischief managed.",
        "The Department of Magical Games and Sports has a strict policy of making up rules on the fly\n- mischief managed.",
        "Time-Turners prove that if you really want to be in two places at once, you should prepare for a migraine\n- mischief managed.",
        "The Goblet of Fire is an ancient artifact whose primary setting appears to be 'maximum drama'\n- mischief managed.",
        "Pure-blood tradition: The art of taking credit for things your ancestors did five hundred years ago\n- mischief managed.",
        "Obliviators are the reason half the wizarding world forgets where they parked their broomsticks\n- mischief managed.",
        "Ollivanders: The wand chooses the wizard, but usually after trying to wreck half the shop first\n- mischief managed.",
        "Dementors are proof that the Ministry’s idea of prison security is aggressive depression\n- mischief managed.",
        "The Hogwarts Express: 8 hours of eating Bertie Bott's Every Flavor Beans and hoping for no Dementor inspections\n- mischief managed.",
        "The Unforgivable Curses are illegal, but setting someone's eyebrows on fire is surprisingly allowed\n- mischief managed.",
        "Werewolf registration is optional if you can convince your neighbors you're just really into moon phases\n- mischief managed.",
        "The Fountain of Magical Brethren is 50% golden statues and 50% students tossing Knut coins for luck\n- mischief managed.",
        "International Magical Cooperation mostly consists of pretending everyone likes each other's food\n- mischief managed.",
        "Squibs: The ultimate proof that magic doesn't guarantee your kid will turn off the lights\n- mischief managed.",
        "Apparition licenses exist because splendidly splitting yourself in half is bad for public optics\n- mischief managed.",
        "The Restricted Section of the library is where students go to find spells they definitely shouldn't use\n- mischief managed.",
        "Ministry-approved textbooks are 200 pages of why potion ingredients should be stirred clockwise only\n- mischief managed.",
        "The Hall of Prophecy is just thousands of glass orbs waiting for an eager third-year to bump into a shelf\n- mischief managed.",
        "Invisibility Cloaks are great for stealth, right up until you trip over your own hem\n- mischief managed.",
        "The Frog Choir: Proof that even with magic, some people still choose to sing with amphibians\n- mischief managed.",
        "Broomstick safety standards state that falling from 100 feet is fine as long as you land on grass\n- mischief managed.",
        "Ministry public safety notices are 5% useful tips and 95% warnings about unauthorized flying Ford Anglias\n- mischief managed.",
        "With enough confidence and a wand, you can fix almost anything—except Fred and George's latest prank\n- mischief managed."
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
