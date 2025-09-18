from flask import Flask, jsonify
from flask_cors import CORS

# Flask एप्लिकेशन को शुरू करें।
app = Flask(__name__)
CORS(app)  # यह आपके फ्रंटएंड को बैकएंड से जुड़ने देता है।

# --- डेटाबेस का सिमुलेशन (असली डेटाबेस के बजाय) ---
# दैनिक राशिफल का डेटा
daily_horoscopes = {
    "मेष": "आपका दिन ऊर्जा से भरा रहेगा।",
    "वृष": "आर्थिक मामलों में सावधानी बरतें।",
    "मिथुन": "संचार के माध्यम से आपको लाभ होगा।",
    "कर्क": "भावनात्मक रूप से आप बहुत संवेदनशील रहेंगे।",
    "सिंह": "नेतृत्व करने का अवसर मिलेगा।",
    "कन्या": "अपनी सेहत का ध्यान रखें।",
    "तुला": "रिश्तों में संतुलन बनाए रखें।",
    "वृश्चिक": "गूढ़ विषयों में आपकी रुचि बढ़ेगी।",
    "धनु": "यात्रा का योग बन रहा है।",
    "मकर": "कार्यक्षेत्र में आपको अधिक मेहनत करनी पड़ सकती है।",
    "कुंभ": "नए विचार और नवाचार आपके मन में आएंगे।",
    "मीन": "अपने अंतर्ज्ञान पर भरोसा करें।"
}

# पंचांग का डेटा
panchang_data = {
    "tithi": "चतुर्थी",
    "vaar": "गुरुवार"
}

# अन्य जानकारी का डेटा
features_data = {
    "muhurt": "लाभ मुहूर्त: 10:45 AM - 12:15 PM",
    "vivah_yog": "ज्योतिष में विवाह का समय 7वें भाव और उसके स्वामी से देखा जाता है।",
    "hastrekha": "आपके हाथ की रेखाओं का अध्ययन करके भविष्य बताया जाता है।",
    "astrologer_role": [
        "कुंडली विश्लेषण",
        "समस्याओं के लिए ज्योतिषीय उपाय",
        "शुभ मुहूर्त परामर्श"
    ]
}

# --- एपीआई रूट्स (APIs) ---

@app.route('/api/panchang', methods=['GET'])
def get_panchang():
    """पंचांग डेटा प्रदान करता है।"""
    return jsonify(panchang_data)

@app.route('/api/horoscope/<rasi>', methods=['GET'])
def get_horoscope(rasi):
    """एक राशि के लिए दैनिक राशिफल प्रदान करता है।"""
    horoscope = daily_horoscopes.get(rasi, "राशिफल उपलब्ध नहीं है।")
    return jsonify({"rasi": rasi, "horoscope": horoscope})

@app.route('/api/kundli_milan', methods=['GET'])
def get_kundli_milan():
    """कुंडली मिलान का एक नकली स्कोर प्रदान करता है।"""
    import random
    score = random.randint(15, 36)
    return jsonify({"score": score})

@app.route('/api/features', methods=['GET'])
def get_features():
    """अन्य सभी ज्योतिषीय सुविधाओं का डेटा प्रदान करता है।"""
    return jsonify(features_data)

# एप्लिकेशन को चलाएं
if __name__ == '__main__':
    app.run(debug=True)
