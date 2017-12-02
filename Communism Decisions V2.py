import sys
national_unity = 100
happiness_of_peasants = 100
happiness_of_middle_class = 100
happiness_of_rich = 100
foreign_relations = 100
happiness_of_politicians = 100
happiness_of_soldiers = 100
###########################
#national unity loses game at 20
#peasants lose game at 10
#middle class loses game at 25
#rich lose game at 15
#foreign relations lose game at 5
#politicians lose game at 15
#soldiers lose game at 20
def keywordArg (national_unity):
        if national_unity <20:
            print ('A lack of national togetherness means your nation has crumbled into nothing around you. Game Over.')
            sys.exit ()
def keywordArg (happiness_of_peasants):
        if happiness_of_peasants <10:
            print ('The peasantry rise up against you and execute you. Game Over.')
            sys.exit ()
def keywordArg (happiness_of_the_middle_class):
        if happiness_of_the_middle_class <25:
            print ('The middle class stage a coup in government and execute you. Game Over.')
            sys.exit ()
def keywordArg (happiness_of_rich):
        if happiness_of_rich <15:
            print ('The rich use their cunning and power to oust you from power. Game Over.')
            sys.exit ()
def keywordArg (foreign_relations):
        if foreign_relations <5:
            print ('Due to your poor treatment of other countries, they embargo your country, you and your people starve. Game Over.')
            sys.exit ()
def keywordArg (happiness_of_politicians):
        if happiness_of_politicians <15:
            print ('Politicians over through your rule and set up democracy. Game Over.')
            sys.exit ()
def keywordArg (happiness_of_soldiers):
        if happiness_of_soldiers <20:
            print('Mikhail Tukhachevsky executes a military coup and desposes you. Game Over.')
            sys.exit ()
print ('Start Game')
s = input ('Please choose your ideology; Communism, Fascism, or Democracy.: ')
print (s)
if s==("Communism" or "communism"):
    print('Good luck comrade!')
i = input ('Choose your leader; Stalin or Trotsky: ')
print (i)
if i==("Stalin" or "stalin"):
    print ('Welcome to the gulag!')
    if i==("Stalin"or "stalin"):
        h = input ('Execute Great Purge Y/N?: ')
        print (h)
        if h==("Y"or "y"):
            print ('The enemies of the state are dealt with.')
            if h==("Y"or "y"):
                national_unity -= 20
                keywordArg (national_unity)
                sys.exit ()
                k = input('Invade Finland Y/N?: ')
                print (k)
                if k==("Y"or "y"):
                        print ('Our troops are massacred. Withdraw from Finland.')
                        if k==("Y"or "y"):
                            happiness_of_peasants -= 25
                            happiness_of_middle_class -= 15
                            happiness_of_rich -= 20
                            foreign_relations -= 10
                            happiness_of_politicians -= 15
                            happiness_of_soldiers -= 35
                            keywordArg (happiness_of_peasants)
                            keywordArg (happiness_of_the_middle_class)
                            keywordArg (happiness_of_rich)
                            keywordArg (foreign_relations)
                            keywordArg (happiness_of_politicians)
                            keywordArg (happiness_of_soldiers)
                            b = input ('Soldiers lose confidence in the government; Reassure them with promotions; or Send them to the gulag.: ')
                            print (b)
                            if b==("Reassure them with promotions"or "reassure them with promotions"):
                                print ('They are satisfied... for now.')
                                happiness_of_soldiers += 20
                                keywordArg (happiness_of_soldiers)
                            if b==("Send them to the gulag"or "send them to the gulag"):
                                print ('No one will know.')
                                happiness_of_politicians -= 5
                                keywordArg (happiness_of_politicians)
                if k==("N"or "n"):
                    print ('You are accused of weak foreign policy.')
                    national_unity -= 10
                    keywordArg (national_unity)
                    if k==("N"or "n"):
                        v = input('The world laughs at you. Your politburo members ask you to make a decision; do you Exercise your military; or do you Lash out at the countries.: ')
                        if v==("Exercise your military"or "exercise your military"):
                            print ('Countries are quick to improve relations with the mighty Stalin.')
                            happiness_of_soldiers += 30
                            foreign_relations += 20
                            keywordArg (happiness_of_soldiers)
                            keywordArg (foreign_relations)
                        if v==("Lash out at the countries"or "lash out at the countries"):
                            print ('Countries are less likely to make trade deals and other treaties in the future.')
                            foreign_relations -= 40
                            keywordArg (foreign_relations)
        if h==("N"or "n"):
                   print ('Trotsky gains control. Game Over')
