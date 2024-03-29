name = input(str("Filename: ")) + ".html"

html = open(name, 'w')

style = """
<style>
:root {
    --grey: #30363d;
    --red: #7d0000;
    --lightgray: #58a6f0;
    --font: #c9d1d9;
    --background: #0d1117;
}

html {
    background-color: var(--background);
    overflow: hidden;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

h1 {
    text-align: center;
}

.mainbox{
    width: 500px;
    height: 900px;
    border: 3px solid var(--grey);
    border-radius: 30px;
    float: left;
    margin-right: 20px;
}

.leftbox {
    width: 100px;
    height: 900px;
    border-right: 3px solid var(--grey);
    border-top: 3px solid var(--grey);
    border-bottom: 3px solid var(--grey);
    border-radius: 0 30px 30px 0;
    margin-right: 20px;
    float: left;
}

.rightbox {
    width: 100px;
    height: 900px;
    border-left: 3px solid var(--grey);
    border-top: 3px solid var(--grey);
    border-bottom: 3px solid var(--grey);
    border-radius: 30px 0 0 30px;
    float: left;
}

.topleftbox {
    width: 100px;
    height: 50px;
    margin-right: 20px;
    float: left;
}

.toprightbox {
    width: 100px;
    height: 50px;
    float: left;
}

.topmainbox {
    width: 500px;
    height: 50px;
    border-left: 3px solid var(--grey);
    border-right: 3px solid var(--grey);
    border-bottom: 3px solid var(--grey);
    border-radius: 0 0 30px 30px;
    float: left;
    margin-right: 20px;
    margin-bottom: 20px;
}

.bottommainbox {
    width: 500px;
    height: 50px;
    border-left: 3px solid var(--grey);
    border-right: 3px solid var(--grey);
    border-top: 3px solid var(--grey);
    border-radius: 30px 30px 0 0;
    float: left;
    margin-right: 20px;
    margin-top: 20px;
}

.option1, .option2 {
    width: 450px;
    height: 100px;
    border: 2px solid var(--grey);
    border-radius: 30px;
    margin-bottom: 20px;
}

.force {
    width: 350px;
    padding: 10px 0 10px 0;
    border: 1px solid var(--red);
    border-radius: 30px;
    margin-bottom: 20px;
    position: relative;
}

.force:first-child {
    margin-top: 87px;
}

.forceleft{
    width: 50%;
    height: 50%;
    position: absolute;
}

.forceright{
    width: 50%;
    height: 50%;
    position: absolute;
    margin-left: 175px;
}

.progressbar {
    position: absolute;
    left: 50%;
    top: 4%;
    transform: translate(-50%, -50%);
}

.progress1, .progress2, .progress3, .progress4, .progress5, .progress6 {
    width: 50px;
    height: 2px;
    border: 1px solid var(--grey);
    border-radius: 10px;
    background-color: var(--grey);
    float: left;
    margin-right: 10px;
}

.progress1 {
    border-color: var(--lightgray);
    background-color: var(--lightgray);
}

.text {
    margin-left: 40px;
    margin-right: 40px;
}

h2 {
    margin: 7.8% auto;
    color: var(--lightgray);
    font-family: 'Open Sans', sans-serif;
}

h1 {
    color: var(--lightgray);
    font-family: 'Open Sans', sans-serif;
}

a, p, div {
    text-decoration: none;
    color: var(--font);
    font-family: 'Open Sans', sans-serif;
}


.content, .content2 {
    margin: 0 50px 0 50px;
    font-size: 20px;
}

.content img{
    width: 100%;
    margin-top: 4%
}

.content .css {
    width: 50%;
}

#window {
    position: absolute;
    top:  50%;
    left: 50%;
    transform: translate(-50%,-50%);
    border: 2px solid var(--grey);
    border-radius: 10px;
}

@media screen and (max-height: 1080px) {
    .mainbox{
        width: 500px;
        height: 800px;
        border: 3px solid var(--grey);
        border-radius: 30px;

        float: left;
        margin-right: 20px;
    }
    
    .leftbox {
        width: 100px;
        height: 800px;
        border-right: 3px solid var(--grey);
        border-top: 3px solid var(--grey);
        border-bottom: 3px solid var(--grey);
        border-radius: 0 30px 30px 0;
        margin-right: 20px;
        float: left;
    }
    
    .rightbox {
        width: 100px;
        height: 800px;
        border-left: 3px solid var(--grey);
        border-top: 3px solid var(--grey);
        border-bottom: 3px solid var(--grey);
        border-radius: 30px 0 0 30px;

        float: left;
    }

    .content .css {
        width: 35%;
    }
}
</style>"""

forceoptions = """
                            <div class="force" id="force1"><div class="forceleft" onclick="falseforce1()"></div>"""

force1 = """

                    <div class="mainbox" id="display3" style="display: none;">
                        <h1>Node.js</h1>
                        <div class="text">
                            <p>Node.js is an open-source, cross-platform, back-end JavaScript runtime environment
                                that runs on the V8 engine and executes JavaScript code outside a web browser.
                                Node.js lets developers use JavaScript to write command line tools and for
                                server-side scripting—running scripts server-side to produce dynamic web
                                page content before the page is sent to the user's web browser. Consequently,
                                Node.js represents a "JavaScript everywhere" paradigm, unifying web-application
                                development around a single programming language, rather than different languages
                                for server-side and client-side scripts.
                            </p>
                        </div>
                        <center>"""
force2 = """
                        </center>
                    </div>
"""

textonly = """

                    <div class="mainbox" id="display1">
                        <h1>Simple HTML Code</h1>
                        <div class="content">
                            <p>HYPER-TEXT MARKUP LANGUAGE
                                Is the standardised markup language (a subset of XML) that 
                                defines the layout of a webpage. 
                                HTML has no functional properties, other languages such as 
                                JavaScript must be used in order to manipulate the layout
                                and perform HTTP requests.
                                CSS (Cascading Style Sheets) is commonly used to style the
                                elements in the layout. </p>
                        </div>
                    </div>"""


part1 = """<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="style.css">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">
        <link rel="shortcut icon" type="image/x-icon" href="../img/favicon.ico">
        
        <title>Document</title>

    </head>
    <body>"""

part2 = """
        <div id="window">
            <div id="wrapper">
                <div>
                    <center>
                        <div class="progressbar">
                            <div class="progress1" id="progress1"></div>
                            <div class="progress2" id="progress2"></div>
                            <div class="progress3" id="progress3"></div>
                            <div class="progress4" id="progress4"></div>
                            <div class="progress5" id="progress5"></div>
                            <div class="progress6" id="progress6"></div>
                        </div>
                    </center>
                    <div class="topleftbox"></div>

                    <div class="topmainbox" style="border-color: #0d1117"></div>

                    <div class="toprightbox"></div>
                </div>
                <div>
                    <div class="leftbox" style="border-color: #0d1117" id="left" onclick="left()"></div>"""
                    
part3 = """

                    <div class="rightbox" onclick="right()" id="right"></div>
                </div>
                <div>
                    <div class="topleftbox"></div>

                    <div class="bottommainbox" style="border-left: 3px solid #0d1117;border-right: 3px solid #0d1117;border-top: 3px solid #0d1117;"></div>

                    <div class="toprightbox"></div>
                </div>
            </div>
        </div>
    <script src="script.js"></script>
    </body>
</html>"""

html.write(part1 + style + part2 + textonly + force1 + forceoptions*4 + force2 + part3)
html.close()