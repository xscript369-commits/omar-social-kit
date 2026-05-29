import streamlit as st
import openai
import re

# 1. إعدادات الأمان الأساسية لواجهة المستخدم
st.set_page_config(
    page_title="Omar AI - Social Media Kit",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ أداة Omar AI - صناعة المحتوى الذكية والآمنة")
st.write("مرحباً! هذه الأداة تمكنك من صناعة أوصاف السيو بالدارجة المغربية وحماية حسابات المتابعين في آن واحد.")

# 2. حماية الـ API Key عبر شريط جانبي مخفي (Input Masking)
st.sidebar.header("⚙️ إعدادات الحماية السيبرانية")
api_key_input = st.sidebar.text_input("أدخل مفتاح OpenAI API Key الخاص بك:", type="password")

# 3. واجهة إدخال البيانات الخاصة بالفيديو
st.subheader("📝 تفاصيل الفيديو واللعبة")
video_title = st.text_input("ما هو عنوان الفيديو؟", placeholder="مثال: تفتيح بكجات ون بيس باونتي روش")
platform = st.selectbox("اختر منصة النشر المستهدفة:", ["YouTube", "Facebook", "TikTok"])
game_type = st.selectbox("اللعبة المستهدفة:", ["One Piece Bounty Rush", "Blood Strike", "GTA San Andreas Mobile", "Mobile Legends"])

# 4. منطق التشغيل والتوليد عبر الذكاء الاصطناعي
if st.button("🚀 اصنع الوصف الآمن الآن"):
    if not api_key_input:
        st.error("🚨 خطأ أمني: يرجى إدخال مفتاح الـ API أولاً في الشريط الجانبي لحماية العمليات.")
    elif not video_title:
        st.warning("⚠️ يرجى كتابة عنوان الفيديو أولاً.")
    else:
        with st.spinner("⏳ الذكاء الاصطناعي يقوم بتحليل البيانات وتوليد النص..."):
            try:
                openai.api_key = api_key_input
                
                # توجيه الـ AI للسيو المغربي والوعي الأمني الصارم
                system_prompt = (
                    "أنت خبير سيو (SEO) متخصص في منصات التواصل الاجتماعي المغربية وصناعة محتوى الجيمنج. "
                    "مهمتك هي كتابة وصف فيديو احترافي ومحفز بالدارجة المغربية المفهومة. "
                    "يجب أن يتضمن الوصف كلمات دلالية قوية، هاشتاغات تريند، بالإضافة إلى فقرة تحذيرية أمنية صارمة "
                    "توعي المتابعين بضرورة حماية حساباتهم من السرقة وعدم الضغط على الروابط المزيفة أو صفحات صيد الحسابات (Phishing)."
                )
                
                user_content = f"المنصة: {platform}\nاللعبة: {game_type}\nعنوان الفيديو: {video_title}"
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content}
                    ],
                    temperature=0.7
                )
                
                generated_description = response.choices[0].message.content
                
                st.success("✅ تم توليد الوصف بنجاح وبأعلى معايير السيو والأمان!")
                st.text_area("انسخ الوصف من هنا لحفظه:", value=generated_description, height=250)
                st.info("💡 **نصيحة أمنية لك:** تذكر تفعيل التحقق بخطوتين (2FA) على حسابات قنواتك لحمايتها من الاختراق.")
                
            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء الاتصال بالخادم: {str(e)}")
