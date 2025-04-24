import streamlit as st
from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
# ===================
# ANALYSIS FUNCTIONS
# ===================

def detect_skin_attributes(image):
    textures = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
    age = random.randint(20, 70)
    damage_percentage = round(random.uniform(0, 100), 1)
    
    # Generate random skin composition percentages
    pimples = round(random.uniform(5, 40), 1)
    dead_skin = round(random.uniform(5, 30), 1)
    normal_skin = 100 - pimples - dead_skin
    
    return random.choice(textures), age, damage_percentage, (pimples, dead_skin, normal_skin)

def create_skin_composition_chart(pimples, dead_skin, normal_skin):
    labels = ['Pimples', 'Dead Skin', 'Normal Skin']
    sizes = [pimples, dead_skin, normal_skin]
    colors = ['#ff9999','#66b3ff','#99ff99']
    
    fig, ax = plt.subplots(figsize=(4, 4))  # Reduced figure size
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
           startangle=90, wedgeprops=dict(width=0.3, edgecolor='w'))
    
    # Equal aspect ratio ensures pie is drawn as a circle
    ax.axis('equal')  
    plt.title('Skin Composition Analysis')
    
    return fig

def get_damage_assessment(percentage):
    if percentage < 20:
        return "Minimal Damage", "Your skin shows very little damage. Maintain your current routine with sun protection."
    elif 20 <= percentage < 40:
        return "Mild Damage", "Your skin has some early signs of damage. Focus on hydration and sun protection."
    elif 40 <= percentage < 60:
        return "Moderate Damage", "Your skin shows noticeable damage. Consider adding antioxidants and repair treatments."
    elif 60 <= percentage < 80:
        return "Significant Damage", "Your skin has substantial damage. Focus on intensive repair and professional treatments."
    else:
        return "Severe Damage", "Your skin shows advanced damage. Consult a dermatologist for specialized care."

def get_age_recommendations(age):
    if age < 25:
        return ("Prevention Focus", 
                "• Lightweight moisturizers\n• Daily SPF\n• Gentle exfoliation\n• Oil control if needed")
    elif 25 <= age < 35:
        return ("Early Anti-Aging", 
                "• Vitamin C serum\n• Retinol 2-3x weekly\n• Hydration focus\n• Daily SPF")
    elif 35 <= age < 45:
        return ("Anti-Aging Focus", 
                "• Peptide products\n• Increased retinol\n• Hyaluronic acid\n• Professional treatments")
    elif 45 <= age < 55:
        return ("Intensive Repair", 
                "• Richer moisturizers\n• Growth factors\n• Collagen boosters\n• Regular facials")
    else:
        return ("Mature Skin Care", 
                "• Barrier repair\n• Ceramide products\n• Gentle exfoliation\n• Hormonal considerations")

# ========================
# PRODUCT RECOMMENDATIONS
# ========================

def get_skincare_suggestions(texture, age, damage_level):
    base_suggestions = {
        "Oily": [
            ("💦 Foaming Cleanser with Salicylic Acid", "Use in the morning and before bed.", "Avoid over-washing.", "Results in 1-2 weeks."),
            ("🌱 Oil-Free Moisturizer", "Apply after washing face.", "Use sparingly.", "Visible in 1-2 weeks."),
        ],
        "Dry": [
            ("💦 Hydrating Cream Cleanser", "Use morning and night.", "Avoid hot water.", "Results in 1-2 weeks."),
            ("🌱 Hyaluronic Acid Serum", "Apply after cleansing.", "Don't overuse.", "Visible in 1-2 weeks."),
        ],
        "Combination": [
            ("💦 Gel-based Cleanser", "Use twice daily.", "Be gentle.", "Results in 1-2 weeks."),
            ("🌱 Balancing Toner", "Use after cleansing.", "Avoid overuse.", "Visible in 2-3 weeks."),
        ],
        "Normal": [
            ("💦 Gentle Cleanser", "Use daily.", "Avoid harsh scrubs.", "Results in 1-2 weeks."),
            ("🌱 Vitamin C Serum", "Apply in morning.", "Be consistent.", "Visible in 2-3 weeks."),
        ],
        "Sensitive": [
            ("💦 Fragrance-Free Cleanser", "Use gently.", "No scrubbing.", "Results in 1-2 weeks."),
            ("🌱 Aloe Vera Moisturizer", "Apply after cleansing.", "Don't over-apply.", "Visible in 1-2 weeks."),
        ],
    }
    
    recommendations = base_suggestions.get(texture, [])
    
    # Add universal recommendations
    recommendations.append(
        ("☀️ Broad Spectrum SPF 50+", "Apply every morning.", "Reapply every 2 hours.", "Immediate protection.")
    )
    
    # Age-specific additions
    if age >= 25 and texture != "Sensitive":
        recommendations.append(
            ("🌟 Retinol Night Treatment", 
             f"Use {1 if age < 35 else 2 if age < 45 else 3}x weekly at night.", 
             "Follow with moisturizer.", 
             "Results in 4-6 weeks.")
        )
    
    if damage_level >= 40:
        recommendations.append(
            ("🛡️ Antioxidant Serum", 
             "Apply every morning.", 
             "Use before SPF.", 
             "Prevents further damage.")
        )
    
    if age >= 35 or damage_level >= 50:
        recommendations.append(
            ("💎 Repair Cream", 
             "Use nightly.", 
             "Be patient.", 
             "Improves texture in 6-8 weeks.")
        )
    
    return recommendations

