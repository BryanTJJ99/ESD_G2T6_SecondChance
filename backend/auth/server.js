const firebase = require('firebase/auth')
const initialise = require('firebase/app')
const express = require('express');
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const cors = require('cors')
const errorHandling = require('./error')
const session = require('express-session')
require('dotenv').config()

mongoose.connect(`${process.env.MONGODB}`)

var Schema = mongoose.Schema

var UserSchema = new Schema({
    id: String,
    firstName: String,
    lastName: String,
    departmentId: Number,
    officeId: Number
})

var Users = mongoose.model('users', UserSchema)

const app = express()
app.use(cors({
    origin: '*'
}))

app.use(session({
    secret: `${process.env.secret}`
}))

const firebaseConfig = {
    apiKey: `${process.env.apiKey}`,
    authDomain: `${process.env.authDomain}`,
    projectId: `${process.env.projectId}`,
    storageBucket: `${process.env.storageBucket}`,
    messagingSenderId: `${process.env.messagingSenderId}`,
    appId: `${process.env.appId}`
};

initialise.initializeApp(firebaseConfig)

app.use(bodyParser.json({limit: '50mb'}))
app.use(bodyParser.urlencoded({extended: false, limit: '50mb'}))

app.get("/", (req,res) => {
    res.status(200).send("It works")
})

app.post("/register", async (req, res) => {
    const email = req.body.email
    const password = req.body.password
    const firstName = req.body.firstName
    const lastName = req.body.lastName
    const departmentId = req.body.departmentId
    const officeId = req.body.officeId
    try {
        await firebase.createUserWithEmailAndPassword(firebase.getAuth(), email, password)
        const userId = await firebase.getAuth().currentUser.reloadUserInfo.localId
        await Users.create({
            id: userId,
            firstName: firstName,
            lastName: lastName,
            departmentId: departmentId,
            officeId: officeId
        })
        res.status(200).json("Registered")
    } catch (error) {
        console.log(error)
        const errMsg = errorHandling.errorHandling(error)
        res.status(400).json(errMsg)
    }
})

app.post("/login", async (req,res) => {
    const email = req.body.email
    const password = req.body.password
    try{
        await firebase.signInWithEmailAndPassword(firebase.getAuth(), email, password)
        const userId = await firebase.getAuth().currentUser.reloadUserInfo.localId
        req.session.uid = userId
        res.status(200).json("Login")
    } catch (error) {
        const errMsg = errorHandling.errorHandling(error)
        res.status(400).json(errMsg)
    }
})

module.exports = app

app.listen(8080)