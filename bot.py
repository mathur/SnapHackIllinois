from snap.snapchat_bots import SnapchatBot

class HackIllinoisBot(SnapchatBot):

  def initialize(self):
    """initialize the bot by creating a queue of received snaps"""
    self.queue = self.get_snaps(mark_viewed=False)

  def on_snap(self, sender, snap):
    """Add snap to review queue when received"""
    self.queue.append(snap)
    #self.post_story(snap)

  def on_friend_add(self, friend):
    """Add friends back automatically"""
    self.add_friend(self, friend)
    print friend

  def get_num_friends(self):
    """Return the number of friends the bot has"""
    return len(self.get_friends())

