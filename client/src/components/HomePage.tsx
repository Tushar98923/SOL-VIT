import React, { useState } from "react";
import { Home, Plane, Mail, User, MapPin } from "lucide-react";

const cities = [
  "Mumbai", 
  "Shirdi",
];

export const HomePage = () => {
  const [startPoint, setStartPoint] = useState("");
  const [destination, setDestination] = useState("");

  return (
    <div className="p-4 bg-blue-100 min-h-screen">
      {/* Greeting */}
      <h2 className="text-lg font-semibold mb-4">Hi, User</h2>

      {/* Search Fields */}
      <div className="bg-white p-4 rounded-xl shadow-md mb-4">
        <div className="flex items-center border-b mb-2 pb-2">
          <MapPin className="text-pink-500 mr-2" />
          <select
            className="flex-1 p-2 border rounded"
            value={startPoint}
            onChange={(e) => setStartPoint(e.target.value)}
          >
            <option value="" disabled>
              Select Start Point
            </option>
            {cities.map((city, index) => (
              <option key={index} value={city}>
                {city}
              </option>
            ))}
          </select>
        </div>
        <div className="flex items-center">
          <MapPin className="text-black mr-2" />
          <select
            className="flex-1 p-2 border rounded my-3"
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
          >
            <option value="" disabled>
              Select Destination
            </option>
            {cities.map((city, index) => (
              <option key={index} value={city}>
                {city}
              </option>
            ))}
          </select>
        </div>
        <button className="btn w-full">Suggest Me</button>
      </div>

      
      <h2 className="font-bold text-[2vw] text-center" >Select Your Arrival and Destitantion</h2>


      {/* Bottom Navigation */}
      <div className="fixed bottom-0 left-0 right-0 bg-white p-3 flex justify-around shadow-md">
        {/* {[
          { icon: <Home className="text-blue-500" />, label: "Home" },
          { icon: <Plane />, label: "My Trip" },
          { icon: <Mail />, label: "Inbox" },
          { icon: <User />, label: "Account" },
        ].map((item, index) => (
          <div key={index} className={`flex flex-col items-center text-sm ${item.label === "Home" ? "text-blue-500 font-bold" : "text-gray-700"}`}>
            {item.icon}
            <p>{item.label}</p>
          </div>
        ))} */}
        <div className="hover:bg-gray-300 p-1 rounded-md cursor-pointer">
          <Home></Home>
        </div>
        <div className="hover:bg-gray-300 p-1 rounded-md cursor-pointer">
          <Mail></Mail>
        </div>
        <div className="hover:bg-gray-300 p-1 rounded-md cursor-pointer">
          <User></User>
        </div>
      </div>
      
    </div>
  );
};
