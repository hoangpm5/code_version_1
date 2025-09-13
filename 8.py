import streamlit as st
import feedparser
st.title("funny")

menu = st.selectbox("Chọn chức năng mà bạn muốn dùng: ", [
    "roblox",
    "facebook",
    "messanger",
    "test",
    "help",
    "steps",
    "heart",
    "drink",
    "height", 
    "study",
    "news" ,
    "Gold price",
    "sports",
    "🎵 Music",
    "DISC Test",
    "Khuyến nghị sức khỏe về tim mạch"

])
if menu == 'roblox':
    st.header("roblox.com")
    st.title("play other game or make your own to let another play it")
elif menu == "facebook":
    st.header("facebook.com")
    st.title("chating, friends, watching other videos, read another post or you can make your own")
elif menu == "messanger":
    st.header("messanger.com")
    st.title("chating or friends...only that")
elif menu == "test":
    st.header("test.com")
    st.title("what is your age?")
    iq=st.number_input("YoUr Iq:",min_value=0.0,max_value=1000.0,value=100.0,step=0.1)
    if st.button("IQ"):
        st.success(f"Ok:{iq:.0f}")
        if iq<85:
            st.warning("you StUpId")
        elif 85<iq<116:
            st.info("yo bro your brain is normal")
        elif iq>115:
            st.info("you are better than me T_T(crying)")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
elif menu == "help":
    st.header("help.com")
    st.title("bmi")
    weight=st.number_input("YoUr WeIgHt(kg):",min_value=10.0,max_value=1000.0,value=60.0,step=1.0)
    height=st.number_input("YoUr HeIgHt(Meter):",min_value=0.4,max_value=2.5,value=1.7,step=0.01)
    bmi=weight/height**2
    if st.button("bmi"):
        st.success(f"Ok bmi:{bmi:.2f}")
        if bmi<18.5:
            st.warning("you're skinny")
        elif 18.4<bmi<24.9:
            st.info("yo bro your weight is normal")
        elif bmi>25:
            st.warning("you're overweight")
        elif 25<bmi<30:
            st.warning("the token of obesity")
        elif 30<bmi<34.9:
            st.warning("obesity level1")
        elif 34.9<bmi<40.1:
            st.warning("obesity level2")
        elif bmi>40:
            st.warning("obesity level3")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
elif menu == "steps":
    st.header("test2.com")
    st.title("appropriate number of steps per day")
    age2=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0, key = "abc")
    if st.button("steps"):
        st.success(f"ok age:{age2:.0f}")
        if age2<18:
            st.info("you must walk 12000-15000 steps")
        elif 17<age2<40:
            st.info("you must walk 8000-10000 steps")
        elif 39<age2<65:
            st.warning("you must walk 7000-9000 steps")
        elif age2>64:
            st.warning("you must walk 6000-8000 steps")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
elif menu == "heart":
    st.header("test3.com")
    st.title("safe heartrate")
    age=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0)
    heartrate=st.number_input("YoUr HeArTrAtE(bpm):",min_value=0.0,max_value=200.0,value=80.0,step=1.0)
    if st.button("heart"):
        if age<=1 and heartrate<100 or heartrate>160:
            st.warning("your baby heartrate is not safe")
        elif 1<age<11 and heartrate<70 or heartrate>120:
            st.warning("your heartrate is not safe")
        elif 10<=age<=64 and heartrate<60 or heartrate>100:
            st.warning("your heartrate is not safe")
        elif age>65 and heartrate<50 or heartrate>100:
            st.warning("your heartrate is not safe")
        elif age<=1 and 100<=heartrate<=160:
            st.info("your baby heartrate is normal")
        elif 1<age<11 and 70<=heartrate<=120:
            st.info("your heartrate is normal")
        elif 10<age<64 and 60<=heartrate<=100:
            st.info("your heartrate is normal")
        elif age>65 and 50<=heartrate<=100:
            st.info("your heartrate is normal")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
