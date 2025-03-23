import React from 'react'

const Navbar = () => {
  return (
    <div className="px-4 bg-base-300 py-3">
        <div className="flex justify-between items-center">
            <div className="left">
                <h2 className='font-bold cursor-pointer hover:text-secondary text-base-content' >TransitSync</h2>
            </div>
            <div className="middle flex gap-10">
                <h2 className='relative font-semibold cursor-pointer hover:text-secondary 
                before:w-0 before:transition-all hover:before:content-[""] hover:before:bottom-0 hover:before:absolute hover:before:w-full hover:before:h-0.5 hover:before:bg-secondary hover:before:right-0 hover:before:-my-0.5' >Home</h2>
                <h2 className='relative font-semibold cursor-pointer hover:text-secondary 
                before:w-0 before:transition-all hover:before:content-[""] hover:before:bottom-0 hover:before:absolute hover:before:w-full hover:before:h-0.5 hover:before:bg-secondary hover:before:right-0 hover:before:-my-0.5' >About us</h2>
                <h2 className='relative font-semibold cursor-pointer hover:text-secondary 
                before:w-0 before:transition-all hover:before:content-[""] hover:before:bottom-0 hover:before:absolute hover:before:w-full hover:before:h-0.5 hover:before:bg-secondary hover:before:right-0 hover:before:-my-0.5' >Destinations</h2>
                <h2 className='relative font-semibold cursor-pointer hover:text-secondary 
                before:w-0 before:transition-all hover:before:content-[""] hover:before:bottom-0 hover:before:absolute hover:before:w-full hover:before:h-0.5 hover:before:bg-secondary hover:before:right-0 hover:before:-my-0.5' >Contact Us</h2>
            </div>
            <div className="right">
                <button className="bg-base-100 btn border-none hover:bg-secondary hover:text-secondary-content">Plan Your Trip</button>
            </div>
        </div>
    </div>
  )
}

export default Navbar
