import ShiftCard from "./ShiftCard";

export default function Shifts({ shifts, onClaim, loading }) {
  return (
    <div style={{ border: "1px solid #ddd", borderRadius: 12, padding: 16 }}>
      <h2>Open Shifts</h2>

      {shifts.length === 0 ? (
        <p style={{ color: "#666" }}>No shifts yet. Paste something in Chat.</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {shifts.map((s) => (
            <ShiftCard key={s.id} shift={s} onClaim={onClaim} loading={loading} />
          ))}
        </div>
      )}
    </div>
  );
}

