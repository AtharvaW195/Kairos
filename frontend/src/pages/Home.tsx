import { Link } from "react-router-dom";

export function Home() {
  return <section className="py-20 text-center"><p className="mb-4 font-semibold text-emerald-400">Trade with intention</p><h1 className="mx-auto max-w-3xl text-5xl font-bold tracking-tight">Practice smarter investing with Kairos.</h1><p className="mx-auto mt-6 max-w-xl text-lg text-slate-400">A focused trading simulator for exploring markets, building portfolios, and learning from every decision.</p><div className="mt-10 flex justify-center gap-4"><Link to="/register" className="rounded-lg bg-emerald-500 px-5 py-3 font-semibold text-slate-950">Create an account</Link><Link to="/login" className="rounded-lg border border-slate-700 px-5 py-3 font-semibold">Sign in</Link></div></section>;
}
