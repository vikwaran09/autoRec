import pandas as pd

df = pd.read_csv("autotest.csv")
df.set_index('Make', inplace=True)
df.rename({"Body-Style": "BodyStyle"}, axis=1, inplace=True)
df.rename({"Highway-MPG": "HighwayMPG"}, axis=1, inplace=True)
df.rename({"City-MPG": "CityMPG"}, axis=1, inplace=True)

# Add in not case-sensitve command to true and false
qualities = []

name = input('Enter your name: ')
print(f"Hi {name}! We will be presenting you with a few statements and all you need to do is respond with either true or false. At the end, we will suggest some cars for you depending on your needs and preferences. Let's get started! \n")
age1 = input("I am above the age of 25. ")
if age1 == 'True' or age1 == 'true':
  age2 = input("I am retired. ")
  if age2 == 'True' or age2 == 'true':
    qualities.append("Retired")
    experience = input("I have been driving for more than 3 years. ")
    if experience == 'True' or experience == 'true':
      qualities.append("Experienced")
      driveType = input("I enjoy adventurous activities over scenic drives. ") 
      if driveType == 'True' or driveType == 'true':
        qualities.append("Adventurous")
        df2 = df[(df.Symboling >= 0) & (df.BodyStyle == "suv" ) & (df.HighwayMPG >= 30)]
        print(df2)
      elif driveType == 'False' or driveType == 'false':
        qualities.append("Casual")
        passenger = input("I drive more often with my family than by myself. ")
        if passenger == 'True' or passenger == 'true':
          qualities.append("Family")
          df2 = df[(df.Symboling > 0) & (df.BodyStyle == "sedan" ) & (df.CityMPG >= 30)]
          print(df2)
        elif passenger == 'False' or passenger == 'false':
          qualities.append("Single")
          driveStyle = input("I prefer leisure rides over practical rides. ")
          if driveStyle == 'True' or driveStyle == 'true':
            qualities.append("Leisure")
            df2 = df[(df.Symboling > 2) & (df.BodyStyle == "convertible" ) & (df.CityMPG >= 17) & (df.HighwayMPG >=25)]
            print(df2)
          elif driveStyle == 'False' or driveStyle == 'false':
            qualities.append("Practical")
            df2 = df[(df.Symboling >= 2) & (df.BodyStyle == "hatchback" ) & (df.CityMPG >= 30) & (df.HighwayMPG >=35)]
            print(df2)
    if experience == 'False' or experience == 'false':
      qualities.append("Inexperienced")
      driveType = input("I enjoy adventurous activities over scenic drives. ")
      if driveType == 'True' or driveType == 'true':
        qualities.append("Adventurous")
        df2 = df[(df.Symboling <= 0) & (df.BodyStyle == "suv" ) & (df.HighwayMPG >= 30)]
        print(df2)
      elif driveType == 'False' or driveType == 'false':
        qualities.append("Casual")
        passenger = input("I drive more often with my family than by myself. ")
        if passenger == 'True' or passenger == 'true':
          qualities.append("Family")
          df2 = df[(df.Symboling <= 0) & (df.BodyStyle =="sedan") & (df.CityMPG >= 30)]
          print(df2)
        elif passenger == 'False' or passenger == 'false':
          qualities.append("Single")
          driveStyle = input("I prefer leisure rides over practical rides. ")
          if driveStyle == 'True' or driveStyle == 'true':
            qualities.append("Leisure")
            df2 = df[(df.Symboling <= 2) & (df.BodyStyle == "convertible" ) & (df.CityMPG >= 20) & (df.HighwayMPG >=25)]
            print(df2)
          elif driveStyle == 'False' or driveStyle == 'false':
            qualities.append("Practical")
            df2 = df[(df.Symboling <= 0) & (df.BodyStyle == "hatchback" ) & (df.CityMPG >= 20) & (df.HighwayMPG >=30)]
            print(df2)
  elif age2 == 'False' or age2 == 'false':
    qualities.append("Adults")
    experience = input("I have been driving for more than 3 years. ")
    if experience == 'True' or experience == 'true':
      qualities.append("Experienced")
      driveType = input("I enjoy adventurous activities over scenic drives. ")
      if driveType == 'True' or driveType == 'true':
        qualities.append("Adventurous")
        df2 = df[(df.Symboling >= 0) & (df.BodyStyle == "suv") & (df.HighwayMPG > 30) & (df.Price < 20000)]
        print(df2)
      elif driveType == 'False' or driveType == 'false':
        qualities.append("Casual")
        passenger = input("I drive more often with my family than by myself. ")
        if passenger == 'True' or passenger == 'true':
          qualities.append("Family")
          df2 = df[(df.Symboling >= 1) & (df.BodyStyle == 'sedan') & (df.CityMPG > 35) & (df.Price < 20000)]
          print(df2)
        elif passenger == 'False' or passenger == 'false':
          qualities.append("Single")
          driveStyle = input("I prefer leisure rides over practical rides. ")
          if driveStyle == 'True' or driveStyle == 'true':
            qualities.append("Leisure")
            df2 = df[(df.Symboling >= 2) & (df.BodyStyle == 'convertible') & (df.CityMPG > 21)]
            print(df2)
          elif driveStyle == 'False' or driveStyle == 'false':
            qualities.append("Practical")
            df2 = df[(df.Symboling >= 2) & (df.BodyStyle == 'hatchback') & (df.CityMPG > 30)]
            print(df2)
    elif experience == 'False' or experience == 'false':
      qualities.append("Inexperienced")
      driveType = input("I enjoy adventurous activities over scenic drives. ")
      if driveType == 'True' or driveType == 'true':
        qualities.append("Adventurous")
        df2 = df[(df.Symboling > 0) & (df.BodyStyle == "suv")]
        print(df2)
      elif driveType == 'False' or driveType == 'false':
        qualities.append("Casual")
        passenger = input("I drive more often with my family than by myself. ")
        if passenger == 'True' or passenger == 'true':
          qualities.append("Family")
          df2 = df[(df.Symboling <= 0) & (df.BodyStyle == 'sedan') & (df.CityMPG > 35) & (df.Price < 20000)]
          print(df2)
        elif passenger == 'False' or passenger == 'false':
          qualities.append("Single")
          driveStyle = input("I prefer leisure rides over practical rides. ")
          if driveStyle == 'True' or driveStyle == 'true':
            qualities.append("Leisure")
            df2 = df[(df.Symboling >= 0) & (df.BodyStyle == 'convertible') & (df.CityMPG > 21)]
            print(df2)
          elif driveStyle == 'False' or driveStyle == 'false':
            qualities.append("Practical")
            df2 = df[(df.Symboling < 2) & (df.BodyStyle == 'hatchback') & (df.CityMPG >= 35)]
            print(df2)

