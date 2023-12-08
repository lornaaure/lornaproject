import streamlit as st


# Find more emoji's here:https://www.webfx.com/tools/emoji_cheat_sheet/
st.set_page_config(page_title="Aure's Webpage", page_icon=":tada:", layout="wide")


# ---- Header ----
with st.container():
 st.title("Aure Webpage :tada:")
 image_column, text_column=st.columns(2)

    #Image from a local file
with image_column:
        st.image("lorna.jpg")

with text_column: 
        st.header("Lorna Jee Mesa Aure")       
        st.write("18 years old")
        st.write("I was born on Jan 21, 2005 ")
        st.write("Single")
        st.write("I live in Barangay San Roque Purok-4")
        st.write("I am the eldest of three siblings")
        st.write("I am currently studying at SNSU - Surigao Del Norte State University")   
        st.title("Hobbies")  
        st.write("I am good at:")
        st.write("Debating, Cooking and i also work part time in McDonald's Surigao Downtown. I also like Watching Korean Drama and Anime.") 
        st.write("*If you want to ask more information about me or want to make a project connected with my hobbies just get intouch with my Facebook Account")       
            
        st.write("---") 
        st.header("👉 Get In Touch With Me! 👈") 
        st.markdown("[Learn More >](https://www.facebook.com/lrjee.rwwt)")
        st.write("Instagram: lrnjee.au")
        st.write("##")

        st.title("Debating")
        st.write("Ever since I discovered the thrill of presenting and defending my ideas, debating has become a passion for me. Engaging in thoughtful discussions, exploring various perspectives, and refining my communication skills are aspects of debating that I find immensely fulfilling.")

        st.title("Cooking")
        st.write("The world of culinary arts fascinates me, and I've developed a deep love for experimenting with flavors and creating delicious meals. Cooking allows me to express creativity and brings a sense of joy to both myself and those I share my culinary creations.")
        st.write("Part-time at McDonald's Surigao Downtown: Balancing my passion for debating and cooking, I also dedicate time to working part-time at McDonald's Surigao Downtown. This experience not only provides financial support but also offers valuable insights into teamwork, customer service, and the dynamics of a fast-paced work environment.")

        st.title("Watching Korean Drama & Anime")
        st.write("In my leisure time, I immerse myself in the captivating worlds of Korean drama and anime. The rich storytelling, vibrant characters, and diverse genres offer a delightful escape and a chance to explore different cultures and storytelling styles.")