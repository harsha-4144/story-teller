# Story Teller

A collection of short stories with AI-generated audio narration using [Sarvam AI's Bulbul v3 Text-to-Speech API](https://docs.sarvam.ai/).

## Features

- Text-to-Speech generation using Sarvam AI API
- Multiple voice options for storytelling
- Bilingual support (English, Telugu)

## Generated Audio Samples

### Example 1: The Clever Rabbit

**Voice:** Kavya (Female)  
**Language:** English

Once upon a time, in a dense forest, there lived a clever rabbit. One day, the rabbit was walking near a well. He heard a voice from the well. "Help me! Help me!" cried the voice. The rabbit looked down the well and saw a golden fish. "Please save me," said the fish. "If you save me, I will grant you a wish." The rabbit was clever. He thought for a moment and said, "I cannot swim. But if you can grant me a wish, jump out of the well yourself." The fish tried hard and jumped out of the well. The rabbit was happy. He had learned that day that cleverness is stronger than strength.

**Moral:** Cleverness is stronger than strength

---

**Listen:**

▶️ [Play The Clever Rabbit Audio](https://raw.githubusercontent.com/harsha-4144/story-teller/main/audio/story_1_the_clever_rabbit.wav)

▶️ [Play The Honest Woodcutter Audio](https://raw.githubusercontent.com/harsha-4144/story-teller/main/audio/story_2_the_honest_woodcutter.wav)

### Example 2: The Honest Woodcutter

**Voice:** Shubh (Male)  
**Language:** English

Long ago, there lived a poor woodcutter in a village. Every day, he went to the forest to cut wood and sell it. One day, his axe slipped from his hand and fell into the river. He sat on the bank and cried. A fairy appeared and asked, "Why are you crying, little boy?" "My axe fell into the river," said the woodcutter. The fairy dived into the water and brought out a golden axe. "Is this yours?" asked the fairy. "No," said the honest woodcutter. The fairy dived again and brought a silver axe. "Is this yours?" asked the fairy. "No," said the woodcutter again. Finally, she brought his own iron axe. "Yes, this is mine!" said the woodcutter happily. The fairy was pleased with his honesty and gave him both the golden and silver axes as rewards. And the woodcutter lived happily ever after.

**Moral:** Honesty is the best policy

---

**Listen:**

<audio controls>
  <source src="audio/story_2_the_honest_woodcutter.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

## Voice Options Tested

The following voices from Sarvam AI's Bulbul v3 model were tested:

### Male Voices
| Voice | Quality | Best For |
|-------|---------|----------|
| shubh | Good | General storytelling |
| aditya | Good | Narratives |
| rohan | Good | Stories |
| amit | Good | Casual stories |
| dev | Good | General use |

### Female Voices
| Voice | Quality | Best For |
|-------|---------|----------|
| kavya | Excellent | Children's stories |
| ishita | Good | Engaging narratives |
| shreya | Good | Expressive stories |
| ritu | Good | Pleasant tone |
| priya | Good | Clear narration |

**Recommendation:** For storytelling, `kavya` (female) and `shubh` (male) produce the most engaging results.

## Python Script

The `tts_script.py` can be used to generate audio for any text:

```bash
# Test different voices
python tts_script.py test

# Generate audio for stories
python tts_script.py generate
```

## Requirements

- Python 3.8+
- sarvamai package (`pip install sarvamai`)

## API

This project uses the [Sarvam AI Text-to-Speech API](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-to-speech/overview) with the Bulbul v3 model.
