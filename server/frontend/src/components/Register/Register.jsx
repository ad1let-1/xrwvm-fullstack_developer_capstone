import React, { useState } from 'react';

export default function Register() {
  const [form, setForm] = useState({ userName: '', firstName: '', lastName: '', email: '', password: '' });
  const [message, setMessage] = useState('');
  const update = (event) => setForm({ ...form, [event.target.name]: event.target.value });
  const submit = async (event) => {
    event.preventDefault();
    const response = await fetch('/djangoapp/register', {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(form)
    });
    const result = await response.json();
    setMessage(response.ok ? `Welcome, ${result.userName}!` : result.error || 'Registration failed');
  };
  return <main className="register-page">
    <h1>Sign up for Best Cars</h1>
    <form onSubmit={submit}>
      <label>Username<input name="userName" placeholder="Username" value={form.userName} onChange={update} required /></label>
      <label>First Name<input name="firstName" placeholder="First Name" value={form.firstName} onChange={update} required /></label>
      <label>Last Name<input name="lastName" placeholder="Last Name" value={form.lastName} onChange={update} required /></label>
      <label>Email<input name="email" type="email" placeholder="email" value={form.email} onChange={update} required /></label>
      <label>Password<input name="password" type="password" placeholder="Password" value={form.password} onChange={update} required minLength={8} /></label>
      <button type="submit">Register</button>
    </form>
    <p role="status">{message}</p>
  </main>;
}
