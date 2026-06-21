function authMiddleware(req, res, next) {
    console.log("Authenticating request...");

    // Simulated token (normally from headers)
    const token = req.headers["authorization"];

    if (!token) {
        return res.status(401).json({
            success: false,
            message: "No token provided"
        });
    }

    // Simulated validation
    if (token === "valid_token") {
        req.user = {
            id: "demo_user",
            role: "developer"
        };

        console.log("Authentication successful");
        return next();
    }

    return res.status(403).json({
        success: false,
        message: "Invalid token"
    });
}

module.exports = authMiddleware;