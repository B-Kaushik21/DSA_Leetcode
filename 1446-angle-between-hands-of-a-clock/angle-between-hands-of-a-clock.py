class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle=minutes*6
        hour=hour%12
        h_angle=(hour*30)+(minutes*0.5)
        angle=abs(h_angle-m_angle)
        return min(angle,360-angle)
