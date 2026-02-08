import { useEffect, useState } from "react";

function App() {
  const [facts, setFacts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/facts")
      .then(res => res.json())
      .then(data => setFacts(data));
  }, []);

  return (
    <div>
      <h1>Fun Facts</h1>
      <ul>
        {facts.map(f => (
          <li key={f.id}>{f.fact}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