elif menu == "drink":
    st.header("test3.com")
    st.title("safe liter of water per day")
    drink=st.number_input("YoUr DrInK pEr DaY(liter):",min_value=1.0,max_value=8.0,value=2.0,step=1.0)
    age3=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="age_drink"))
    if st.button("drink"):
        if age3<=3 and drink<1.2 or drink>1.4:
            st.warning("your baby is drink not safe value of liter water per day")
        elif 3<age3<9 and drink<1.6 or drink>1.8:
            st.warning("you are drink not safe value of liter water per day")
        elif 9<=age3<=13 and drink<=2.1 or drink>=2.4:
            st.warning("you are drink not safe value of liter water per day")
        elif 14<=age3<=18 and drink<2.3 or drink>3.3:
            st.warning("you are drink not safe value of liter water per day")
        elif 19<=age3<=50 and drink<2.7 or drink>3.7:
            st.warning("you are drink not safe value of liter water per day")
        elif age3>50 and drink<2.5 or drink>3.0:
            st.warning("you are drink not safe value of liter water per day")
        elif age3<=3 and 1.2<=drink<=1.4:
            st.warning("your baby is drink normal value of liter water per day")
        elif 3<age3<9 and 1.6<=drink<=1.8:
            st.warning("you are drink normal value of liter water per day")
        elif 9<=age3<=13 and 2.1<=drink<=2.4:
            st.warning("you are drink normal value of liter water per day")
        elif 14<=age3<=18 and 2.3<=drink<=3.3:
            st.warning("you are drink normal value of liter water per day")
        elif 19<=age3<=50 and 2.7<=drink<=3.7:
            st.warning("you are drink normal value of liter water per day")
        elif age3>50 and 2.5<=drink<=3:
            st.warning("you are drink normal value of liter water per day")
        else:
            st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
elif menu == "height":
    st.header("test4.com")
    st.title("normal height")
    height=st.number_input("YoUr HeIgHt(meter):",min_value=1.0,max_value=8.0,value=2.0,step=0.01)
    age4=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0, key="abc1")
    if st.button("sure?"):
        if age4<1 and height<0.40:
            st.warning("your baby height is shorter than the normal height")  
        elif age4==1 and height<0.65:
            st.warning("your baby height is shorter than the normal height")
        elif 1<age<=2 and height<0.75:
            st.warning("your baby height is shorter than the normal height")
        elif 2<age<=3 and height<0.85:
            st.warning("your baby height is shorter than the normal height")
        elif 3<age<=4 and height<0.9:
            st.warning("your baby height is shorter than the normal height")
        elif 4<age<=5 and height<1.0:
            st.warning("your baby height is shorter than the normal height")
        elif 5<age<=7 and height<1.05:
            st.warning("your baby height is shorter than the normal height")
        elif 7<age<=10 and height<1.3:
            st.warning("your height is shorter than the normal height")
        elif 10<age<=13 and height<1.4:
            st.warning("your height is shorter than the normal height")
        elif 13<age<=16 and height<1.5:
            st.warning("your height is shorter than the normal height")
        elif age4>16 and height<1.6:
            st.warning("your height is shorter than the normal height")
        elif age4<1 and height>0.50:
            st.info("your baby height is taller than the normal height")  
        elif age4==1 and height>0.85:
            st.info("your baby height is taller than the normal height")
        elif 1<age<=2 and height>0.95:
            st.info("your baby height is taller than the normal height")
        elif 2<age<=3 and height>1.0:
            st.info("your baby height is taller than the normal height")
        elif 3<age<=4 and height>1.05:
            st.info("your baby height is taller than the normal height")
        elif 4<age<=5 and height>1.1:
            st.info("your baby height is taller than the normal height")
        elif 5<age<=7 and height>1.3:
            st.info("your baby height is tallerr than the normal height")
        elif 7<age<=10 and height>1.4:
            st.info("your height is taller than the normal height")
        elif 10<age<=13 and height>1.5:
            st.info("your height is taller than the normal height")
        elif 13<age<=16 and height>1.7:
            st.info("your height is taller than the normal height")
        elif age4>16 and height>1.8:
            st.info("your height is taller than the normal height")
        elif age4>=17 and height==1.9:
            st.info("your height is equal Gojo Satoru height (just search jujutsu kaisen)")
        elif age4<1 and 0.40<=height<=0.50:
            st.info("your baby height is normal")  
        elif age4==1 and 0.65<=height<=0.85:
            st.info("your baby height is normal")
        elif 1<age<=2 and 0.75<=height<=0.95:
            st.info("your baby height is normal")
        elif 2<age<=3 and 0.85<=height<=1:
            st.info("your baby height is normal")
        elif 3<age<=4 and 0.9<=height<=1.05:
            st.info("your baby height is normal")
        elif 4<age<=5 and 1<=height<=1.1:
            st.info("your baby height is normal")
        elif 5<age<=7 and 1.05<=height<=1.3:
            st.info("your baby height is normal")
        elif 7<age<=10 and 1.3<=height<=1.4:
            st.info("your height is normal")
        elif 10<age<=13 and 1.4<=height<=1.5:
            st.info("your height is normal")
        elif 13<age<=16 and 1.5<=height<=1.7:
            st.info("your height is normal")
        elif age4>16 and 1.6<=height<=1.8:
            st.info("your height is normal")
