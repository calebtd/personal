const status = Number(process.argv[2]);

if (status === 0) {
    console.log('alive');
} else {
    console.log('other');
}