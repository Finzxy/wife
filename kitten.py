from kittenml import KittenTTS
from optimization import use_optimization

use_optimization() #remove or comment this function if you feel laggy
model = KittenTTS("KittenML/kitten-tts-mini-0.8")
def speaking(text):
    audio = model.generate(text, voice="Rosie", speed=1)
    # model.generate("This high-quality TTS model runs without a GPU.", voice="Rosie")
    # # Adjust speech speed (default: 1.0)
    # model.generate("Hello, world.", voice="Rosie", speed=1.2)
    # Save directly to a file
    # model.generate_to_file("Hello, world.", "output.mp3", voice="Rosie", speed=1.2)

    # List available voices
    print(model.available_voices)
    # ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']

    import soundfile as sf
    sf.write("output.mp3", audio, 24000)
