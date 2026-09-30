import { useState } from "react";
import API from "./api";

import RegistrationForm from "./components/Registration/RegistrationForm";
import OTPVerification from "./components/Registration/OTPVerification";
import Dashboard from "./pages/Dashboard";

import { PublicPassportVerification } from "./components/placement/PlacementExperience";

function App() {
  const [currentStep, setCurrentStep] = useState("registration");
  const [studentData, setStudentData] = useState(null);

  const passportRoute = window.location.pathname.match(
    /^\/passport\/verify\/([^/]+)/
  );

  const startRegistration = async (data) => {
    try {
      // Send student information to FastAPI
      const response = await API.post("/students/", {
        name: data.fullName,
        email: data.email,
        phone: data.phone,
        collegeId: data.collegeId,
        branch: data.branch,
      });

      console.log("Student saved successfully:", response.data);

      // Keep student data for dashboard
      setStudentData({
        fullName: data.fullName,
        email: data.email,
        phone: data.phone,
        collegeId: data.collegeId,
        branch: data.branch,
      });

      // Move to OTP page
      setCurrentStep("otp");
    } catch (error) {
      console.error("Backend connection error:", error);

      alert("Could not connect to CampusLink backend.");
    }
  };

  const verifyOtp = () => {
    setCurrentStep("dashboard");
  };

  // Passport verification page
  if (passportRoute) {
    return (
      <PublicPassportVerification
        passportId={passportRoute[1]}
      />
    );
  }

  // Registration page
  if (currentStep === "registration") {
    return (
      <RegistrationForm
        onContinue={startRegistration}
      />
    );
  }

  // OTP page
  if (currentStep === "otp") {
    return (
      <OTPVerification
        studentData={studentData}
        onVerified={verifyOtp}
        onBack={() => setCurrentStep("registration")}
      />
    );
  }

  // Dashboard
  return (
    <Dashboard
      studentData={studentData}
    />
  );
}

export default App;