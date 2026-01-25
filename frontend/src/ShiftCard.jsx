export default function ShiftCard({ shift, onClaim, loading }) {
  const remaining = Math.max(0, shift.slots - shift.claimed);

  return (
    <div
      style={{
        border: "1px solid #eee",
        borderRadius: 12,
        padding: 12,
        display: "grid",
        gap: 6,
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <strong>{shift.site || "Open Shift"}</strong>
        {shift.pay != null && <span>${Math.round(shift.pay)}/hr</span>}
      </div>

      <div style={{ color: "#555" }}>
        {shift.date} • {shift.start} - {shift.end}
      </div>

      <div style={{ color: remaining === 0 ? "darkorange" : "#666" }}>
        Slots left: {remaining}
      </div>

      <button
        onClick={() => onClaim(shift.id)}
        disabled={loading || remaining === 0}
        style={{
          padding: "8px 12px",
          borderRadius: 10,
          border: "none",
          cursor: remaining === 0 ? "not-allowed" : "pointer",
        }}
      >
        {remaining === 0 ? "Filled" : "Claim"}
      </button>
    </div>
  );
}

