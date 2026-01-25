const API = "http://127.0.0.1:8000";

export async function getShifts() {
  const res = await fetch(`${API}/shifts`);
  if (!res.ok) throw new Error("Failed to fetch shifts");
  return res.json();
}

export async function parseText(text) {
  const res = await fetch(`${API}/parse`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) throw new Error("Failed to parse text");
  return res.json();
}

export async function claimShift(id, employee = "Alex") {
  const res = await fetch(`${API}/shifts/${id}/claim`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ employee }),
  });
  if (!res.ok) throw new Error("Failed to claim shift");
  return res.json();
}