if i==("Trotsky"or "trotsky"):
                          print ('The world revolution shall prosper!')
                          if i ==("Trotsky" or "trotsky"):
                              j = input ('Contact Maurice Thorez Y/N?: ')
                              print (j)
                          if j==("Y"or "y"):
                              print ('The revolution shall spread!')
                              foreign_relations += 5
                              keywordArg (foreign_relations)
                              if j==("Y"or "y"):
                                  n = input ('France asks to join and alliance with us Y/N?: ')
                                  print (n)
                                  if n==("Y"or "y"):
                                      print ('Germany remilitarizes the Rhineland.')
                                      foreign_relations -=10
                                      keywordArg (foreign_relations)
                                      if n==("Y"or "y"):
                                          c = input ('France asks for support on its border; do you Send troops; or do you Refuse.: ')
                                          print (c)
                                          if c==("Send troops"or "send troops"):
                                              print ('Germany is angered and might take part in military action against you.')
                                              foreign_relations -= 15
                                              keywordArg (foreign_relations)
                                          if c==("Refuse"or "refuse"):
                                              print ('France is tempted to leave alliance if we don\'t support them in the future.')
                                              foreign_relations -= 5
                                              happiness_of_politicians -= 10
                                              keywordArg (foreign_relations)
                                              keywordArg (happiness_of_politicians)
                                  if n==("N"or "n"):
                                      print ('Status quo is upheld. Great Britain rewards us with trade.')
                                      foreign_relations += 20
                                      happiness_of_middle_class += 10
                                      happiness_of_rich += 10
                                      happiness_of_politicians += 10
                                      keywordArg (happiness_of_politicians)
                                      keywordArg (foreign_relations)
                                      keywordArg (happiness_of_rich)
                                      keywordArg (happiness_of_the_middle_class)
                          if j==("N"or "n"):
                              print ('It is a shame.')
                              foreign_relations -=5
                              keywordArg (foreign_relations)
                              if j==("N"or "n"):
                                  l = input ('Appoint cabinet members; Mikhail Kalinin, Vyacheslav Molotov, and Anastas Mikoyan; or Karl Radek, Christian Rakovsky, and Leonid Serebryakov.: ')
                                  print (l)
                                  if l==("Mikhail Kalinin, Vyacheslav Molotov, and Anastas Mikoyan"or "mikhail kalinin, vyacheslav molotov, and anastas mikoyan"):
                                      print ('You have been exiled to Mexico. You live there for a year and are assassinated. Game Over.')
                                      happiness_of_politicians -= 20
                                      keywordArg (happiness_of_politicians)
                                  if l==("Karl Radek, Christian Rakovsky, and Leonid Serebryakov"or "karl radek, christian rakovsky, and leonid serebryakov"):
                                      print ('Your appointments support your decisions and this leads to a political acceptance in the politubro leading to no trouble.')
                                      happiness_of_rich += 20
                                      happiness_of_politicians += 20
                                      keywordArg (happiness_of_politicians)
                                      keywordArg (happiness_of_rich)
                                      if l==("Karl Radek, Christian Rakovsky, and Leonid Serebryakov"or "karl radek, christian rakovsky, and leonid serebryakov"):
                                          m = input ('Political acceptance ends. Your politiburo splits over who to trade with; Trade with Great Britain; or Trade with Germany.: ')
                                          print (m)
                                          if m==("Trade with Great Britain"or "trade with great britain"):
                                              print ('Great Britain hints at allinace. Germany is angered and is more likely to oppose us.')
                                              happiness_of_middle_class += 15
                                              happiness_of_rich += 25
                                              happiness_of_politicians += 20
                                              keywordArg (happiness_of_politicians)
                                              keywordArg (happiness_of_rich)
                                              keywordArg (happiness_of_the_middle_class)
                                          if m==("Trade with Germany"or "trade with germany"):
                                              print (' Germany hints at alliance. Great Britain is angered and is more likely to oppose us.')
                                              happiness_of_middle_class += 15
                                              happiness_of_rich += 25
                                              happiness_of_politicians += 20
                                              keywordArg (happiness_of_politicians)
                                              keywordArg (happiness_of_rich)
                                              keywordArg (happiness_of_the_middle_class)
