from elevenlabs import set_api_key, voices

set_api_key("sk_11751a3d953f56c786cacc4c0c3deb3b47dae7877fbb1ddd")

for voice in voices():
    print(f"{voice.name} — ID: {voice.voice_id}")
