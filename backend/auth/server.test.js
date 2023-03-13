const request = require('supertest')
const app = require('./server')
const firebase = require('firebase/auth')
const initialise = require('firebase/app');
const { default: mongoose } = require('mongoose');

const firebaseConfig = {
    apiKey: `${process.env.apiKey}`,
    authDomain: `${process.env.authDomain}`,
    projectId: `${process.env.projectId}`,
    storageBucket: `${process.env.storageBucket}`,
    messagingSenderId: `${process.env.messagingSenderId}`,
    appId: `${process.env.appId}`
};

initialise.initializeApp(firebaseConfig)

var uid = ''

describe("Authentication API testing", () => {
    test('Returns 200 OK when signup request is valid', async () => {
        await request(app).get("/")
    })
})

describe("POST /register", () => {
    test('should return registered', async () => {
        const res = await request(app).post('/register')
        .send({
            email: 'test@test.com',
            password: 'Password',
            firstName: 'John',
            lastName: 'Doe',
            departmentId: 1,
            officeId: 1
        })
        uid = await firebase.getAuth().currentUser.reloadUserInfo.localId
        expect(res.body).toBe("Registered")
    }, 10000)
})

describe("POST /login", () => {
    test('should return login', async () => {
        const res = await request(app).post('/login')
        .send({
            email: 'test@test.com',
            password: 'Password'
        })
        expect(res.body).toBe("Login")
    }, 10000)
})

afterAll(async () => {
    const user = await firebase.getAuth().currentUser
    await firebase.deleteUser(user)
    await mongoose.connection.collection('users').deleteMany({})
    await mongoose.disconnect()
})