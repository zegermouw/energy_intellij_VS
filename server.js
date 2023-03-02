const http = require("http");
const host = 'localhost';
const port = 8000;
var robot = require("robotjs");
const program_type = process.argv[2];
const requestListener = function (req, res) {
    res.writeHead(200);
    res.end("My first server!");
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});

async function test() {
    console.log('start timer');
    await new Promise(resolve => setTimeout(resolve, 10000));
    console.log('after 10 seconds');
    server.close()
    if(program_type == "intellij"){
        robot.keyToggle('alt', 'down')
        robot.keyTap('f4')
        robot.keyToggle('alt', 'up')
    } else {

        robot.keyToggle('control', 'down');
        robot.keyTap('w');
        robot.keyToggle('control', 'up');
    }

}
test()
console.log("test")
