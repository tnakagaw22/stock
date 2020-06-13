const getRecentPeak = (highPrices) => {
    let peakPrice = 0;

    for (const highPrice of highPrices) {
        if (peakPrice < highPrice) {
            peakPrice = highPrice;
        }
        else {
            break;
        }

    }
    return peakPrice;
}

module.exports = {
    getRecentPeak
}