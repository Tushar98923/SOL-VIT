import { useState } from 'react'

export const HomePage = () => {
  const [startPoint, setStartPoint] = useState('');
  const [destination, setDestination] = useState('');
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div className="max-w mx-auto bg-white min-h-screen shadow-md relative overflow-hidden rounded-lg">
      {/* Top Menu */}
      <div className="bg-white p-2 flex justify-end">
        <button 
          onClick={() => setMenuOpen(!menuOpen)} 
          className="text-gray-600 p-1"
        >
          ☰
        </button>
        
        {/* Dropdown Menu */}
        {menuOpen && (
          <div className="absolute right-0 top-10 bg-white shadow-lg rounded-lg z-10 w-40 border border-gray-100">
            <ul className="py-1">
              <li className="hover:bg-gray-100">
                <button className="px-4 py-2 text-sm text-gray-700 w-full text-left flex items-center">
                  <span className="mr-2">➕</span> Add Stop
                </button>
              </li>
              <li className="hover:bg-gray-100">
                <button className="px-4 py-2 text-sm text-gray-700 w-full text-left">Settings</button>
              </li>
              <li className="hover:bg-gray-100">
                <button className="px-4 py-2 text-sm text-gray-700 w-full text-left">Help</button>
              </li>
            </ul>
          </div>
        )}
      </div>
      
      {/* Header */}
      <div className="bg-blue-100 p-4 rounded-b-2xl">
        <div className="mt-2 space-y-3">
          {/* Start point input */}
          <div className="flex items-center bg-white rounded-lg shadow p-3">
            <span className="mr-2 text-gray-500">📍</span>
            <input 
              type="text" 
              placeholder="Start point" 
              className="w-full outline-none text-sm"
              value={startPoint}
              onChange={(e) => setStartPoint(e.target.value)}
            />
          </div>
          
          {/* Destination input */}
          <div className="flex items-center bg-white rounded-lg shadow p-3">
            <span className="mr-2 text-gray-500">🏁</span>
            <input 
              type="text" 
              placeholder="Destination" 
              className="w-full outline-none text-sm"
              value={destination}
              onChange={(e) => setDestination(e.target.value)}
            />
          </div>
        </div>
      </div>
      
      {/* Greeting */}
      <div className="p-4 font-semibold text-gray-800">
        Hi, Thanh Giang
      </div>
      
      {/* Travel Mode Icons */}
      <div className="flex justify-around px-4 mt-4">
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-white mb-2">
            ✈️
          </div>
          <span className="text-xs text-gray-700">Flight</span>
        </div>
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-orange-500 flex items-center justify-center text-white mb-2">
            🚂
          </div>
          <span className="text-xs text-gray-700">Train</span>
        </div>
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-purple-500 flex items-center justify-center text-white mb-2">
            🚌
          </div>
          <span className="text-xs text-gray-700">Bus</span>
        </div>
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-yellow-500 flex items-center justify-center text-white mb-2">
            🚕
          </div>
          <span className="text-xs text-gray-700">Cabs</span>
        </div>
      </div>
      
      {/* Promotional Banner */}
      <div className="mx-4 mt-6 bg-blue-50 rounded-lg p-3 shadow-sm flex justify-between items-center relative">
        <div className="pr-2">
          <p className="text-sm font-bold">Top places to visit in India</p>
          <p className="text-xs text-gray-700">Discover beautiful locations and historical landmarks across India!</p>
        </div>
        <button className="bg-blue-600 text-white text-xs py-2 px-3 rounded">
          Check it out!
        </button>
        <button className="absolute top-2 right-2 text-gray-400">
          ×
        </button>
      </div>
      
      {/* Flight Options */}
      <div className="px-4 mt-6">
        <h3 className="font-semibold text-gray-800 mb-3">Flight Option For You</h3>
        <div className="flex space-x-4 overflow-x-auto pb-2">
          <div className="min-w-[150px] rounded-lg overflow-hidden shadow-sm">
            <div className="h-24 bg-gray-300 flex items-center justify-center text-gray-500">Image</div>
            <div className="p-2">
              <p className="text-xs font-semibold">Việt Nam - Phú Yên</p>
              <p className="text-xs text-yellow-500">⭐ ⭐ ⭐ ⭐ ⭐</p>
            </div>
          </div>
          <div className="min-w-[150px] rounded-lg overflow-hidden shadow-sm">
            <div className="h-24 bg-gray-300 flex items-center justify-center text-gray-500">Image</div>
            <div className="p-2">
              <p className="text-xs font-semibold">Tokyo - Kyoto</p>
              <p className="text-xs text-yellow-500">⭐ ⭐ ⭐ ⭐ ⭐</p>
            </div>
          </div>
        </div>
      </div>
      
      {/* Bottom Navigation */}
      <div className="fixed bottom-0 w-full max-w flex justify-around py-2 bg-white border-t border-gray-100">
        <div className="flex flex-col items-center text-blue-600 cursor-pointer">
          <div className="text-xl mb-1">🏠</div>
          <span className="text-xs">Home</span>
        </div>
        <div className="flex flex-col items-center text-gray-500 cursor-pointer">
          <div className="text-xl mb-1">✈️</div>
          <span className="text-xs">My Trip</span>
        </div>
        <div className="flex flex-col items-center text-gray-500 cursor-pointer">
          <div className="text-xl mb-1">📨</div>
          <span className="text-xs">Inbox</span>
        </div>
        <div className="flex flex-col items-center text-gray-500 cursor-pointer">
          <div className="text-xl mb-1">👤</div>
          <span className="text-xs">Account</span>
        </div>
      </div>
    </div>
  );
};
