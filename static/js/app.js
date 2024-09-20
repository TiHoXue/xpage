new Vue({
    el: '#app',
    data: {
        message: "人生朝露，且歌且行",
        currentTime: new Date()
    },
    computed: {
        formattedTime() {
            const now = this.currentTime;
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            const month = now.getMonth() + 1;
            const day = now.getDate();
            const year = now.getFullYear();

            return {
                time: `${hours}:${minutes}:${seconds}`,
                date: `${year}年${month}月${day}日`
            };
        }
    },
    mounted() {
        setInterval(() => {
            this.currentTime = new Date();
        }, 1000);
    }
});