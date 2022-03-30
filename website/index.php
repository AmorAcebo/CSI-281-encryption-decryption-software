<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="/css/style.css">
        <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">	
        <link href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" rel="stylesheet">
    </head>
    <body>
        <script type="text/javascript" src="/website/js/page_header.js"></script>
        <?php include("sidebar.php") ?>
        <?php include("page_header.php") ?>
        <div id="page-container">
            <h1 class="page-content-title"> Encrypt Your File</h1>
            <div id="text-box-wrapper">
                <p name="plainTextInput" id="plainTextInput">
                <div id="userInput"></div>
            </div>
            <button class="button" id="submit-button"type="button" onclick="encryptSubmit()"><i class="fas fa-user-secret"></i> Encrypt </button>
            <div id="display">
                <p class="flow-text" id="display-result"> </p>
            </div>
        </div>
        <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
        <script type="text/javascript">
            
            var toolbarOptions = [
				['bold', 'italic', 'underline', 'strike'],        // toggled buttons

				[{ 'list': 'ordered'}, { 'list': 'bullet' }],
				[{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
				[{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent

				[{ header: [1, 2, false] }],               		  // custom button values
				[{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
				[{ 'font': [] }],

				['link', 'image', 'code-block'],
				];

            var userInput = new Quill("#userInput", {  modules: {
					toolbar: toolbarOptions
				},
				placeholder: "Data to be encrypted goes here...",
				theme: "snow" 
			});

            // var form = document.querySelector('form');
            // form.onsubmit = function() {
            //     // Populate hidden form on submit
            function encryptSubmit() {
                var hiddenBox = document.querySelector('p[name=plainTextInput]');
                hiddenBox.value = JSON.stringify(userInput.getContents());
                document.getElementById("display-result").innerHTML = hiddenBox.value;
            }
        </script>
    </body>
</html>
