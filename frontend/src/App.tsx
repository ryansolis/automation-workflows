import React, { useEffect, useState } from "react";
import axios from "axios";

interface Workflow {
  title: string;
  description: string;
  platform: string;
}

const App: React.FC = () => {
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [search, setSearch] = useState("");
  const [platforms, setPlatforms] = useState<string[]>([]);
  const [selectedPlatform, setSelectedPlatform] = useState<string>("All");

  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 10; // Number of workflows per page

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/workflows")
      .then((res) => {
        const data = res.data as Workflow[];
        setWorkflows(data);

        const uniquePlatforms = ["All", ...Array.from(new Set(data.map((w) => w.platform)))];
        setPlatforms(uniquePlatforms);
      })
      .catch((err) => console.error("Error fetching data:", err));
  }, []);

  // Filtered workflows based on search & platform selection
  const filteredWorkflows = workflows.filter(
    (workflow) =>
      workflow.title.toLowerCase().includes(search.toLowerCase()) &&
      (selectedPlatform === "All" || workflow.platform === selectedPlatform)
  );

  // Pagination calculations
  const totalPages = Math.ceil(filteredWorkflows.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const paginatedWorkflows = filteredWorkflows.slice(startIndex, startIndex + itemsPerPage);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-800 mb-6 text-center">Automation Workflows</h1>

        <div className="flex flex-col md:flex-row gap-4 mb-6">
          <input
            type="text"
            placeholder="Search workflows..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full md:w-2/3 p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-400"
          />
          <select
            value={selectedPlatform}
            onChange={(e) => setSelectedPlatform(e.target.value)}
            className="w-full md:w-1/3 p-3 border border-gray-300 rounded-lg shadow-sm bg-white focus:ring-2 focus:ring-blue-400"
          >
            {platforms.map((platform) => (
              <option key={platform} value={platform}>
                {platform}
              </option>
            ))}
          </select>
        </div>

        <div className="space-y-4">
          {paginatedWorkflows.map((workflow, index) => (
            <div key={index} className="bg-white p-5 rounded-lg shadow-md border border-gray-200">
              <h2 className="text-xl font-semibold text-gray-800">{workflow.title}</h2>
              <p className="text-gray-600">{workflow.description}</p>
              <p className="mt-2 text-sm font-medium text-blue-600">Platform: {workflow.platform}</p>
            </div>
          ))}
        </div>

        {/* Pagination Controls */}
        <div className="flex justify-center mt-6 space-x-4">
          <button
            onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
            disabled={currentPage === 1}
            className="px-4 py-2 bg-gray-300 rounded-lg shadow-md hover:bg-gray-400 disabled:opacity-50"
          >
            Previous
          </button>

          <span className="px-4 py-2 bg-gray-200 rounded-lg shadow-md">
            Page {currentPage} of {totalPages}
          </span>

          <button
            onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
            disabled={currentPage === totalPages}
            className="px-4 py-2 bg-gray-300 rounded-lg shadow-md hover:bg-gray-400 disabled:opacity-50"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
