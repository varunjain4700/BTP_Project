// const express = require("express");
// const { spawn } = require("child_process");
// const app = express();
// const port = 3000;
// app.get("/", (req, res) => {
//   var dataToSend;
//   // spawn new child process to call the python script
//   const python = spawn("python", ["script1.py"]);
//   // collect data from script
//   python.stdout.on("data", function (data) {
//     console.log("Pipe data from python script ...");
//     dataToSend = data.toString();
//   });
//   // in close event we are sure that stream from child process is closed
//   python.on("close", (code) => {
//     console.log(`child process close all stdio with code ${code}`);
//     // send data to browser
//     res.send(dataToSend);
//   });
// });
// app.listen(port, () =>
//   console.log(`Example app listening on port 
// ${port}!`)
// );

const express = require("express");
const { spawn } = require("child_process");
const app = express();
const port = 3000;
app.get("/", (req, res) => {
  var dataToSend;
  // spawn new child process to call the python script
  // const data = `India, officially the Republic of India, is a country in South Asia.`; // req.body.file or data
  const data='/Users/varunjain/Desktop/BTP_project/India.pdf'
  const indexing = spawn("python", ["/Users/varunjain/Desktop/BTP_project/indexing.py",data]);
  // spawn new child process to call the python script
  // const python = spawn('python', ['script2.py','node.js','python']);

  // collect data from script
  indexing.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = data.toString();
  });

  // in close event we are sure that stream from child process is closed
  indexing.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    // res.send(dataToSend);
  });

  doc_name = "India.pdf";
  const encryption =  spawn("python", [
    "/Users/varunjain/Desktop/BTP_project/Searchable_Encryption/encrypt_index.py",
    doc_name,
  ]);
  // spawn new child process to call the python script
  // const python = spawn('python', ['script2.py','node.js','python']);
  // collect data from script
  encryption.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  encryption.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(dataToSend);
  });
});

// app.get("/encrypt", async (req, res) => {
//   doc_name = "India.pdf";
//   const encryption = await spawn("python", [
//     "/Users/varunjain/Desktop/BTP_project/Searchable_Encryption/encrypt_index.py",doc_name
//   ]);
//   // spawn new child process to call the python script
//   // const python = spawn('python', ['script2.py','node.js','python']);
//   // collect data from script
//   encryption.stdout.on("data", function (data) {
//     console.log("Pipe data from python script ...");
//     dataToSend = data.toString();
//   });
//   // in close event we are sure that stream from child process is closed
//   encryption.on("close", (code) => {
//     console.log(`child process close all stdio with code ${code}`);
//     // send data to browser
//     res.send(dataToSend);
//   });
// });

//server 1
// app.get("/trapdoor", (req, res)=> {
//   // const query
//   // const keyword = req.body.keyword;
//   const keyword = "india";
//   const python = spawn("python", [
//     "/Users/varunjain/Desktop/BTP_project/Searchable_Encryption/trapdoor.py", keyword ]);
//   // spawn new child process to call the python script
//   // const python = spawn('python', ['script2.py','node.js','python']);
//   // collect data from script
//   python.stdout.on("data", function (data) {
//     console.log("Pipe data from python script ...");
//     dataToSend = data.toString();
//   });
//   // in close event we are sure that stream from child process is closed
//   python.on("close", (code) => {
//     console.log(`child process close all stdio with code ${code}`);
//     // send data to browser
//     res.send(dataToSend);
//   });
// })

// app.get("/search", (req, res) => {
//   // const query
//   // const keyword = req.body.keyword;
//   // const keyword = "India";
//   const python = spawn("python", [
//     "/Users/varunjain/Desktop/BTP_project/Searchable_Encryption/sse_search.py",
//   ]);
//   // spawn new child process to call the python script
//   // const python = spawn('python', ['script2.py','node.js','python']);
//   // collect data from script
//   python.stdout.on("data", function (data) {
//     console.log("Pipe data from python script ...");
//     dataToSend = data.toString();
//   });
//   // in close event we are sure that stream from child process is closed
//   python.on("close", (code) => {
//     console.log(`child process close all stdio with code ${code}`);
//     // send data to browser
//     res.send(dataToSend);
//   });
// });

app.listen(port, () =>
  console.log(`Example app listening on port 
${port}!`)
);
