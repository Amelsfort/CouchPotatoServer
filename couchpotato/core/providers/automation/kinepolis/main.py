from couchpotato.core.logger import CPLog
from couchpotato.core.providers.automation.base import Automation

log = CPLog(__name__)


class Kinepolis(Automation):

    def getMovies(self):

        if self.isDisabled():
            return

        return []
