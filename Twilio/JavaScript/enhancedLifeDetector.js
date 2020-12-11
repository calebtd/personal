const status = Number(process.argv[2]);

if (status === 0) {
    console.log('alive');
} else if (status === 1) {
    console.log('flowering');
} else if (status === 2) {
    console.log('shedding');
} else {
    console.log('other');
}