from flask import Flask, render_template_string, request, jsonify
import requests
import re

app = Flask(__name__)

# ---------------- DASHBOARD (WALEED) ----------------
HTML_DASHBOARD = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WALEED LEGEND P3N4L </title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{background:radial-gradient(circle at 20% 30%, #0a0a2e, #000000);display:flex;flex-direction:column;align-items:center;min-height:100vh;padding:2rem;color:#fff;font-family:'Orbitron',sans-serif;}
header{text-align:center;margin-bottom:2rem;}
header h1{font-size:3rem;font-weight:700;background:linear-gradient(135deg,#ff6b6b,#ffd93d,#6bcb77,#4d96ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:0 0 30px rgba(255,107,107,0.3);letter-spacing:3px;animation:glowPulse 2s ease-in-out infinite;}
@keyframes glowPulse{0%{filter:drop-shadow(0 0 5px #ff6b6b);}50%{filter:drop-shadow(0 0 20px #ffd93d);}100%{filter:drop-shadow(0 0 5px #4d96ff);}}
.container{display:flex;flex-wrap:wrap;gap:2rem;justify-content:center;width:100%;max-width:1300px;}
.card{position:relative;width:360px;height:460px;border-radius:24px;overflow:hidden;background:#111;cursor:pointer;box-shadow:0 0 30px rgba(255,0,100,0.2);transition:transform 0.4s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.4s ease;}
.card:hover{transform:scale(1.05) translateY(-10px);box-shadow:0 0 50px rgba(255,0,150,0.5);}
.card video{width:100%;height:100%;object-fit:cover;filter:brightness(0.8) saturate(1.2);}
.overlay{position:absolute;bottom:-100%;left:0;width:100%;height:100%;background:linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(255,0,100,0.3) 100%);display:flex;flex-direction:column;justify-content:flex-end;padding:25px;opacity:0;transition:all 0.5s cubic-bezier(0.23,1,0.32,1);backdrop-filter:blur(4px);z-index:2;}
.card.active .overlay{bottom:0;opacity:1;}
.overlay h3{font-size:26px;margin-bottom:8px;text-shadow:0 0 20px #ff0066,0 0 40px rgba(255,0,100,0.5);color:#fff;letter-spacing:1px;animation:slideUp 0.5s ease forwards;}
.overlay p{font-size:14px;color:#f0f0f0;margin-bottom:15px;opacity:0;animation:fadeIn 0.6s ease forwards;animation-delay:0.2s;}
.open-btn{align-self:center;background:linear-gradient(135deg,#ff0040,#ff1a66);border:none;padding:12px 30px;border-radius:40px;font-size:15px;color:white;cursor:pointer;font-weight:700;box-shadow:0 0 20px rgba(255,0,0,0.6);transition:all 0.3s ease;opacity:0;animation:fadeIn 0.6s ease forwards;animation-delay:0.4s;}
.open-btn:hover{transform:scale(1.1) rotate(2deg);box-shadow:0 0 40px rgba(255,0,100,1);}
@keyframes slideUp{from{transform:translateY(40px);opacity:0;}to{transform:translateY(0);opacity:1;}}
@keyframes fadeIn{from{opacity:0;}to{opacity:1;}}
footer{margin-top:3rem;font-size:1rem;color:#888;text-align:center;border-top:1px solid rgba(255,255,255,0.05);padding-top:1.5rem;width:80%;}
footer span{background:linear-gradient(135deg,#ff6b6b,#ffd93d);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:700;}
</style>
</head>
<body>
<header><h1>⚡ ALL PAID S3V3R WALEED XD </h1></header>
<div class="container">

<!-- Card 1 -->
<div class="card" onclick="toggleOverlay(this)">
  <video autoplay muted loop playsinline>
    <source src="https://raw.githubusercontent.com/serverxdt/Approval/main/223.mp4" type="video/mp4">
  </video>
  <div class="overlay">
    <h3>Convo 3.0</h3>
    <p>Nonstop Pro Whatsapp server by waleed xd </p>
    <button class="open-btn" onclick="event.stopPropagation(); window.open('http://fi8.bot-hosting.net:20615//','_blank')">OPEN</button>
  </div>
</div>

<!-- Card 2 -->
<div class="card" onclick="toggleOverlay(this)">
  <video autoplay muted loop playsinline>
    <source src="https://raw.githubusercontent.com/serverxdt/Approval/main/Anime.mp4" type="video/mp4">
  </video>
  <div class="overlay">
    <h3>Post 3.0</h3>
    <p>T3L3GRAM NONSTOP SERVER BY WALEED KHAN Stop/Resume/Pause</p>
    <button class="open-btn" onclick="event.stopPropagation(); window.open('https://waleedin.onrender.com/','_blank')">OPEN</button>
  </div>
</div>

<!-- Card 3 -->
<div class="card" onclick="toggleOverlay(this)">
  <video autoplay muted loop playsinline>
    <source src="https://raw.githubusercontent.com/serverxdt/Approval/main/GOKU%20_%20DRAGON%20BALZZ%20_%20anime%20dragonballz%20dragonballsuper%20goku%20animeedit%20animetiktok.mp4" type="video/mp4">
  </video>
  <div class="overlay">
    <h3>Token Checker 3.0</h3>
    <p>Token Geneter tool+ GC UID Extractor Bot</p>
    <button class="open-btn" onclick="event.stopPropagation(); window.open('https://tooken2026.onrender.com','_blank')">OPEN</button>
  </div>
</div>

<!-- Card 4 -->
<div class="card" onclick="toggleOverlay(this)">
  <video autoplay muted loop playsinline>
    <source src="https://raw.githubusercontent.com/serverxdt/Approval/main/SOLO%20LEVELING.mp4" type="video/mp4">
  </video>
  <div class="overlay">
    <h3>Post UID 2.0</h3>
    <p>Enter Your Post Link & Extract Post UID Easily</p>
    <button class="open-btn" onclick="event.stopPropagation(); window.open('/post_uid','_blank')">OPEN</button>
  </div>
</div>

</div>
<footer>Created by <span>WALEED</span> • 2026</footer>
<script>
function toggleOverlay(card){card.classList.toggle('active');}
</script>
</body>
</html>
"""

# ---------------- TOKEN CHECKER PAGE (WALEED) ----------------
TOKEN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>2025 GC UID Finder • WALEED</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Orbitron',sans-serif;background:radial-gradient(circle at top,#0f0c29,#302b63,#24243e);color:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;padding:20px;}
.glass-container{background:rgba(255,255,255,0.07);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.15);border-radius:32px;padding:30px;width:100%;max-width:440px;text-align:center;box-shadow:0 0 60px rgba(100,0,255,0.3);animation:float 6s ease-in-out infinite;}
@keyframes float{0%{transform:translateY(0px);}50%{transform:translateY(-10px);}100%{transform:translateY(0px);}}
h1{margin-bottom:8px;font-size:24px;background:linear-gradient(135deg,#f093fb,#f5576c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:0 0 20px rgba(245,87,108,0.4);}
.sub{font-size:13px;color:#aaa;margin-bottom:18px;}
input{width:95%;padding:14px;border-radius:20px;border:1px solid rgba(255,255,255,0.2);outline:none;margin-bottom:15px;font-size:14px;text-align:center;background:rgba(255,255,255,0.05);color:#fff;transition:0.3s;box-shadow:inset 0 0 10px rgba(255,0,255,0.1);}
input:focus{border-color:#f5576c;box-shadow:0 0 20px rgba(245,87,108,0.5);}
input::placeholder{color:#999;}
.btn{display:block;width:100%;background:linear-gradient(135deg,#f093fb,#f5576c);color:white;border:none;border-radius:30px;padding:14px;font-size:15px;margin:8px 0;cursor:pointer;font-weight:700;box-shadow:0 0 20px rgba(245,87,108,0.4);transition:transform 0.2s,box-shadow 0.3s;}
.btn:hover{transform:scale(1.02);box-shadow:0 0 40px rgba(245,87,108,0.8);}
.result-box{background:rgba(0,0,0,0.4);border-radius:20px;padding:15px;margin-top:15px;text-align:left;border:1px solid rgba(255,255,255,0.05);backdrop-filter:blur(4px);}
.copy-btn{background:linear-gradient(135deg,#4facfe,#00f2fe);color:white;border:none;border-radius:20px;padding:6px 16px;cursor:pointer;font-size:12px;transition:0.3s;margin-top:5px;}
.copy-btn:hover{transform:scale(1.05);box-shadow:0 0 15px #00f2fe;}
.spinner{margin:15px auto;border:4px solid rgba(255,255,255,0.1);border-top:4px solid #f5576c;border-radius:50%;width:40px;height:40px;animation:spin 0.8s linear infinite;}
@keyframes spin{100%{transform:rotate(360deg);}}
.footer{margin-top:20px;font-size:12px;color:#666;}
.footer span{background:linear-gradient(135deg,#f093fb,#f5576c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
</style>
</head>
<body>
<div class="glass-container">
<h1>⚡ GC UID Finder</h1>
<p class="sub">by <span style="color:#f5576c;">WALEED</span> • 2025</p>
<input type="text" id="token" placeholder="Paste Your Facebook Token"/>
<button class="btn" onclick="fetchTokenInfo()">🔑 Check Token</button>
<button class="btn" onclick="fetchGcUids()">💬 Find GC UID</button>
<div id="loading" class="spinner" style="display:none;"></div>
<div id="tokenResult" class="result-box"></div>
<div id="gcResult" class="result-box"></div>
<div class="footer">Powered by <span>WALEED</span></div>
</div>
<script>
function fetchTokenInfo(){
  const token=document.getElementById("token").value.trim();
  if(!token)return alert("Please enter a token!");
  toggleLoading(true);
  fetch("/token_info",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:"token="+encodeURIComponent(token)})
  .then(res=>res.json())
  .then(data=>{
    toggleLoading(false);
    const result=document.getElementById("tokenResult");
    result.innerHTML=data.error?`<p style="color:#ff6b6b;">❌ ${data.error}</p>`:`<p><b>✅ Name:</b> ${data.name}</p><p><b>ID:</b> ${data.id}</p><p><b>DOB:</b> ${data.dob}</p><p><b>Email:</b> ${data.email}</p>`;
  });
}
function fetchGcUids(){
  const token=document.getElementById("token").value.trim();
  if(!token)return alert("Please enter a token!");
  toggleLoading(true);
  fetch("/gc_uid",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:"token="+encodeURIComponent(token)})
  .then(res=>res.json())
  .then(data=>{
    toggleLoading(false);
    const result=document.getElementById("gcResult");
    result.innerHTML="<h3 style='margin-bottom:8px;'>Messenger Group Chats</h3>";
    if(data.error){result.innerHTML+=`<p style="color:#ff6b6b;">❌ ${data.error}</p>`;}else{
      data.gc_data.forEach((gc,i)=>{
        result.innerHTML+=`<div style="margin-top:12px;border-bottom:1px solid rgba(255,255,255,0.08);padding-bottom:8px;">
<p><b>GC ${i+1}:</b> ${gc.gc_name}</p>
<p><b>UID:</b> ${gc.gc_uid}</p>
<button class='copy-btn' onclick="navigator.clipboard.writeText('${gc.gc_uid}').then(()=>alert('✅ UID copied!'))">📋 Copy UID</button>
</div>`;
      });
    }
  });
}
function toggleLoading(show){document.getElementById("loading").style.display=show?"block":"none";}
</script>
</body>
</html>
"""

# ---------------- POST UID FINDER (WALEED) ----------------
POST_UID_HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Post UID Extractor • WALEED</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Segoe UI',sans-serif;background:radial-gradient(circle at 30% 20%, #0f0c29, #302b63, #24243e);display:flex;justify-content:center;align-items:center;flex-direction:column;min-height:100vh;color:white;padding:20px;}
.glass-box{width:100%;max-width:400px;background:rgba(255,255,255,0.06);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.1);border-radius:32px;padding:30px;text-align:center;box-shadow:0 0 60px rgba(0,200,255,0.15);}
img{width:100%;border-radius:24px;margin-bottom:20px;box-shadow:0 0 30px rgba(0,200,255,0.2);}
h2{font-size:24px;background:linear-gradient(135deg,#4facfe,#00f2fe);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:15px;}
input[type=text]{width:95%;padding:14px;margin:15px 0;border:none;border-radius:30px;font-size:16px;background:rgba(255,255,255,0.1);color:white;outline:1px solid rgba(255,255,255,0.2);transition:0.3s;text-align:center;}
input[type=text]:focus{outline:2px solid #00f2fe;box-shadow:0 0 20px rgba(0,242,254,0.3);}
input::placeholder{color:#aaa;}
button{padding:14px 30px;border:none;border-radius:40px;background:linear-gradient(135deg,#4facfe,#00f2fe);color:white;font-size:16px;font-weight:700;cursor:pointer;box-shadow:0 0 20px rgba(0,242,254,0.3);transition:transform 0.2s,box-shadow 0.3s;}
button:hover{transform:scale(1.04);box-shadow:0 0 40px rgba(0,242,254,0.6);}
.result{margin-top:20px;padding:15px;background:rgba(0,0,0,0.3);border-radius:20px;font-weight:bold;color:#00f2fe;word-break:break-all;}
.footer{margin-top:25px;font-size:14px;color:#888;}
.footer span{background:linear-gradient(135deg,#4facfe,#00f2fe);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
</style>
</head>
<body>
<div class="glass-box">
<img src="https://i.imgur.com/iJ8mZjV.jpeg" alt="banner">
<h2>Post UID Finder</h2>
<form method="POST">
<input type="text" name="fb_url" placeholder="Enter FB post URL" required>
<button type="submit">🔍 Find UID</button>
</form>
{% if uid %}
<div class="result">📌 Post UID: {{ uid }}</div>
{% endif %}
<div class="footer">Developed by <span>WALEED</span> • 2.0</div>
</div>
</body>
</html>
"""

# ---------------- UTILITY FUNCTIONS ----------------
TOKEN_INFO_URL = "https://graph.facebook.com/v17.0/me?fields=id,name,birthday,email"
GC_UID_URL = "https://graph.facebook.com/v17.0/me/conversations?fields=id,name"

def check_token(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(TOKEN_INFO_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "status": "Valid",
            "name": data.get("name", "N/A"),
            "id": data.get("id", "N/A"),
            "dob": data.get("birthday", "N/A"),
            "email": data.get("email", "N/A")
        }
    return {"status": "Invalid"}

def get_gc_details(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(GC_UID_URL, headers=headers)
    if response.status_code == 200:
        gc_data = response.json().get("data", [])
        gc_list = []
        for gc in gc_data:
            raw_id = gc.get("id", "N/A")
            clean_id = raw_id.replace("t_", "").replace("t", "") if raw_id else "N/A"
            gc_list.append({"gc_name": gc.get("name", "Unknown"), "gc_uid": clean_id})
        return gc_list
    return None

# ---------------- ROUTES ----------------
@app.route("/token")
def token_page():
    return render_template_string(TOKEN_HTML)

@app.route("/token_info", methods=["POST"])
def token_info():
    token = request.form.get("token", "").strip()
    if not token:
        return jsonify({"error": "Token is required!"})
    info = check_token(token)
    if info["status"] == "Invalid":
        return jsonify({"error": "Invalid or expired token!"})
    return jsonify(info)

@app.route("/gc_uid", methods=["POST"])
def gc_uid():
    token = request.form.get("token", "").strip()
    if not token:
        return jsonify({"error": "Token is required!"})
    data = get_gc_details(token)
    if data is None:
        return jsonify({"error": "Failed to fetch GC UIDs!"})
    return jsonify({"gc_data": data})

@app.route("/post_uid", methods=["GET", "POST"])
def post_uid():
    uid = None
    if request.method == "POST":
        fb_url = request.form.get("fb_url", "").strip()
        if fb_url:
            try:
                resp = requests.get(fb_url, timeout=10)
                text = resp.text
                patterns = [r"/posts/(\d+)", r"story_fbid=(\d+)", r"facebook.com.*?/photos/\d+/(\d+)"]
                for pat in patterns:
                    match = re.search(pat, text)
                    if match:
                        uid = match.group(1)
                        break
                if not uid:
                    uid = "Not found"
            except Exception as e:
                uid = f"Error: {e}"
        else:
            uid = "Please provide a valid URL"
    return render_template_string(POST_UID_HTML, uid=uid)

@app.route("/")
def home():
    return render_template_string(HTML_DASHBOARD)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)