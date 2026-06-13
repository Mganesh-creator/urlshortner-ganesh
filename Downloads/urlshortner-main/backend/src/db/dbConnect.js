import mongoose from "mongoose";
import { config } from "../config.js";

console.log("Mongo URI =", config.MONGODB_URI);

const connectDB = async () => {
  try {
    await mongoose.connect(config.MONGODB_URI);
    console.log("MongoDB connected successfully");
  } catch (err) {
    console.error("MongoDB connection error:", err.message);
    process.exit(1);
  }
};

export default connectDB;
