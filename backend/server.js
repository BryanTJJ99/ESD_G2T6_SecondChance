const express = require('express');
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const cors = require('cors')
require('dotenv').config()

const app = express()
app.use(cors({
    origin: '*'
}))

app.use(bodyParser.json({limit: '50mb'}))
app.use(bodyParser.urlencoded({extended: false, limit: '50mb'}))

mongoose.connect(`${process.env.MONGODB}`)

app.listen(8080)