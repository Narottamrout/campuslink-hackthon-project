import { useEffect, useState } from "react";
import API from "./api";

function Students() {

    const [students, setStudents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function getStudents() {

            try {

                const response = await API.get("/students/");

                console.log("Backend response:", response.data);

                setStudents(response.data.data);

            } catch (error) {

                console.error("Backend connection error:", error);

                setError("Could not connect to backend");

            } finally {

                setLoading(false);

            }
        }

        getStudents();

    }, []);


    if (loading) {
        return <h2>Loading students...</h2>;
    }


    if (error) {
        return <h2>{error}</h2>;
    }


    return (
        <div>

            <h1>CampusLink Students</h1>

            {students.length === 0 ? (

                <p>No students found.</p>

            ) : (

                students.map((student, index) => (

                    <div key={index}>

                        <h2>{student.name}</h2>

                        <p>
                            College: {student.college}
                        </p>

                        <p>
                            Course: {student.course}
                        </p>

                        <p>
                            Graduation Year: {student.graduation_year}
                        </p>

                        <p>
                            Skills:{" "}
                            {student.skills?.join(", ")}
                        </p>

                        <hr />

                    </div>

                ))

            )}

        </div>
    );
}

export default Students;