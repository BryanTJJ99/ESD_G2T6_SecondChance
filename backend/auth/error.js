module.exports = {
    errorHandling: function (error){
        switch(error.code){
            case "auth/email-already-in-use":
                return "Email is already in use"
            case "auth/weak-password":
                return "The password must be 6 characters long or more"
            case "auth/email-already-in-use":
                return "The email address is already in use by another account"
            // case "auth/invalid-email":
            //     res.status(400).send("Please use a valid email address")
            case "auth/wrong-password":
                return "The credentials provided are incorrect"
            case "auth/user-not-found":
                return "The credentials provided are incorrect"
            default:
                return "Please use a valid email address"
        }
    }
}