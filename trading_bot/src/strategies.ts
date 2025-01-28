export class TradingStrategy {
    static simpleMovingAverage(prices: number[], period: number): number {
        const sum = prices.slice(-period).reduce((a, b) => a + b, 0);
        return sum / period;
    }
}
