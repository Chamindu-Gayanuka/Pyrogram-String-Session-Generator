import time
from pyrogram import Client
import asyncio

# This script generates a session string for a Telegram client using the Pyrogram library.
def progress_bar():
    for i in range(0, 101, 10):
        print(f"🔄 Generating string session... {i}% complete", end="\r")
        time.sleep(0.1)
    print("✅ Generating string session... 100% complete")

async def stringGenerate():
    api_id = int(input("Enter your API ID: "))
    api_hash = input("Enter your API Hash: ")
    client = Client("memory", api_id, api_hash)
    await client.connect()
    
    phone_number = input("Enter your phone number: ")
    print("Sending code to your telegram...")
    code = await client.send_code(phone_number)

    phone_code_msg = input("Enter the code you received: ")
    
    try:
        print('Login in Telegram...')
        await client.sign_in(phone_number, code.phone_code_hash, phone_code_msg)
    except:
        password = input('Insert your double factor:\n')
        await client.check_password(password=password)
    print("Session String: ")
    string_session = await client.export_session_string()

    # Show progress before launching client
    progress_bar()
    
    # Send to Telegram
    await client.send_message("me", f"✅ **Your Pyrogram String Session:**\n\n`{string_session}`")

    # Save to file
    with open("pyrogram_string_session.txt", "w") as f:
        f.write(string_session)

    print("\n✅ String session generated successfully.")
    print("📩 Sent to your Telegram 'Saved Messages'.")
    print("💾 Saved to 'pyrogram_string_session.txt'.")
    
if __name__ == "__main__":
    asyncio.run(stringGenerate())