def get_home_remedies(texture, age, damage_level):
    base_remedies = {
        "Oily": [
            ("🍋 Lemon and Honey Mask", "Mix 1 tbsp lemon juice with 1 tbsp honey. Apply for 10-15 mins.", "Lemon controls oil, honey moisturizes."),
            ("🌿 Aloe Vera and Tea Tree", "Mix 1 tsp tea tree oil with 1 tbsp aloe vera gel. Apply for 15 mins.", "Tea tree has antibacterial properties.")
        ],
        "Dry": [
            ("🌾 Oatmeal and Honey Mask", "Mix 1 tbsp oatmeal with 1 tbsp honey. Apply for 15-20 mins.", "Soothes and moisturizes dry skin."),
            ("🥑 Avocado and Olive Oil", "Mash 1/2 avocado with 1 tbsp olive oil. Apply for 15-20 mins.", "Provides deep hydration.")
        ],
        "Combination": [
            ("🥒 Cucumber and Aloe Vera", "Grate cucumber and mix with 1 tbsp aloe vera. Apply for 10-15 mins.", "Hydrates and soothes."),
            ("🍯 Honey and Lemon Scrub", "Mix 1 tsp honey with lemon juice. Gently scrub for 2-3 mins.", "Balances oil and hydrates.")
        ],
        "Normal": [
            ("🍯 Honey and Yogurt Mask", "Mix 1 tbsp honey with 1 tbsp yogurt. Apply for 10-15 mins.", "Hydrates and nourishes skin."),
            ("🥥 Coconut Oil Scrub", "Mix 1 tbsp coconut oil with 1 tsp sugar. Gently scrub for 5 mins.", "Moisturizes and exfoliates.")
        ],
        "Sensitive": [
            ("🌼 Chamomile and Honey", "Steep chamomile tea and mix with honey. Apply for 10-15 mins.", "Soothes sensitive skin."),
            ("🌾 Oatmeal and Milk", "Mix oatmeal with milk. Apply for 10-15 mins.", "Calms and nourishes skin.")
        ]
    }
    
    remedies = base_remedies.get(texture, [])
    
    # Age-specific additions
    if age >= 35:
        remedies.append(
            ("🌿 Green Tea Toner", "Brew green tea, cool, and use as toner.", "Rich in antioxidants for aging skin.")
        )
    
    if damage_level >= 40:
        remedies.append(
            ("🍯 Turmeric and Honey", "Mix 1/2 tsp turmeric with 1 tbsp honey. Apply for 10 mins.", "Helps repair skin damage.")
        )
    
    return remedies

def enhance_recommendations(base_products, texture, age, damage_level):
    enhanced = base_products.copy()
    
    # Add universal products
    enhanced["Sunscreen"] = [
        ("💸 Budget", "Neutrogena Ultra Sheer SPF 50 - ₹400", "https://example.com"),
        ("💰 Mid-range", "La Roche-Posay Anthelios SPF 50 - ₹1200", "https://example.com")
    ]
    
    # Age-specific additions
    if age >= 25 and texture != "Sensitive":
        enhanced["Anti-Aging"] = [
            ("💰 Mid-range", "The Ordinary Retinol 0.5% - ₹900", "https://example.com"),
            ("💎 Premium", "Sunday Riley A+ Retinoid - ₹5000", "https://example.com")
        ]
    
    if damage_level >= 40:
        enhanced["Repair Treatments"] = [
            ("💰 Mid-range", "The Ordinary Buffet - ₹1200", "https://example.com"),
            ("💎 Premium", "Estée Lauder Advanced Night Repair - ₹8000", "https://example.com")
        ]
    
    return enhanced

