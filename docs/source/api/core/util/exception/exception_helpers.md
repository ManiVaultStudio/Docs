# Exception presentation helpers

The overloads below show a modal error dialog for a reason, standard exception, or `ManiVaultException`. Use them only at the GUI boundary that consumes the failure.

```{doxygenfunction} mv::util::exceptionMessageBox(const QString&, const QString&, QWidget*)
```

```{doxygenfunction} mv::util::exceptionMessageBox(const QString&, const std::exception&, QWidget*)
```

```{doxygenfunction} mv::util::exceptionMessageBox(const QString&, const ManiVaultException&, QWidget*)
```
