import { Route, Routes } from "react-router-dom";
import { AppShell } from "./components/AppShell";
import { AuthForm } from "./pages/AuthForm";
import { Home } from "./pages/Home";
import { Placeholder } from "./pages/Placeholder";

export default function App() { return <Routes><Route element={<AppShell />}><Route path="/" element={<Home />} /><Route path="/login" element={<AuthForm mode="login" />} /><Route path="/register" element={<AuthForm mode="register" />} /><Route path="/dashboard" element={<Placeholder title="Dashboard" />} /><Route path="/market" element={<Placeholder title="Market" />} /><Route path="/portfolio" element={<Placeholder title="Portfolio" />} /><Route path="/watchlist" element={<Placeholder title="Watchlist" />} /><Route path="/ai-insights" element={<Placeholder title="AI Insights" />} /></Route></Routes>; }
