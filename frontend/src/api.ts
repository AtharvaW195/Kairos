const apiUrl = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export async function authenticate(path: "/register" | "/login", email: string, password: string): Promise<string> {
  const response = await fetch(`${apiUrl}${path}`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password }) });
  if (!response.ok) {
    const body = await response.json().catch(() => ({ detail: "Unable to reach Kairos." }));
    throw new Error(body.detail ?? "Authentication failed.");
  }
  return (await response.json() as { access_token: string }).access_token;
}
