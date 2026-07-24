# SSH Push to GitHub

## 1. Generate a key pair

Make sure you're in the `.ssh` folder:

```bash
cd ~/.ssh
```

Create the key pair:

```bash
ssh-keygen -t ed25519 -a 100 -C "kyram-ngoma@tech610-work-laptop"
```

- **Name for key:** `tech610-kyram-gh-key`
- Press **Enter** twice to leave the passphrase empty

## 2. Add the public key to GitHub

1. Click your profile picture on GitHub
2. Go to **Settings** → **SSH and GPG keys**
3. Click **New SSH key**
4. **Title:** `tech610-kyram-gh-key`
5. **Key type:** Authentication Key
6. Get the public key contents:
   ```bash
   cat tech610-kyram-gh-key.pub
   ```
7. Copy and paste the full output into the **Key** field — it must start with `ssh-ed25519`:
   ```
   ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXX kyram-ngoma@tech610-work-laptop
   ```

## 3. Register the private key with the SSH agent

```bash
eval "$(ssh-agent -s)"
ssh-add tech610-kyram-gh-key
```

Test the connection:

```bash
ssh -T git@github.com
```

Expected output:

```
Hi Kyram6! You've successfully authenticated, but GitHub does not provide shell access.
```

## 4. Create a test repo

Move out of `.ssh` and into your GitHub working folder (going into `Learning/` first is optional):

```bash
cd ~/Github
mkdir tech610-test-ssh
cd tech610-test-ssh
```

Then:

```bash
git init
echo "# tech610-test-ssh" >> README.md
git branch -M main
git remote add origin git@github.com:Kyram6/tech610-test-ssh.git
git add .
git commit -m "add readme with title"
git push --set-upstream origin main
```

> Note: use the **SSH** remote URL (`git@github.com:...`), not HTTPS, since this setup relies on the SSH key.