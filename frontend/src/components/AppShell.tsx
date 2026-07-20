import { NavLink, Outlet } from "react-router-dom";

const links = ["Dashboard", "Market", "Portfolio", "Watchlist", "AI Insights"];

export function AppShell() {
  return <><header className="border-b border-slate-800"><nav className="mx-auto flex max-w-6xl items-center gap-6 px-6 py-4"><NavLink to="/" className="text-xl font-bold text-emerald-400">Kairos</NavLink><div className="flex flex-wrap gap-4 text-sm text-slate-300">{links.map((link) => <NavLink key={link} to={`/${link.toLowerCase().replace(" ", "-")}`} className={({ isActive }) => isActive ? "text-emerald-400" : "hover:text-white"}>{link}</NavLink>)}</div></nav></header><main className="mx-auto max-w-6xl px-6 py-12"><Outlet /></main></>;
}
