const { getRecentPeak } = require("./peak.js");

const stockSymbol = "AAPL";

const mostRecentPeak = 280; // get it from dynamo
const todayHigh = 279; // get it from api
// r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=')

const currentOptionPrice ;
// https://iexcloud.io/docs/api/

const highPrices = [298, 3349.2, 2349];

const peak = getRecentPeak(highPrices);

console.log(peak);
