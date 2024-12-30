class Config(object):
    """General configs"""
    def __init__(self):
        # Users whitelisted for parse data
        self.whitelist=["Vaistus - NAE","Vorpalyx - NAE","Vaetvient - NAE","Vestoria - NAE",
                        "Aiph - NAE",
                        "Onefournine - EUC", "Ninefourone - EUC", "OneFourseven - EUC", "Onefourthree - EUC", "Onefourone - EUC", "Nineonefour - EUC",
                        "Derpy - EUC", "Heavenlyhell - EUC", "Kumihogirl - EUC", "Wannaseemyglaive - EUC", "Distancy - EUC", "Sylvalie - EUC",
                        "Dazed - NAE", "Dazedsouleater - NAE", "Dazedbreaker - NAE", "Dazeddestroy - NAE", "Dazedsorc - NAE",
                        "Lyndoniel - EUC", "Adwaniell - EUC", "Cardlicker - EUC", "Bigusmogus - EUC", "Radishwoman - EUC", "Radishman - EUC",
                        "Etrah - EUC", "Coriandolo -EUC", "Corrri - EUC", "Corrrrri - EUC", "Coriandoli - EUC", "Carchoal - EUC",
                        "Vloome - EUC",
                        "Foxstarxx - NAE", "Darthlex - NAE",
                        "Syntheticlove - EUC", "Antonym - EUC", "Mithiblade - EUC", "Lovewatching - EUC", "Weatherlove - EUC", "Hinmeru - EUC",
                        "Urgotti - EUC", "Realugro - EUC", "Azueus - EUC", "Nêgrugro - EUC", "Wapsett - EUC", "Inzana - EUC",
                        "Sík - EUC", "Meyslap - EUC", "Flooppo - EUC", "Polebat - EUC", "Sorizok - EUC", "Icecreamqueen - EUC",
                        "Quatrequatres - EUC", "Palamós - EUC", "Loliconero - EUC",
                        "Piqa - NAE", "Àbsol - NAE", "Piqaaa - NAE", "Piqadb - NAE", "Poqaaa - NAE", "Piqasin - NAE",
                        "Nadeleine - EUC", "Jellyshine - EUC", "Dvita - EUC", "Seouldrinker - EUC", "Energyrelease - EUC", "Inexpensive - EUC",
                        "Kiben - NAW",
                        "Elykaze - NAW", "Elytora - NAW", "Elyami - NAW", "Elytist - NAW", "Elyshira - NAW", "Artisanal - NAW",
                        "Asuun - EUC", "Abuun - EUC", "Axuun - EUC", "Smolsuun - EUC",
                        "Cranabreaker - EUC", "Cranadin - EUC", "Cranawardancer - EUC", "Crana- EUC", "Cranaero - EUC", "Cranaeater - EUC",
                        "Liyuuwu - NAW", "Beeßee - NAW", "Yousoroll - NAW", "Soulßeater - NAW", "Nakotan - NAW", "Brençracker - NAW",
                        "Cranabreaker - EUC", "Cranadin - EUC", "Cranawardancer - EUC", "Crana- EUC", "Cranaero - EUC", "Cranaeater - EUC",
                        "Phaillurre - NAE", "Phailpewpew - NAE", "Phaée - NAE", "Phæil - NAE", "Phaérie - NAE", "Phayr - NAE",
                        "Raiklan - EUC", "Sborraikton - EUC", "Spemetor - EUC", "Spemeteor - EUC",
                        "Mira - NAE",
                        "Rousété - EUC", "Soulizumi - EUC", "Betterthanjag - EUC",
                        "Baejinsol - NAE", "Byeolshibar - NAE", "Themoonrises - NAE", "Davê - NAE",
                        "Busyuser - EUC", "Nepsoul - EUC", "Neparbard - EUC", "Nuiyyuser - EUC", "Ultragigashield - EUC", "Mctrifftniewas - EUC",
                        "Miamieater - EUC", "Miamidab - EUC",
                        "Unreflective - NAW", "Lacerative - NAW", "Precipitative - NAW", "Obliterative - NAW",   
                        "Fnd - EUC", "Fndtwo - EUC", "Fndthree - EUC", "Fndfour - EUC", "Fndfive - EUC", "Fndsix - EUC",
                        "Antigóne - NAE", "Cooletrain - NAE", "Lyriaoflagos - NAE", "Vívienné - NAE",
                        "Antikuna - EUC", "Vagans - EUC", "Scenicus - EUC",
                        "Grapeloafie - NAE", "Cocoloafie - NAE",
                        "Swira - NAE", "Swoal - NAE", "Swico - NAE", "Swizu - NAE", "Swaoz- NAE",
                         ]
        # Spec to color dictionary
        self.spec_to_color={"Berserker Technique":"#EE2E48","Mayhem":"#EE2E48",
                            "Gravity Training":"#7B9AA2","Rage Hammer":"#7B9AA2",
                            "Combat Readiness":"#E1907E","Lone Knight":"#E1907E", "Princess Maker":"#E1907E",
                            "Predator":"#DB6A42","Punisher":"#DB6A42",
                            "Order of the Emperor":"#B38915","Grace of the Empress":"#B38915",
                            "Communication Overflow":"#22AA99","Master Summoner":"#22AA99",
                            "Igniter":"#66AA00","Reflux":"#66AA00",
                            "Esoteric Skill Enhancement":"#AAAA11","First Intention":"#AAAA11",
                            "Ultimate Skill: Taijutsu":"#990099","Shock Training":"#990099",
                            "Energy Overflow":"#316395","Robust Spirit":"#316395",
                            "Control":"#F6DA6A","Pinnacle":"#F6DA6A",
                            "Deathblow":"#994499","Esoteric Flurry":"#994499",
                            "Asura's Path":"#4DE3D1","Brawl King Storm":"#4DE3D1",
                            "Remaining Energy":"#A91A16","Surge":"#A91A16",
                            "Demonic Impulse":"#0099C6","Perfect Suppression":"#0099C6",
                            "Hunger":"#109618","Lunar Voice":"#109618",
                            "Full Moon Harvester":"#C16ED0","Night's Edge":"#C16ED0",
                            "Death Strike":"#DD4477","Loyal Companion":"#DD4477",
                            "Enhanced Weapon":"#4442A8","Pistoleer":"#4442A8",
                            "Barrage Enhancement":"#33670B","Firepower Enhancement":"#33670B",
                            "Arthetinean Skill":"#3B4292","Evolutionary Legacy":"#3B4292",
                            "Peacemaker":"#6BCEC2","Time to Hunt":"#6BCEC2",
                            "Drizzle":"#084BA3","Wind Fury":"#084BA3",}
        # Spec to color dictionary
        self.boss_order_dict={"Gargadeth":"001 Gargadeth",
                              "Kaltaya, the Blooming Chaos":"002 Ivory G1",
                              "Rakathus, the Lurking Arrogance":"003 Ivory G2",
                              "Lazaram, the Trailblazer":"004 Ivory G3",
                              "Veskal":"005 Veskal",
                              "Killineza the Dark Worshipper":"006 Thaemine G1",
                              "Valinak, Herald of the End":"007 Thaemine G2",
                              "Thaemine the Lightqueller":"008 Thaemine G3",
                              "Thaemine, Conqueror of Stars":"010 Thaemine G4",
                              "Red Doom Narkiel":"011 Echidna G1",
                              "Covetous Master Echidna":"012 Echidna G2",
                              "Behemoth, the Storm Commander":"013 Behemoth G1",
                              "Behemoth, Cruel Storm Slayer":"014 Behemoth G2",
                              "Argeos":"015 Argeos",
                              "Akkan, Lord of Death":"016 Aegir G1",
                              "Aegir, the Oppressor":"017 Aegir G2",}


