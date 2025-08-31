import Navbar from "./components/Navbar";
import PropertyCard from "./components/PropertyCard";
import Services from "./components/Services";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div>
      <Navbar />
      <h1 className="text-center text-3xl font-bold my-4">🏠 Our Properties</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 p-4">
        <PropertyCard title="3BHK Apartment" price="₹45,00,000" />
        <PropertyCard title="Luxury Villa" price="₹1.25 Cr" />
      </div>
      <Services />
      <Footer />
    </div>
  );
}
