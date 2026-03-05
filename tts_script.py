import base64
import os
from sarvamai import SarvamAI

STORIES = [
    {
        "title": "The Clever Rabbit",
        "text": """Once upon a time, in a dense forest, there lived a clever rabbit. 
One day, the rabbit was walking near a well. He heard a voice from the well. 
"Help me! Help me!" cried the voice. The rabbit looked down the well and saw a golden fish. 
"Please save me," said the fish. "If you save me, I will grant you a wish."
The rabbit was clever. He thought for a moment and said, "I cannot swim. But if you can grant me a wish, jump out of the well yourself." 
The fish tried hard and jumped out of the well. The rabbit was happy. He had learned that day that cleverness is stronger than strength.""",
        "voice": "kavya"
    },
    {
        "title": "The Honest Woodcutter",
        "text": """Long ago, there lived a poor woodcutter in a village. 
Every day, he went to the forest to cut wood and sell it. 
One day, his axe slipped from his hand and fell into the river. 
He sat on the bank and cried. A fairy appeared and asked, "Why are you crying, little boy?"
"My axe fell into the river," said the woodcutter. 
The fairy dived into the water and brought out a golden axe. 
"Is this yours?" asked the fairy. "No," said the honest woodcutter.
The fairy dived again and brought a silver axe. "Is this yours?" asked the fairy. 
"No," said the woodcutter again. Finally, she brought his own iron axe. 
"Yes, this is mine!" said the woodcutter happily. 
The fairy was pleased with his honesty and gave him both the golden and silver axes as rewards. 
And the woodcutter lived happily ever after.""",
        "voice": "shubh"
    },
    {
        "title": "Light's Path (Telugu)",
        "text": """ఒక ఊరిలో గోపి, గణేష్ ఇద్దరు బాలురు. 
ఇద్దరు చాలా మిత్రులు. 
ఒకరోజు, ఊరు బయట ఒక బాక్సు 
కనబట్టారు. లో బంగారు నాణెలు 
మెడలెజ్ ఉన్నాయి. 
"ఇది నాది!"అనాడు గోపి. 
"కాదు, నాది!"అనాడు గణేష్. 
ఇద్దరు గబుగబుగా 
తగాదాకు దిగారు. 
అక్కఅకు ఒక వృద్ధురాలు 
రావడం చూశారు. 
"బాబులారా, ఏం జరిగింది?" 
అని ఆమె ఆశ్చర్యురాలై 
అడిగింది. 
"ఈ బాక్సు ఎవరిదో 
తెలియదు. ఇద్దం హక్కు 
కాబట్టాము"అన్నారు. 
"తిరిగి ఇచ్చే 
ఆలోచన లేదు?" 
అని ఆ వృద్ధురాలు 
తబ్బిలాడుతుంది. 
బాలురు బళ్ళఁ 
తల ఎత్తలేదు. 
బాగ్కారం, నిజాయతీ — 
ఇదే జీవితం""",
        "voice": "shubh",
        "language": "te-IN"
    }
]

VOICES = {
    "male": ["shubh", "aditya", "rahul", "rohan", "amit", "dev", "varun"],
    "female": ["ritu", "priya", "neha", "pooja", "simran", "kavya", "ishita", "shreya", "roopa"]
}

API_KEY = "sk_fptuc6sq_bn1jxyNekKHqno23EcaGgn3C"

def generate_audio(text, voice="shubh", language="en-IN", pace=0.9):
    """Generate audio for given text using Sarvam TTS."""
    client = SarvamAI(api_subscription_key=API_KEY)
    
    try:
        response = client.text_to_speech.convert(
            text=text,
            model="bulbul:v3",
            speaker=voice,
            target_language_code=language,
            pace=pace,
            speech_sample_rate=24000
        )
        
        audio_base64 = "".join(response.audios)
        audio_bytes = base64.b64decode(audio_base64)
        return audio_bytes
    except Exception as e:
        print(f"Error generating audio with voice {voice}: {e}")
        return None

def test_voices():
    """Test different voices with sample text."""
    sample_text = "Once upon a time, in a faraway land, there lived a brave little rabbit."
    
    print("Testing male voices...")
    for voice in VOICES["male"]:
        print(f"Testing {voice}...")
        audio = generate_audio(sample_text, voice=voice, pace=0.9)
        if audio:
            filename = f"audio/test_{voice}.wav"
            os.makedirs("audio", exist_ok=True)
            with open(filename, "wb") as f:
                f.write(audio)
            print(f"  Saved: {filename}")
    
    print("\nTesting female voices...")
    for voice in VOICES["female"]:
        print(f"Testing {voice}...")
        audio = generate_audio(sample_text, voice=voice, pace=0.9)
        if audio:
            filename = f"audio/test_{voice}.wav"
            with open(filename, "wb") as f:
                f.write(audio)
            print(f"  Saved: {filename}")

def generate_story_audio():
    """Generate audio for all stories."""
    os.makedirs("audio", exist_ok=True)
    
    for i, story in enumerate(STORIES, 1):
        title = story["title"].lower().replace(" ", "_")
        filename = f"audio/story_{i}_{title}.wav"
        
        voice = story.get("voice", "shubh")
        language = story.get("language", "en-IN")
        
        print(f"Generating audio for: {story['title']} (voice: {voice}, lang: {language})")
        audio = generate_audio(story["text"], voice=voice, language=language, pace=0.9)
        
        if audio:
            with open(filename, "wb") as f:
                f.write(audio)
            print(f"  Saved: {filename}")
        else:
            print(f"  Failed to generate audio for {story['title']}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            test_voices()
        elif sys.argv[1] == "generate":
            generate_story_audio()
    else:
        print("Usage: python tts_script.py [test|generate]")
        print("  test     - Test different voices")
        print("  generate - Generate audio for stories")
