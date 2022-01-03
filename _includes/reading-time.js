<script>
    function readingTime() {
        const text = document.getElementById("article").innerText;
        const wpm = 200;
        const words = text.trim().split(/\s+/).length;
        const time = Math.ceil(words / wpm);
        const textToAdd = time <= 1 ? `${time} minute` : `${time} minutes`;
        document.getElementById("reading-time").innerText = textToAdd;
    }
    readingTime();
</script>