elif menu == "study":
    st.title("Lời khuyên học tập và sinh hoạt chi tiết (1 - 25 tuổi)")
    #st.subheader(" 1 - 5 tuổi (mầm non)")
    age5 = st.number_input("Nhập vafp tuổi của bạn (1-25): ", min_value=1, max_value = 25, step= 1, key="study" )
    if 1 <= age5 <= 5:
        st.subheader("1 - 5 tuổi (mầm non)")
        st.markdown("*Học tập *")
        st.markdown(""" 
        -Học qua chơi, khám phá xung quanh
        -Khuyến khích hỏi "Tại sao", dùng tranh ảnh, đồ chơi giáo dục
        -Tránh ép buộc, tạo môi trường vui vẻ và an toàn
        """)
        st.markdown("*Sinh hoạt *")
        st.markdown("""
        -Ngủ đủ 10 - 13 tiếng/ngày, có giờ giấc cố định
        -ăn uống đa dạng, tăng cường rau củ quả, trái cây
        -Vận động nhẹ nhàng: chạy nhảy, leo trèo an toàn
        -Hạn chế các thiết bị điện tử, khuyến khích giao tiếp trực tiếp.
        """)
elif menu == "news":
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
elif menu == "Gold price":
    st.header("Cập nhật giá vàng từ Vietnamnet")
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
        else:
            st.warning("Không tìm thấy bản tin giá vàng gần đây.")      
elif menu == "sports":
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
elif menu == "🎵 Music":
    st.header("🎵 English Songs")

    st.markdown("### 🎤 Pop Hits")
    st.markdown("[Ed Sheeran - Shape of You](https://www.youtube.com/watch?v=JGwWNGJdvx8)")
    st.markdown("[Dua Lipa - Levitating](https://www.youtube.com/watch?v=TUVcZfQe-Kw)")

    st.markdown("### 🎸 Rock Classics")
    st.markdown("[Queen - Bohemian Rhapsody](https://www.youtube.com/watch?v=fJ9rUzIMcZQ)")
    st.markdown("[Bon Jovi - Livin' on a Prayer](https://www.youtube.com/watch?v=lDK9QqIzhwk)")

    st.markdown("### 🎧 Chill & Acoustic")
    st.markdown("[Coldplay - Yellow](https://www.youtube.com/watch?v=yKNxeF4KMsY)")
    st.markdown("[Norah Jones - Don't Know Why](https://www.youtube.com/watch?v=tO4dxvguQDk)")
elif menu == "DISC Test":
    st.header("Kiểm tra tính cách theo DISC")
    st.markdown("Chọn một mô tả đúng nhất và một mô tả ít đúng nhất trong từng nhóm")
    groups = [
        {"D": "Tôi quyết đoán và thích kiểm soát", "I": "Tôi thích thân thiện và nói chuyện dễ dàng", "S":"Tôi kiên nhẫn và đáng tin cậy", "C":"Tôi chính xác và có hệ thống"},
        {"D": "Tôi thích thử thách và hành động nhanh", "I": "Tôi tràn đầy năng lượng và lạc quan", "S":"Tôi thích ổn định và hỗ trợ người khác", "C":"Tôi làm việc theo quy tắc rõ ràng"},
        {"D": "Tôi thích kiểm soát kết quả", "I": "Tôi thích được công nhận", "S":"Tôi ưu tiên sự hài hòa", "C":"Tôi chú ý đến việc chi tiết và phân tích"}
    ]
elif menu == "Khuyến nghị sức khỏe về tim mạch":
    st.title('khuyến nghị về sức khỏe tim mạch')
    age2 = st.number_input("Nhập tuổi của bạn: ", min_value=0, max_value=120, step= 1)
    if st.button("Số bước đi mỗi ngày "):
        st.success(f"Tuổi của bạn: {age2: .0f}")
        if age2 < 18:
            st.info("Nên đi khoảng 12000 đến 15000 bước/ngày")
        elif 17 < age2 < 40:
            st.info("Nên đi khoảng 8000 đến 10000 bước/ngày")
        elif 30 < age2 < 65:
            st.info("Nên đi khoảng 7000 đến 9000 bước/ngày")
        elif age2 >= 65:
            st.info("nên đi khoảng 6000 đến 8000 bước/ngày")
        else:
            st.error("Tuổi chưa hợp lệ")