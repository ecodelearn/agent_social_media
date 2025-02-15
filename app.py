# app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from util.message import Message
from util.send_sandeco import SendSandeco
from image_decode_save import ImageDecodeSaver

from instagram_send import InstagramSend
from paths import Paths


from flask import Flask, request

app = Flask(__name__)


border_image = os.path.join(Paths.ROOT_DIR,"instagram","moldura.png")


@app.route("/messages-upsert", methods=['POST'])
def webhook():
    
    data = request.get_json()  
    
    print(data)
            
    msg = Message(data)
    texto = msg.get_text()
    
    send = SendSandeco()

    if msg.scope == Message.SCOPE_GROUP:    
        
        print(f"Grupo: {msg.group_id}")
        
        if str(msg.group_id) == "120363372879654391":
             
            if msg.message_type == msg.TYPE_IMAGE:
                
                image_path = ImageDecodeSaver.process(msg.image_base64)
                
                InstagramSend.send_instagram(image_path, texto)
                
            
    return "" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

