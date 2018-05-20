addEventListener("DOMContentLoaded", () => {
    document.getElementById("sentFile").onchange = function() {
        document.getElementById("formUpload").submit();
    };
})