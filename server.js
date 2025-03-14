const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

const db = new sqlite3.Database("qr_codes.db", (err) => {
    if (err) {
        console.error("Database connection failed:", err.message);
    } else {
        console.log("Connected to SQLite database.");
        db.run("CREATE TABLE IF NOT EXISTS qrcodes (id INTEGER PRIMARY KEY AUTOINCREMENT, qr_data TEXT UNIQUE)");
    }
});

app.post("/register", (req, res) => {
    const { qr_data } = req.body;

    if (!qr_data) {
        return res.status(400).json({ message: "QR data is required" });
    }

    db.run("INSERT INTO qrcodes (qr_data) VALUES (?)", [qr_data], (err) => {
        if (err) {
            return res.status(500).json({ message: "Failed to insert QR data or already exists" });
        }
        res.json({ message: "QR data registered successfully!" });
    });
});

app.get("/qrcodes", (req, res) => {
    db.all("SELECT * FROM qrcodes", [], (err, rows) => {
        if (err) {
            return res.status(500).json({ message: "Failed to retrieve data" });
        }
        res.json(rows);
    });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
