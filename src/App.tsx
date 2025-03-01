import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Components/Navbar";
import PriceTag from "./Components/PriceTag"; 
import HeroSection from "./Components/HeroSection";
import Redeem from "./Components/Redeem";
import History from "./Components/History";

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <PriceTag /> 
        <Routes>
          <Route path="/" element={<HeroSection />} />  
          <Route path="/dashboard" element={<HeroSection />} />
          <Route path="/redeem" element={<Redeem />} />
          <Route path="/Achievement" element={<History />} />
        </Routes>
      </div>  
    </Router>
  );
};

export default App;