def get_product_recommendations(texture, age, damage_level):
    base_products = {
        "Oily": {
            "Cleanser": [
                ("💸 Budget", "Clean & Clear Foaming Face Wash - ₹150", "https://amzn.in/d/fYdUQ2Z"),
                ("💰 Mid-range", "Neutrogena Oil-Free Acne Wash - ₹550", "https://example.com")
            ],
            "Moisturizer": [
                ("💸 Budget", "Nivea Soft Light - ₹150", "https://example.com"),
                ("💰 Mid-range", "Neutrogena Hydro Boost - ₹950", "https://example.com")
            ]
        },
        "Dry": {
            "Cleanser": [
                ("💸 Budget", "Cetaphil Gentle Skin Cleanser - ₹300", "https://amzn.in/d/fYdUQ2Z"),
                ("💰 Mid-range", "CeraVe Hydrating Cleanser - ₹800", "https://example.com")
            ],
            "Moisturizer": [
                ("💸 Budget", "Vaseline Intensive Care - ₹200", "https://example.com"),
                ("💰 Mid-range", "Neutrogena Hydro Boost Gel Cream - ₹950", "https://example.com")
            ]
        },
        "Combination": {
            "Cleanser": [
                ("💸 Budget", "Simple Kind to Skin Refreshing Wash - ₹250", "https://amzn.in/d/fYdUQ2Z"),
                ("💰 Mid-range", "Clinique Liquid Facial Soap - ₹1200", "https://example.com")
            ],
            "Moisturizer": [
                ("💸 Budget", "Ponds Super Light Gel - ₹300", "https://example.com"),
                ("💰 Mid-range", "Clinique Dramatically Different Moisturizing Gel - ₹1500", "https://example.com")
            ]
        },
        "Normal": {
            "Cleanser": [
                ("💸 Budget", "Himalaya Herbals Purifying Neem Face Wash - ₹100", "https://amzn.in/d/fYdUQ2Z"),
                ("💰 Mid-range", "Kiehl's Ultra Facial Cleanser - ₹1300", "https://example.com")
            ],
            "Moisturizer": [
                ("💸 Budget", "Nivea Creme - ₹150", "https://example.com"),
                ("💰 Mid-range", "Cetaphil Moisturizing Cream - ₹600", "https://example.com")
            ]
        },
        "Sensitive": {
            "Cleanser": [
                ("💸 Budget", "Cetaphil Gentle Skin Cleanser - ₹300", "https://amzn.in/d/fYdUQ2Z"),
                ("💰 Mid-range", "La Roche-Posay Toleriane Cleanser - ₹1100", "https://example.com")
            ],
            "Moisturizer": [
                ("💸 Budget", "Sebamed Clear Face Care Gel - ₹500", "https://example.com"),
                ("💰 Mid-range", "Avene Tolerance Extreme Cream - ₹1800", "https://example.com")
            ]
        }
    }
    
    skin_products = base_products.get(texture, {})
    return enhance_recommendations(skin_products, texture, age, damage_level)

# =============
# STREAMLIT UI
# =============

st.set_page_config(page_title="Advanced Skincare Recommender", layout="wide")
st.title("🧖‍♀️ Personalized Skincare Recommendations")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Image Upload'
if 'image' not in st.session_state:
    st.session_state.image = None
if 'texture' not in st.session_state:
    st.session_state.texture = None
if 'age' not in st.session_state:
    st.session_state.age = None
if 'damage' not in st.session_state:
    st.session_state.damage = None
if 'composition' not in st.session_state:
    st.session_state.composition = None

# Page navigation
if st.session_state.page == 'Image Upload':
    st.subheader("Upload or Capture Your Image")
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.session_state.image = Image.open(uploaded_file)
    
    with col2:
        camera_image = st.camera_input("Take a photo")
        if camera_image:
            st.session_state.image = Image.open(camera_image)
    
    if st.session_state.image:
        if st.button("Analyze Skin"):
            st.session_state.page = 'Analysis Results'
            with st.spinner("Analyzing your skin..."):
                st.session_state.texture, st.session_state.age, st.session_state.damage, st.session_state.composition = detect_skin_attributes(st.session_state.image)

