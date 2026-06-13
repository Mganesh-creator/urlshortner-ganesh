import jwt from "jsonwebtoken";
import { config } from "../config.js";

export const loggedInUser = (req, res, next) => {
  console.log("========== AUTH DEBUG ==========");

  const authHeader = req.headers.authorization;

  console.log("Authorization Header:", authHeader);

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return res.status(401).json({
      status: "UNAUTHORIZED",
      message: "No token found",
    });
  }

  const token = authHeader.split(" ")[1];

  try {
    const decoded = jwt.verify(token, config.JWT_SECRET);

    console.log("Decoded:", decoded);

    req.user = decoded;
    next();
  } catch (error) {
    console.log("JWT VERIFY ERROR:", error.message);

    return res.status(403).json({
      status: "FORBIDDEN",
      message: "Invalid token",
    });
  }
};
