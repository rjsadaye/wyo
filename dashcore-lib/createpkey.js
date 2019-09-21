

var bitcore=require('./index.js');

var privateKey = new bitcore.PrivateKey('yZZUvP9F6XNUxPsFun6zeH7UQ6RwRD7S6R','testnet');

var exported = privateKey.toWIF();
// e.g. L3T1s1TYP9oyhHpXgkyLoJFGniEgkv2Jhi138d7R2yJ9F4QdDU2m
var imported = bitcore.PrivateKey.fromWIF(exported);
var hexa = privateKey.toString();

console.log(hexa);
