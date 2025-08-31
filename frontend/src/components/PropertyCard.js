export default function PropertyCard({ title, price }) {
  return (
    <div className="border p-4 shadow-lg rounded-xl">
      <h2 className="text-xl font-semibold">{title}</h2>
      <p className="text-green-600">{price}</p>
      <button className="mt-2 bg-blue-600 text-white px-4 py-2 rounded-lg">
        View Details
      </button>
    </div>
  );
}
