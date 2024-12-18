#!/usr/bin/node
if (process.argv.length < 3)
{
  console.log("No argument");
}
else if (process.argv.length < 4)
{
  console.log("Argument Found");
}
else if (process.argv.length >= 4){
  console.log("Arguments Found")
}