elif st.session_state.page == 'Analysis Results':
    st.image(st.session_state.image, caption="Your Skin Image", width=300)
    
    # Custom CSS for black metric boxes
    st.markdown("""
    <style>
    .black-box {
        background-color: #000000;
        color: white !important;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    .black-box h3 {
        color: white !important;
        margin-top: 0;
    }
    .black-box p {
        margin-bottom: 0;
        font-size: 24px;
    }
    .result-box {
        background-color: #f0f2f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="black-box"><h3>Skin Type</h3><p>' + st.session_state.texture + '</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="black-box"><h3>Estimated Age</h3><p>' + str(st.session_state.age) + ' years</p></div>', unsafe_allow_html=True)
    with col3:
        damage_level, _ = get_damage_assessment(st.session_state.damage)
        st.markdown('<div class="black-box"><h3>Skin Damage</h3><p>' + f"{st.session_state.damage}%" + '</p><small>' + damage_level + '</small></div>', unsafe_allow_html=True)
    
    # Display the pie chart (reduced size)
    st.subheader("Skin Composition Analysis")
    pimples, dead_skin, normal_skin = st.session_state.composition
    fig = create_skin_composition_chart(pimples, dead_skin, normal_skin)
    st.pyplot(fig)
    
    # Display interpretation of the pie chart
    with st.expander("🔍 What does this mean?"):
        st.write("""
        - **Pimples**: Shows the percentage of your skin affected by acne or blemishes
        - **Dead Skin**: Indicates areas with dry, flaky, or dull skin that needs exfoliation
        - **Normal Skin**: Represents healthy, well-balanced skin areas
        """)
        if pimples > 30:
            st.warning("Your skin has a significant amount of pimples. Consider using salicylic acid or benzoyl peroxide treatments.")
        if dead_skin > 20:
            st.warning("Your skin has considerable dead skin buildup. Gentle exfoliation 2-3 times weekly is recommended.")
    
    age_title, age_tips = get_age_recommendations(st.session_state.age)
    with st.expander(f"🔍 {age_title} Recommendations"):
        st.markdown(age_tips)
    
    st.subheader("Personalized Routine")
    
    # Add result summary at the top of the routine
    st.markdown(f"""
    <div class="result-box">
    <h4 style="color:#333;margin-top:0;">Based on your analysis:</h4>
    <ul style="margin-bottom:0;">
    <li>Your skin type is <b>{st.session_state.texture}</b></li>
    <li>Your skin shows <b>{damage_level.lower()}</b> ({st.session_state.damage}%)</li>
    <li>Your skin has {pimples}% pimples and {dead_skin}% dead skin</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    for product in get_skincare_suggestions(st.session_state.texture, st.session_state.age, st.session_state.damage):
        with st.container():
            st.markdown(f"**{product[0]}**")
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                st.markdown(f"*How to use:* {product[1]}")
            with col2:
                st.markdown(f"*Precautions:* {product[2]}")
            with col3:
                st.markdown(f"*Expected results:* {product[3]}")
            st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View Product Recommendations"):
            st.session_state.page = 'Product Recommendations'
    with col2:
        if st.button("View Home Remedies"):
            st.session_state.page = 'Home Remedies'

elif st.session_state.page == 'Product Recommendations':
    st.subheader("Recommended Products for You")
    
    products = get_product_recommendations(st.session_state.texture, st.session_state.age, st.session_state.damage)
    
    for category, items in products.items():
        st.markdown(f"### {category}")
        cols = st.columns(3)
        for i, (price, name, link) in enumerate(items):
            with cols[i % 3]:
                st.markdown(f"**{price}**  \n{name}  \n[Buy Now]({link})")
        st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Analysis"):
            st.session_state.page = 'Analysis Results'
    with col2:
        if st.button("View Home Remedies"):
            st.session_state.page = 'Home Remedies'

elif st.session_state.page == 'Home Remedies':
    st.subheader("Natural Home Remedies for Your Skin")
    
    st.write(f"These remedies are specially selected for {st.session_state.texture.lower()} skin:")
    
    remedies = get_home_remedies(st.session_state.texture, st.session_state.age, st.session_state.damage)
    
    for remedy in remedies:
        with st.expander(remedy[0]):
            st.markdown(f"**How to use:** {remedy[1]}")
            st.markdown(f"**Benefits:** {remedy[2]}")
        st.divider()
    
    if st.button("Back to Analysis"):
        st.session_state.page = 'Analysis Results'

# Custom CSS
st.markdown("""
<style>
div[data-testid="stExpander"] {
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)