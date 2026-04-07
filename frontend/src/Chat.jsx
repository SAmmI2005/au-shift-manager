import { useState } from "react";

export default function Chat({ onParse, loading }) {
  const [text, setText] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const t = text.trim();
    if (!t) return;
    await onParse(t);
    setText("");
  }

  return (
    <div style={{ border: "1px solid #ddd", borderRadius: 12, padding: 16 }}>
      <h2>Chat (Manager Paste)</h2>

      <p style={{ color: "#666", marginTop: 0 }}>
        Paste shift text in any format. MVP parser detects lines with <b>MM/DD</b> and <b>HH:MM - HH:MM</b>.
      </p>

      <form onSubmit={handleSubmit}>
        <textarea
          rows={10}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Example:\n• Community Parks\n_ 8/13 09:00 - 17:00"
          style={{
            width: "100%",
            padding: 10,
            borderRadius: 10,
            border: "1px solid #ccc",
            resize: "vertical",
          }}
        />

        <button
          type="submit"
          disabled={loading || !text.trim()}
          style={{
            marginTop: 10,
            padding: "10px 14px",
            borderRadius: 10,
            border: "none",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Working..." : "Send / Parse"}
        </button>
      </form>
    </div>
  );
}
