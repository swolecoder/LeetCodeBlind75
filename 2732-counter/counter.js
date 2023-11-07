/**
 * @param {number} n
 * @return {Function} counter
 */
const  createCounter = (n) => {
    let d = n
    return () => {
        return d++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */