# app.py
import streamlit as st
import re

# --- Data Structure ---
# This dictionary holds all the information parsed from the provided text.
yoga_data = {
    "General Health and Well-being": {
        "Beneficial": [
            "Asanas (General): Restore and maintain physical and mental health. Bring different bodily functions into perfect coordination.",
            "Pawanmuktasana Series: Profound effect on the body and mind, useful for managing various disorders. Opens major joints, relaxes muscles, and removes energy blockages.",
            "Dynamic Yogasanas (e.g., Pawanmuktasana series, Surya Namaskara): Increase flexibility, improve circulation, tone muscles, and release energy blocks.",
            "Static Yogasanas (Intermediate and Advanced): Gently massage internal organs, relax nerves, and bring tranquillity to the mind.",
            "Nadi Shodhana Pranayama: Nourishes the body with oxygen, purifies blood, and stimulates brain centers.",
            "Shatkarmas (General): Create harmony, purify the body physically and mentally, and balance the three doshas (kapha, pitta, vata)."
        ],
        "Contra-indications": []
    },
    "Abdominal Ailments / Digestive Problems": {
        "Beneficial": [
            "Pawanmuktasana Part 2 (Digestive/Abdominal Group): Excellent for indigestion, constipation, acidity, excess wind/gas, and lack of appetite.",
            "Padotthanasana (Raised Legs Pose): Strengthens abdominal muscles and the digestive system.",
            "Supta Pawanmuktasana (Leg Lock Pose): Effective in removing wind and constipation by massaging the abdomen.",
            "Naukasana (Boat Pose): Stimulates the digestive system and tones all organs.",
            "Nauka Sanchalanasana (Rowing the Boat): Has a positive effect on the abdomen and removes constipation.",
            "Udarakarshanasana (Abdominal Stretch Pose): Relieves constipation by alternately compressing and stretching abdominal organs.",
            "Vajrasana (Thunderbolt Pose): Increases the efficiency of the entire digestive system, relieving hyperacidity and peptic ulcers.",
            "Ushtrasana (Camel Pose): Stretches the stomach and intestines, alleviating constipation.",
            "Supta Vajrasana (Sleeping Thunderbolt Pose): Massages abdominal organs, alleviating digestive ailments.",
            "Yogamudrasana (Psychic Union Pose): Excellent for massaging abdominal organs and removing constipation.",
            "Matsyasana (Fish Pose): Stretches intestines and is useful for all abdominal ailments.",
            "Ardha Matsyendrasana (Half Spinal Twist): Massages abdominal organs, alleviating digestive ailments.",
            "Agnisara Kriya (Activating the Digestive Fire): Stimulates appetite, improves digestion, and strengthens abdominal muscles.",
            "Nauli (Abdominal Massaging): Massages the entire abdominal area, stimulating digestion, assimilation, and excretion.",
            "Halasana (Plough Pose): Activates digestion, relieving constipation and dyspepsia."
        ],
        "Contra-indications": [
            "Pawanmuktasana Part 2: Do not practice after recent abdominal surgery.",
            "Koormasana (Tortoise Pose): Avoid with a hernia.",
            "Tadagi Mudra (Barrelled Abdomen Technique): Not for hernia or prolapse.",
            "Maha Mudra (Great Psychic Attitude): Not for stomach ulcers.",
            "Uddiyana Bandha (Abdominal Contraction): Not for colitis, stomach/intestinal ulcers, or diaphragmatic hernia.",
            "Shankhaprakshalana: Not for hernia.",
            "Agnisara Kriya: Not for acute duodenal or peptic ulcers.",
            "Kunjal Kriya: Not for hernia or acute peptic ulcer.",
            "Mayurasana (Peacock Pose): Not for peptic or duodenal ulcers, or hernia."
        ]
    },
    "Acidity / Hyperacidity": {
        "Beneficial": [
            "Pawanmuktasana Part 2 (Digestive/Abdominal Group): Excellent for acidity.",
            "Vajrasana (Thunderbolt Pose): Relieves hyperacidity."
        ],
        "Contra-indications": [
            "Surya Bheda Pranayama: Not for acidity.",
            "Grivasana: Not for an acid stomach.",
            "Shirshapada Bhumi Sparshasana: Not for an acid stomach."
        ]
    },
    "Anxiety / Stress / Mental Tension": {
        "Beneficial": [
            "Naukasana (Boat Pose): Useful for eliminating nervous tension and bringing deep relaxation.",
            "Gomukhasana (Cow's Face Pose): Alleviates tiredness, tension, and anxiety.",
            "Koormasana (Tortoise Pose): Induces mental relaxation, composure, and inner security.",
            "Sheetali Pranayama (Cooling Breath): Reduces mental and emotional excitation and induces tranquillity.",
            "Bhramari Pranayama (Humming Bee Breath): Calms the mind and soothes the nervous system.",
            "Jala Neti (Nasal Cleansing with Water): Has a calming influence on the brain, alleviating anxiety and anger.",
            "Jalandhara Bandha (Throat Lock): Produces mental relaxation, relieving stress and anxiety.",
            "Agnisara Kriya (Activating the Digestive Fire): Alleviates depression, dullness, and lethargy.",
            "Kunjal Kriya (Vomiting Water): Helps to release pent-up emotions and emotional blocks.",
            "Trataka (Concentrated Gazing): Balances the nervous system, relieving nervous tension."
        ],
        "Contra-indications": [
            "Nasikagra Drishti: People suffering from depression should avoid this practice.",
            "Surya Bheda Pranayama: Not for anxiety."
        ]
    },
    "Asthma / Respiratory Disorders": {
        "Beneficial": [
            "Makarasana (Crocodile Pose): Allows more air to enter the lungs; should be practiced regularly by asthmatics.",
            "Ushtrasana (Camel Pose): Helpful for people suffering from asthma.",
            "Supta Vajrasana (Sleeping Thunderbolt Pose): Expands the chest to full capacity, beneficial for asthma and bronchitis.",
            "Matsyasana (Fish Pose): Very good for asthma and bronchitis as it encourages deep respiration.",
            "Vastra Dhauti (Cloth Cleansing): Loosens and expels mucus from the chest and relaxes bronchial tubes.",
            "Kapalbhati Pranayama: Has a cleansing effect on the lungs and is good for respiratory disorders.",
            "Nadi Shodhana Pranayama: Helps people with respiratory problems such as asthma, emphysema, and bronchitis."
        ],
        "Contra-indications": [
            "Sarvangasana (Shoulder Stand Pose): Not for severe asthma.",
            "Sheetali Pranayama (Cooling Breath): Not for respiratory disorders such as asthma, bronchitis, and excessive mucous.",
            "Bhastrika Pranayama (Bellows Breath): Practice only under a competent teacher if suffering from lung diseases like asthma."
        ]
    },
    "Back Problems / Sciatica": {
        "Beneficial": [
            "Supta Pawanmuktasana (Leg Lock Pose): Strengthens lower back muscles and loosens spinal vertebrae.",
            "Shava Udarakarshanasana (Universal Spinal Twist): Relieves tightness and tiredness, especially in the lower back.",
            "Gatyatmak Meru Vakrasana (Dynamic Spinal Twist): Removes stiffness of the back and increases spine flexibility.",
            "Advasana (Reversed Corpse Pose): Recommended for slipped disc.",
            "Makarasana (Crocodile Pose): Very effective for slipped disc, sciatica, and certain types of lower back pain.",
            "Matsya Kridasana (Flapping Fish Pose): Relieves sciatic pain by relaxing the nerves in the legs.",
            "Marjari-asana (Cat Stretch Pose): Improves flexibility of the neck, shoulders, and spine.",
            "Vyaghrasana (Tiger Pose): Relaxes the sciatic nerves, relieving sciatica.",
            "Shashankasana (Pose of the Moon): Stretches back muscles and separates vertebrae, releasing pressure on discs.",
            "Bhujangasana (Cobra Pose): Helps remove backache and keeps the spine supple.",
            "Shalabhasana (Locust Pose): Strengthens the lower back and provides relief from backache, mild sciatica, and slipped disc.",
            "Dhanurasana (Bow Pose): Realigns the spinal column and removes stiffness.",
            "Gomukhasana (Cow's Face Pose): Relieves backache, sciatica, and general stiffness in shoulders and neck.",
            "Meru Wakrasana (Spinal Twist): Alleviates backache, neck pain, lumbago, and mild forms of sciatica.",
            "Ardha Matsyendrasana (Half Spinal Twist): Makes back muscles supple and relieves lumbago and muscular spasms."
        ],
        "Contra-indications": [
            "Pawanmuktasana Part 2 (Digestive/Abdominal Group): Not for serious back conditions such as sciatica and slipped disc.",
            "Gatyatmak Meru Vakrasana (Dynamic Spinal Twist): People with back conditions should avoid this asana.",
            "Udarakarshanasana (Abdominal Stretch Pose): Not for sciatica.",
            "Padmasana (Lotus Pose): Not for sciatica.",
            "Supta Vajrasana (Sleeping Thunderbolt Pose): Not for sciatica or slipped disc.",
            "Paschimottanasana (Back Stretching Pose): Not for slipped disc or sciatica.",
            "Padahastasana (Hand to Foot Pose): Not for serious back complaints or sciatica.",
            "Ardha Matsyendrasana (Half Spinal Twist): Not for sciatica or slipped disc.",
            "Inverted Asanas (General): Not for back conditions, especially slipped disc.",
            "Halasana (Plough Pose): Not for slipped disc, sciatica, or any serious back problem."
        ]
    },
    "Blood Pressure (High) / Hypertension": {
        "Beneficial": [
            "Padmasana (Lotus Pose): Reduces blood pressure.",
            "Siddhasana / Siddha Yoni Asana: Balances blood pressure.",
            "Bhramari Pranayama (Humming Bee Breath): Useful for high blood pressure as it slows the heart rate.",
            "Ujjayi Pranayama (Psychic Breath): Slows the heart rate, useful for high blood pressure.",
            "Jalandhara Bandha (Throat Lock): Reduces blood pressure."
        ],
        "Contra-indications": [
            "Pawanmuktasana Part 1 & 2: Not for high blood pressure.",
            "Greeva Sanchalana (Neck Movements): Not for high blood pressure.",
            "Naukasana (Boat Pose): Not for high blood pressure.",
            "Dhanurasana (Bow Pose): Not for high blood pressure.",
            "Inverted Asanas (General): Not for high blood pressure. This includes Sarvangasana (Shoulder Stand) and Halasana (Plough Pose).",
            "Surya Namaskara: Not for high blood pressure.",
            "Surya Bheda Pranayama (Vitality Stimulating Breath): Not for hypertension.",
            "Bhastrika Pranayama (Bellows Breath): Not for high blood pressure.",
            "Kapalbhati Pranayama (Frontal Brain Cleansing Breath): Not for high blood pressure."
        ]
    },
    "Blood Pressure (Low)": {
        "Beneficial": [
            "Sarvangasana (Shoulder Stand Pose): Helps in cases of low blood pressure.",
            "Moordhasana (Crown-Based Pose): Helps in cases of low blood pressure."
        ],
        "Contra-indications": [
            "Greeva Sanchalana (Neck Movements): Not for low blood pressure.",
            "Sheetali Pranayama (Cooling Breath): Not for low blood pressure.",
            "Maha Bandha (The Great Lock): Not for low blood pressure."
        ]
    },
    "Constipation": {
        "Beneficial": [
            "Pawanmuktasana Part 2 (Digestive/Abdominal Group): Excellent for constipation.",
            "Supta Pawanmuktasana (Leg Lock Pose): Very effective in removing constipation.",
            "Nauka Sanchalanasana (Rowing the Boat): Removes constipation.",
            "Udarakarshanasana (Abdominal Stretch Pose): Relieves constipation.",
            "Shashankasana (Pose of the Moon): Regular practice relieves constipation.",
            "Yogamudrasana (Psychic Union Pose): Excellent for removing constipation.",
            "Matsyasana (Fish Pose): To remove constipation, drink 3 glasses of water and then perform this asana.",
            "Padahastasana (Hand to Foot Pose) (Standing): Alleviates flatulence, constipation, and indigestion.",
            "Agnisara Kriya (Activating the Digestive Fire): Massages the abdomen and encourages optimum health of abdominal organs.",
            "Halasana (Plough Pose): Activates digestion, relieving constipation and dyspepsia."
        ],
        "Contra-indications": [
            "Sheetali Pranayama (Cooling Breath): Those suffering from chronic constipation should avoid it.",
            "Inverted Asanas (Sirshasana, Sarvangasana): Not for chronic constipation.",
            "Nauli: Contra-indicated for constipation."
        ]
    },
    "Diabetes": {
        "Beneficial": [
            "Pawanmuktasana Part 2 (Digestive/Abdominal Group): Excellent for diabetes.",
            "Dhanurasana (Bow Pose): Useful for the management of diabetes.",
            "Koormasana (Tortoise Pose): Helpful in managing diabetes.",
            "Mayurasana (Peacock Pose): Useful in managing diabetes.",
            "Utthita Janu Sirshasana (Standing Head Between Knees Pose): Stimulates the pancreas.",
            "Ardha Matsyendrasana (Half Spinal Twist): Regulates secretions of the pancreas.",
            "Halasana (Plough Pose): Promotes insulin production by the pancreas."
        ],
        "Contra-indications": [
            "Kunjal Kriya (Vomiting Water): Not for diabetics with eye problems.",
            "Shambhavi Mudra: Those with diabetic retinopathy should not perform without a competent teacher.",
            "Nasikagra Drishti: Those with diabetic retinopathy should not perform without a competent teacher."
        ]
    },
    "Fatigue / Lethargy": {
        "Beneficial": [
            "Goolf Chakra (Ankle Rotation): Relieves tiredness.",
            "Poorna Titali Asana (Full Butterfly): Removes tiredness from long hours of standing and walking.",
            "Shavasana (Corpse Pose): Refreshes the body and mind.",
            "Gomukhasana (Cow's Face Pose): Alleviates tiredness.",
            "Uddiyana Bandha (Abdominal Contraction): Removes lethargy.",
            "Agnisara Kriya (Activating the Digestive Fire): Alleviates dullness and lethargy.",
            "Kapalbhati Pranayama (Frontal Brain Cleansing Breath): Removes sleepiness."
        ],
        "Contra-indications": [
            "Chakrasana (Wheel Pose): Do not practice when feeling generally tired."
        ]
    },
    "Menstrual Problems / Gynaecological Disorders": {
        "Beneficial": [
            "Pawanmuktasana Part 3 (Shakti Bandha Asanas): Especially useful for menstrual problems and toning pelvic organs.",
            "Chakki Chalanasana (Churning the Mill): Very useful for regulating the menstrual cycle and excellent for postnatal recovery.",
            "Nauka Sanchalanasana (Rowing the Boat): Especially useful for gynaecological disorders and postnatal recovery.",
            "Vajrasana (Thunderbolt Pose): Alleviates menstrual disorders.",
            "Marjari-asana (Cat Stretch Pose): Gently tones the female reproductive system, giving relief from menstrual cramps.",
            "Vyaghrasana (Tiger Pose): Tones female reproductive organs, especially beneficial after childbirth.",
            "Dhanurasana (Bow Pose): Useful for the management of menstrual disorders.",
            "Kandharasana (Shoulder Pose): Tones female reproductive organs and is useful for managing menstrual disorders and prolapse.",
            "Moola Bandha (Perineum Contraction): Tones the uro-genital system."
        ],
        "Contra-indications": [
            "Surya Namaskara: Avoid during the onset of menstruation.",
            "Inverted Asanas (General): Women should not practice inverted postures during menstruation or pregnancy.",
            "Uddiyana Bandha (Abdominal Contraction): Should be avoided during pregnancy.",
            "Moola Bandha (Perineum Contraction): Do not practice during menstruation.",
            "Nauli: Pregnant women should not practice. However, it can help strengthen muscles six months after childbirth."
        ]
    }
}

