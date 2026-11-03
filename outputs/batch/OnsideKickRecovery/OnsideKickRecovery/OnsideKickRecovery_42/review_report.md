# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 173
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 0
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Right_Coverage4 | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage4 | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | `19` | `19` | 6 | START | 6 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Position_Unknown | `19` | `19` | 45 | START | 45 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Right_Coverage4 | `8` | `8` | 101 | START | 101 | 112 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage4 | `8` | `8` | 150 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 22 | 17 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 22 | 17 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_None` | 42 | 53 | 12 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 112 | 29 | inferred_complete_timeline |
| `Action_None` | 118 | 163 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 49 | 44 | inferred_complete_timeline |
| `Action_None` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 108 | 21 | inferred_complete_timeline |
| `Action_None` | 115 | 127 | 13 | inferred_complete_timeline |
| `Action_None` | 142 | 155 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 41 | 36 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 159 | 32 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 16 | 11 | inferred_complete_timeline |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 38 | 33 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 123 | 127 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 75 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 125 | 35 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 75 | 70 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 170 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 77 | 72 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 156 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 174 | 169 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 53 | 48 | inferred_complete_timeline |
| `Action_None` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 95 | 90 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 74 | 69 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 108 | 103 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 143 | 27 | inferred_complete_timeline |
| `Action_None` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 139 | 134 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 145 | 140 | inferred_complete_timeline |
| `Action_None` | 147 | 167 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–78 | 71 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 5–171 | 126 | 9 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 26–180 | 127 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 43–180 | 101 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 53–98 | 37 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 81–172 | 13 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 85–145 | 44 | 7 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 96–125 | 14 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 99–103 | 5 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 109–163 | 36 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 134–171 | 17 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 149–177 | 29 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 152–166 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_KickBall` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `8` (Right_Coverage4)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 153 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '8' has invalid range: start=150, end=127. Clamping end to start.
- ⚠️ Action 'Action_None' range [6-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-174] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-74] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-77] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-41] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-159] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-75] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-44] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [101-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [123-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-16] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-125] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-38] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-53] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-163] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-49] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-108] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-32] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-38] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-108] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-65] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [6-20] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [26-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [45-77] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [80-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [98-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [101-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [141-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [166-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-64] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-98] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-145] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-107] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>