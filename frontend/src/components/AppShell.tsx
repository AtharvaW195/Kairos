import { NavLink, Outlet, useNavigate } from "react-router-dom";

const links = ["Dashboard", "Market", "Portfolio", "Watchlist", "AI Insights"];

export function AppShell() {
  const navigate = useNavigate();
  const isAuthenticated = Boolean(localStorage.getItem("kairos_token"));

  function logout() {
    localStorage.removeItem("kairos_token");
    navigate("/");
  }

  return <><header className="border-b border-slate-800"><nav className="mx-auto flex max-w-6xl items-center gap-6 px-6 py-4"><NavLink to={isAuthenticated ? "/dashboard" : "/"} className="text-xl font-bold text-emerald-400">Kairos</NavLink><div className="flex flex-1 flex-wrap gap-4 text-sm text-slate-300">{links.map((link) => <NavLink key={link} to={`/${link.toLowerCase().replace(" ", "-")}`} className={({ isActive }) => isActive ? "text-emerald-400" : "hover:text-white"}>{link}</NavLink>)}</div>{isAuthenticated ? <button onClick={logout} className="text-sm font-medium text-slate-300 hover:text-white">Log out</button> : <NavLink to="/login" className="text-sm font-medium text-slate-300 hover:text-white">Sign in</NavLink>}</nav></header><main className="mx-auto max-w-6xl px-6 py-12"><Outlet /></main></>;
}