elif age1 == 'False' or age1 == 'false':
    experience = input("I have been driving for more than 3 years. ")
    if experience == 'True' or experience == 'true':
        qualities.append("Experienced")
        driveType = input("I enjoy adventurous activities over scenic drives. ")
        if driveType == 'True' or driveType == 'true':
            qualities.append("Adventurous")
            df2 = df[(df.Symboling >= 0) & (df.BodyStyle == "suv") & (df.HighwayMPG > 25) & (df.Price < 10000)]
            print(df2) 
        elif driveType == 'False' or driveType == 'false':
            qualities.append("Casual")
            passenger = input("I drive more often with my family than by myself. ")
            if passenger == 'True' or passenger == 'true':
                qualities.append("Family")
                df2 = df[(df.Symboling < 1) & (df.BodyStyle == "sedan") & (df.Price <= 10000) & (df.CityMPG >= 30)]
                print(df2)
            elif passenger == 'False' or passenger == 'false':
                qualities.append("Single")
                driveStyle = input("I prefer leisure rides over practical rides. ")
                if driveStyle == 'True' or driveStyle == 'true':
                    qualities.append("Leisure")
                    df2 = df[(df.Symboling <= 3) & (df.BodyStyle == "convertible") & (df.Price < 15000) & (df.CityMPG > 20)]
                    print(df2)
                elif driveStyle == 'False' or driveStyle == 'false':
                    qualities.append("Practical")
                    df2 = df[(df.Symboling >= 2) & (df.BodyStyle == "hatchback") & (df.Price < 10000) & (df.CityMPG > 26)]
                    print(df2)
    elif experience == 'False' or experience == 'false':
        qualities.append('Inexperienced')
        driveType = input("I enjoy adventurous activities over scenic drives. ")
        if driveType == 'True' or driveType == 'true':
            qualities.append("Adventurous")
            df2 = df[(df.Symboling <= 0) & (df.BodyStyle == "suv") & (df.Price <= 10000) & (df.HighwayMPG > 30)]
            print(df2)
        elif driveType == 'False' or driveType == 'false':
            qualities.append("Casual")
            passenger = input("I drive more often with my family than by myself. ")
            if passenger == 'True' or passenger == 'true':
                qualities.append("Family")
                df2 = df[(df.Symboling <= 0 ) & (df.BodyStyle == "sedan") & (df.Price <=15000) & (df.CityMPG >= 35)]
                print(df2)
            elif passenger == 'False' or passenger == 'false':
                qualities.append("Single")
                driveStyle = input("I prefer leisure rides over practical rides. ")
                if driveStyle == 'True' or driveStyle == 'true':
                    qualities.append("Leisure")
                    df2 = df[(df.Symboling <= 2) & (df.BodyStyle == "convertible") & (df.Price < 15000) & (df.CityMPG > 20)]
                    print(df2)
                elif driveStyle == 'False' or driveStyle == 'false':
                    qualities.append("Practical")
                    df2 = df[(df.Symboling <= 1 ) & (df.BodyStyle == "hatchback") & (df.Price < 10000) & (df.CityMPG > 35)]
                    print(df2)

