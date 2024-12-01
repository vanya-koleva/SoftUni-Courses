function solve(percent) {
    const loadingBar = percent => `[${'%'.repeat(percent / 10)}${'.'.repeat(10 - percent / 10)}]`;
    const renderProgress = percent => `${percent}% ${loadingBar(percent)}`;

    console.log(renderProgress(percent));
    console.log(percent === 100 ? 'Complete!' : 'Still loading...');
}

solve(30);
solve(100);
