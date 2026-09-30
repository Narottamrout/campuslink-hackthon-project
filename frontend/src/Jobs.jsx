import { useEffect, useState } from "react";
import API from "./api";

function Jobs() {

  const [jobs, setJobs] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");


  useEffect(() => {

    async function getJobs() {

      try {

        const response = await API.get("/jobs/");

        console.log(
          "Jobs received from backend:",
          response.data
        );

        setJobs(response.data.data);

      } catch (error) {

        console.error(
          "Backend connection error:",
          error
        );

        setError("Unable to load jobs.");

      } finally {

        setLoading(false);

      }
    }

    getJobs();

  }, []);


  if (loading) {
    return <h2>Loading jobs...</h2>;
  }


  if (error) {
    return <h2>{error}</h2>;
  }


  return (
    <div>

      <h1>Available Jobs</h1>

      {jobs.length === 0 ? (

        <p>No jobs available.</p>

      ) : (

        jobs.map((job, index) => (

          <div key={index}>

            <h2>{job.title}</h2>

            <p>
              Company: {job.company}
            </p>

            <p>
              Location: {job.location}
            </p>

            <p>
              Skills:{" "}
              {job.required_skills?.join(", ")}
            </p>

            <hr />

          </div>

        ))

      )}

    </div>
  );
}

export default Jobs;