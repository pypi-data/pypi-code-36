from typing import List, Optional


class WeightedMeter:
    def __init__(self, name: str, fmt=':.2f'):
        self.name = name
        self.count = 0
        self.sum = 0.0
        self.avg = 0.0
        self.val = 0.0
        self.fmt = fmt

    def update(self, val: float, num: int = 1):
        self.count += num
        self.sum += val * num
        self.avg = self.sum / self.count
        self.val = val

    def __str__(self):
        return ('{name} {val' + self.fmt + '} ({avg' + self.fmt + '})').format(**self.__dict__)


class AverageMeter:
    def __init__(self, name: str, length: int, fmt=':.2f'):
        assert length > 0
        self.name = name
        self.count = 0
        self.sum = 0.0
        self.fmt = fmt
        self.current: int = -1
        self.history: List[Optional[float]] = [None] * length

    @property
    def val(self) -> float:
        return self.history[self.current]

    @property
    def avg(self) -> float:
        return self.sum / self.count

    def update(self, val: float):
        self.current = (self.current + 1) % len(self.history)
        self.sum += val

        old = self.history[self.current]
        if old is None:
            self.count += 1
        else:
            self.sum -= old
        self.history[self.current] = val

    def __str__(self):
        return ('{name} {val' + self.fmt + '} ({avg' + self.fmt + '})').format(
            name=self.name,
            val=self.val,
            avg=self.avg
        )


class ProgressMeter:
    def __init__(self, total_steps: int, total_epochs: int, fmt=':.1f'):
        self.step = 0
        self.fmt = fmt
        self.total_steps = total_steps
        self.total_epochs = total_epochs

    def update(self, step: int):
        self.step = step

    @property
    def ratio(self):
        return self.step / self.total_steps

    def __str__(self):
        return ('Step {step}/{total_steps}={ratio' + self.fmt + '}% ({epoch}/{total_epochs})').format(
            step=self.step,
            total_steps=self.total_steps,
            ratio=self.ratio * 100,
            epoch=int(self.total_epochs * self.ratio),
            total_epochs=self.total_epochs
        )
