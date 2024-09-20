function calcTimeDiff(timestamp) {
    const currentTimestamp = Math.floor(Date.now() / 1000); // Convert milliseconds to seconds
    const differenceInSeconds = currentTimestamp - timestamp;
    const differenceInMinutes = Math.floor(differenceInSeconds / 60);
    return differenceInMinutes;
}

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('[id^="time-diff-"]');
    elements.forEach(element => {
        const itemId = element.id.split('-')[2];
        const timestamp = parseInt(document.getElementById(`timestamp-${itemId}`).textContent, 10);
        const timeDiff = calcTimeDiff(timestamp);
        element.textContent = `${timeDiff} minutes ago`;
    });

});