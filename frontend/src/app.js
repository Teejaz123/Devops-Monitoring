import React, { useEffect, useState } from "react";

function App() {
  const [metrics, setMetrics] = useState({});
  const [data, setData] = useState({});

  useEffect(() => {
    fetch("/api/metrics")
      .then(res => res.json())
      .then(setMetrics);

    fetch("/api/data")
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>DevOps Dashboard</h1>
      <h2>System Metrics</h2>
      <p>CPU Usage: {metrics.cpu_percent}%</p>
      <p>Memory Usage: {metrics.memory_percent}%</p>
      <h2>App Data</h2>
      <p>Users: {data.users}</p>
      <p>Active Sessions: {data.active_sessions}</p>
    </div>
  );
}

export default App;

