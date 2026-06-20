function authMiddleware(req, res, next) {
    console.log("Authenticating request...");
    next();
}