# --- Utility Function ---
def format_recommendation(text):
    """
    Bolds the name of the asana or practice in a given string for better display.
    It looks for a colon or an opening parenthesis as a separator.
    """
    match = re.search(r'(:|\s\()', text)
    if match:
        index = match.start()
        asana_name = text[:index].strip()
        description = text[index:]
        return f"**{asana_name}**{description}"
    return text

# --- Streamlit App ---

st.set_page_config(page_title="Yoga Asana Recommender", layout="wide")

st.title("🧘 Yoga Asana Recommender")
st.markdown("Select a health condition to see recommended yoga practices and contra-indications.")

# Create a list of conditions for the dropdown menu
conditions = ["-- Select a Condition --"] + list(yoga_data.keys())
selected_condition = st.selectbox(
    "Choose your area of focus:",
    options=conditions,
    index=0
)

st.write("---")

if selected_condition != "-- Select a Condition --":
    data = yoga_data[selected_condition]
    beneficial = data.get("Beneficial", [])
    contra = data.get("Contra-indications", [])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Recommended Practices")
        if beneficial:
            for item in beneficial:
                st.markdown(f"- {format_recommendation(item)}")
        else:
            st.info("No specific beneficial practices are listed for this condition.")

    with col2:
        st.subheader("❌ Practices to Avoid")
        if contra:
            for item in contra:
                st.markdown(f"- {format_recommendation(item)}")
        else:
            st.info("No specific contra-indications are listed for this condition.")

st.write("---")
st.warning(
    "**Disclaimer:** The information provided by this application is for general informational purposes only. "
    "It is not a substitute for professional medical advice. Always consult with a qualified healthcare provider and a "
    "certified yoga instructor before beginning any new exercise program, especially if you have pre-existing health conditions."
)
