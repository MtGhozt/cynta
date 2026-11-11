param(
  [string]$Initial = "",
  [string]$Title = "Elegir carpeta de salida — Cynta"
)

# Modern Explorer folder picker (IFileOpenDialog + FOS_PICKFOLDERS).
# Owned by a TopMost helper so it doesn't open behind the browser.
Add-Type -AssemblyName System.Windows.Forms | Out-Null
Add-Type -AssemblyName System.Drawing | Out-Null

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public static class CyntaNative {
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool BringWindowToTop(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, IntPtr processId);
  [DllImport("user32.dll")] public static extern bool AttachThreadInput(uint idAttach, uint idAttachTo, bool fAttach);
  [DllImport("kernel32.dll")] public static extern uint GetCurrentThreadId();
  [DllImport("user32.dll")] public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);
  [DllImport("user32.dll")] public static extern bool AllowSetForegroundWindow(int dwProcessId);
  public const int SW_RESTORE = 9;
  public const int SW_SHOW = 5;
  public const byte VK_MENU = 0x12;
  public const uint KEYEVENTF_KEYUP = 0x0002;
  public const int ASFW_ANY = -1;

  public static void ForceForeground(IntPtr hwnd) {
    AllowSetForegroundWindow(ASFW_ANY);
    IntPtr fg = GetForegroundWindow();
    uint fgThread = GetWindowThreadProcessId(fg, IntPtr.Zero);
    uint thisThread = GetCurrentThreadId();
    bool attached = false;
    if (fg != IntPtr.Zero && fgThread != thisThread) {
      attached = AttachThreadInput(thisThread, fgThread, true);
    }
    try {
      keybd_event(VK_MENU, 0, 0, UIntPtr.Zero);
      keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP, UIntPtr.Zero);
      ShowWindow(hwnd, SW_SHOW);
      BringWindowToTop(hwnd);
      SetForegroundWindow(hwnd);
    } finally {
      if (attached) {
        AttachThreadInput(thisThread, fgThread, false);
      }
    }
  }
}

public static class CyntaFolderPicker {
  [ComImport]
  [Guid("DC1C5A9C-E88A-4DDE-A5A1-60F82A20AEF7")]
  private class FileOpenDialogRCW {}

  [ComImport]
  [Guid("42f85136-db7e-439c-85f1-e4075d135fc8")]
  [InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  private interface IFileOpenDialog {
    [PreserveSig] int Show(IntPtr parent);
    void SetFileTypes(uint cFileTypes, IntPtr rgFilterSpec);
    void SetFileTypeIndex(uint iFileType);
    void GetFileTypeIndex(out uint piFileType);
    void Advise(IntPtr pfde, out uint pdwCookie);
    void Unadvise(uint dwCookie);
    void SetOptions(uint fos);
    void GetOptions(out uint pfos);
    void SetDefaultFolder(IShellItem psi);
    void SetFolder(IShellItem psi);
    void GetFolder(out IShellItem ppsi);
    void GetCurrentSelection(out IShellItem ppsi);
    void SetFileName([MarshalAs(UnmanagedType.LPWStr)] string pszName);
    void GetFileName([MarshalAs(UnmanagedType.LPWStr)] out string pszName);
    void SetTitle([MarshalAs(UnmanagedType.LPWStr)] string pszTitle);
    void SetOkButtonLabel([MarshalAs(UnmanagedType.LPWStr)] string pszText);
    void SetFileNameLabel([MarshalAs(UnmanagedType.LPWStr)] string pszLabel);
    void GetResult(out IShellItem ppsi);
    void AddPlace(IShellItem psi, int alignment);
    void SetDefaultExtension([MarshalAs(UnmanagedType.LPWStr)] string pszDefaultExtension);
    void Close(int hr);
    void SetClientGuid(ref Guid guid);
    void ClearClientData();
    void SetFilter(IntPtr pFilter);
    void GetResults(out IntPtr ppenum);
    void GetSelectedItems(out IntPtr ppsai);
  }

  [ComImport]
  [Guid("43826D1E-E718-42EE-BC55-A1E261C37BFE")]
  [InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  private interface IShellItem {
    void BindToHandler(IntPtr pbc, ref Guid bhid, ref Guid riid, out IntPtr ppv);
    void GetParent(out IShellItem ppsi);
    void GetDisplayName(uint sigdnName, out IntPtr ppszName);
    void GetAttributes(uint sfgaoMask, out uint psfgaoAttribs);
    void Compare(IShellItem psi, uint hint, out int piOrder);
  }

  [DllImport("shell32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
  private static extern int SHCreateItemFromParsingName(
    string pszPath, IntPtr pbc, ref Guid riid, out IShellItem ppv);

  [DllImport("ole32.dll")]
  private static extern void CoTaskMemFree(IntPtr pv);

  private const uint FOS_PICKFOLDERS = 0x00000020;
  private const uint FOS_FORCEFILESYSTEM = 0x00000040;
  private const uint FOS_PATHMUSTEXIST = 0x00000800;
  private const uint SIGDN_FILESYSPATH = 0x80058000;
  private static readonly Guid IID_IShellItem = new Guid("43826D1E-E718-42EE-BC55-A1E261C37BFE");

  public static string Pick(string title, string initialPath, IntPtr owner) {
    var dialog = (IFileOpenDialog)new FileOpenDialogRCW();
    dialog.SetOptions(FOS_PICKFOLDERS | FOS_FORCEFILESYSTEM | FOS_PATHMUSTEXIST);
    if (!string.IsNullOrWhiteSpace(title)) {
      dialog.SetTitle(title);
    }

    if (!string.IsNullOrWhiteSpace(initialPath)) {
      try {
        Guid iid = IID_IShellItem;
        IShellItem item;
        if (SHCreateItemFromParsingName(initialPath, IntPtr.Zero, ref iid, out item) == 0 && item != null) {
          dialog.SetFolder(item);
        }
      } catch { }
    }

    CyntaNative.ForceForeground(owner);
    int hr = dialog.Show(owner);
    if (hr != 0) {
      return null;
    }

    IShellItem result;
    dialog.GetResult(out result);
    IntPtr psz;
    result.GetDisplayName(SIGDN_FILESYSPATH, out psz);
    string path = Marshal.PtrToStringUni(psz);
    CoTaskMemFree(psz);
    return path;
  }
}
"@ -ErrorAction Stop

$owner = New-Object System.Windows.Forms.Form
$owner.Text = "Cynta"
$owner.TopMost = $true
$owner.ShowInTaskbar = $false
$owner.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::None
$owner.StartPosition = [System.Windows.Forms.FormStartPosition]::CenterScreen
$owner.Size = New-Object System.Drawing.Size(2, 2)
$owner.Opacity = 0.01
[void]$owner.Show()
[System.Windows.Forms.Application]::DoEvents()
[CyntaNative]::ForceForeground($owner.Handle)

try {
  $path = [CyntaFolderPicker]::Pick($Title, $Initial, $owner.Handle)
} finally {
  $owner.Close()
  $owner.Dispose()
}

if ([string]::IsNullOrWhiteSpace($path)) {
  exit 2
}
[Console]::Out.Write($path)
exit 0
