
var bitcore=require('./index.js');


var sender = process.argv[2];
var receiver = process.argv[3];
var privatekey = process.argv[4];
var txid = process.argv[5];
var outindex = parseInt(process.argv[6]);
var address = process.argv[7];
var script = process.argv[8];
var satoshis = parseInt(process.argv[9]);
var encoded_data= process.argv[10];


var pk = new bitcore.PrivateKey(privatekey);

var utxo = {
  "txId" : txid,
  "outputIndex" : outindex,
  "address" : address,
  "script" : script,
  "satoshis" : satoshis
};

var transaction = new bitcore.Transaction()
    .from(utxo)
    .to(receiver,0)
    .change(sender)
    .addData(encoded_data) // Add OP_RETURN data
    .sign(pk);

console.log(transaction);
