CSS = """

body{

background:linear-gradient(135deg,#4F46E5,#2563EB,#06B6D4);

background-size:400% 400%;

animation:bg 12s infinite ease;

font-family:Inter,sans-serif;

}

@keyframes bg{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

.glass{

background:rgba(255,255,255,.15);

backdrop-filter:blur(20px);

border-radius:25px;

border:1px solid rgba(255,255,255,.25);

box-shadow:0 20px 40px rgba(0,0,0,.2);

}

"""