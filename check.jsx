function Login() {
  return (
    <div>
      <h2>Welcome Back</h2>

      <input type="email" placeholder="Email" />
      <br /><br />

      <input type="password" placeholder="Password" />
      <br /><br />

      <button>Login</button>

      <p>
        <a href="#">Forgot Password?</a>
      </p>
    </div>
  );
}

export default Login;