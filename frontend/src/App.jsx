import { useEffect, useState } from "react";
import Chat from "./Chat";
import Shifts from "./Shifts";
import { claimShift, getShifts, parseText } from "./api";

export default function App() {
  const [shifts, setShifts] = useState([]);
  const [loading, setLoading] = useState(false);

  async function refresh() {
    const data = await getShifts();
    setShifts(data);
  }

  useEffect(() => {
    refresh();
  }, []);

  async function handleParse(text) {
    setLoading(true);
    try {
      await parseText(text);
      await refresh();
    } finally {
      setLoading(false);
    }
  }

  async function handleClaim(id) {
    setLoading(true);
    try {
      await claimShift(id, "Alex");
      await refresh();
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 900, margin: "40px auto", fontFamily: "system-ui" }}>
      <h1>AUshift MVP</h1>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
        <Chat onParse={handleParse} loading={loading} />
        <Shifts shifts={shifts} onClaim={handleClaim} loading={loading} />
      </div>
    </div>
  );
}

