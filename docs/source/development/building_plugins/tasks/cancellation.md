# Cancellation and abort behavior

Task cancellation is cooperative. Setting `mayKill` exposes cancellation controls, but pressing one does not stop a thread or roll back partial output. It causes the task to enter its abort sequence and emit `Task::requestAbort()`. The operation must observe that request, stop at a safe boundary, clean up, and finally call `setAborted()`.

```cpp
class Operation : public QObject
{
public:
    Operation() : _task(this, "Processing items", mv::Task::Status::Undefined, true)
    {
        connect(&_task, &mv::Task::requestAbort, this, [this]() {
            _abortRequested.store(true, std::memory_order_relaxed);
        });
    }

    void runOnWorker(const Items& items)
    {
        _abortRequested.store(false, std::memory_order_relaxed);
        _task.setRunning();

        for (std::size_t index = 0; index < items.size(); ++index) {
            if (_abortRequested.load(std::memory_order_relaxed)) {
                discardPartialResult();
                _task.setAborted();
                return;
            }

            process(items[index]);
            _task.setProgress(static_cast<float>(index + 1) / items.size());
        }

        _task.setFinished();
    }

private:
    std::atomic_bool  _abortRequested{false};
    mv::ForegroundTask _task;
};
```

The cancellation flag and task must outlive the connection and any worker that uses them. Operation-owned state avoids a stack variable disappearing while asynchronous work continues.

## Cancellation contract

For every killable operation, define:

- where cancellation is checked;
- which calls cannot be interrupted;
- whether partially produced data is discarded or remains valid;
- who changes the task from `Aborting` to `Aborted`;
- whether child operations also receive the request.

Keep checks frequent enough for a responsive interface, but only stop where invariants can be restored. Never terminate a worker thread forcibly.

`kill()` requests cancellation recursively by default. It does not mean cancellation has completed. Code that must wait for cleanup should observe `statusChangedToAborted()` or the operation's own completion result.

## Cancellation is not failure

Use `Aborted` only when the user or owning operation requested cancellation. An exception, invalid input, or unavailable resource is a failure and must retain its diagnostic information separately. Conversely, a normal cancellation should usually not be presented as an error.
