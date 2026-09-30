import { useEffect, useState } from "react";
import API from "./api";

function TestBackend() {
  const [message, setMessage] = useState("Connecting...");

  useEffect(() => {
    async function testBackend() {
      try {
        const response = await API.get("/health");

        console.log("Backend response:", response.data);

        setMessage(response.data.status);
      } catch (error) {
        console.error("Backend connection error:", error);
        setMessage("Backend connection failed");
      }
    }

    testBackend();
  }, []);

  return (
    <div>
      <h1>CampusLink Backend Test</h1>
      <p>{message}</p>
    </div>
  );
}

export default TestBackend;