new Vue({
    el: '#app',
    data: {
        message: "xueth's homepage",
        currentTime: new Date()
    },
    computed: {
        formattedTime() {
            const now = this.currentTime;
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            const monthNames = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ];
            const month = monthNames[now.getMonth()];
            const day = now.getDate();
            const year = now.getFullYear();

            return {
                time: `${hours}:${minutes}:${seconds}`,
                date: `${month} ${day}, ${year}`
            };
        }
    },
    mounted() {
        setInterval(() => {
            this.currentTime = new Date();
        }, 1000);
    }
});