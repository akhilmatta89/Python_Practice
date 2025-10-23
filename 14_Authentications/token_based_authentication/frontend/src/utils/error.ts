export function toErrorMessage(e: any): string {
  const detail = e?.response?.data?.detail;

  if (typeof detail === "string") return detail;

  if (Array.isArray(detail)) {
    // FastAPI validation errors
    const msgs = detail.map((d) => {
      const where = Array.isArray(d.loc) ? d.loc.join(".") : d.loc;
      return `${where}: ${d.msg}`;
    }).join("\n");
    return msgs || "Validation error";
  }

  return e?.response?.data?.message || e?.message || "Request failed";
}
