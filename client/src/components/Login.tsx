import React, { useState } from "react";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = (e: any) => {
        e.preventDefault();
        alert(`Logging in with:\nEmail: ${email}\nPassword: ${password}`);
    };

    const handleGoogleLogin = () => {
        alert("Google Login (dummy) clicked");
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
            <div className="bg-white p-8 rounded shadow-md w-full max-w-sm">
                <h2 className="text-2xl font-bold mb-6 text-center text-base-100">Login</h2>
                <div></div>
                <form onSubmit={handleLogin} className="space-y-4">
                    <div className="flex flex-col text-base-100">
                        <h2>Username</h2>
                        <input
                            type="email"
                            placeholder="Enter Username"
                            className="w-full p-2 border border-gray-300 rounded"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div className="flex flex-col text-base-100">
                        <h2>Password</h2>
                    <input
                        type="password"
                        placeholder="Enter Password"
                        className="w-full p-2 border border-gray-300 rounded"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
                    >
                        Login
                    </button>
                </form>

                <div className="my-4 text-center text-gray-500">OR</div>

                <button
                    onClick={handleGoogleLogin}
                    className="w-full bg-white border border-gray-300 flex items-center justify-center gap-2 p-2 rounded hover:bg-gray-100"
                >
                    <img
                        src="https://www.svgrepo.com/show/475656/google-color.svg"
                        alt="Google"
                        className="w-5 h-5"
                    />
                    <span className="text-base-100 ">Login with Google</span>
                </button>
            </div>
        </div>
    );
}
