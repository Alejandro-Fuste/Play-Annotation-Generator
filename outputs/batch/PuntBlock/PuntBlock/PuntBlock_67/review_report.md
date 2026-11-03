# Play-Annotation-Generator Annotation Review — PuntBlock_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_67`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 209
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher5 | defense | `10` | `10` |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 0 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `19` | `19` | 1 | START | 1 | 1 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 29 | END | 29 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `6` | `6` | 53 | START | 53 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher5 | `10` | `10` | 65 | START | 65 | 70 |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector2 | `5` | `5` | 173 | START | 173 | 193 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 16 | 16 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_None` | 27 | 31 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 237 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 44 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 174 | 126 | inferred_complete_timeline |
| `Action_None` | 176 | 217 | 42 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 1 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 52 | 47 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_None` | 55 | 164 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 106 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_SecureRecovery` | 173 | 193 | 21 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 165 | 165 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_None` | 30 | 52 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 53 | 90 | 38 | inferred_complete_timeline |
| `Action_PuntBall` | 97 | 223 | 127 | inferred_complete_timeline |
| `Action_PuntBall` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 26 | 26 | inferred_complete_timeline |
| `Action_None` | 31 | 96 | 66 | inferred_complete_timeline |
| `Action_None` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_None` | 114 | 131 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 190 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 123 | 123 | inferred_complete_timeline |
| `Action_None` | 125 | 145 | 21 | inferred_complete_timeline |
| `Action_None` | 147 | 185 | 39 | inferred_complete_timeline |
| `Action_None` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_None` | 209 | 215 | 7 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 153 | 153 | inferred_complete_timeline |
| `Action_None` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 175 | 269 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BlockPunt` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_BlockPunt` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 122 | 48 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 19 | 19 | inferred_complete_timeline |
| `Action_None` | 21 | 107 | 87 | inferred_complete_timeline |
| `Action_None` | 159 | 169 | 11 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 196 | 196 | inferred_complete_timeline |
| `Action_None` | 198 | 207 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 121 | 121 | inferred_complete_timeline |
| `Action_None` | 123 | 132 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 219 | 219 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–269 | 230 | 9 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 46–269 | 203 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 48–198 | 133 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 95–131 | 34 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 106–269 | 162 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 115–269 | 141 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 116–218 | 87 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 122–194 | 58 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 124–143 | 20 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 141–170 | 17 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 146–222 | 69 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 160–269 | 90 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 176–269 | 87 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 191–269 | 79 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 192–269 | 78 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 198–203 | 6 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 217–224 | 8 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 218–269 | 45 | 2 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 242–269 | 28 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 248–265 | 15 | 2 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 250–269 | 20 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 250–269 | 20 | 1 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 254–269 | 13 | 2 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 261–266 | 6 | 1 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 261–267 | 6 | 2 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 262–265 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 131 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-196] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [53-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [97-223] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [65-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-26] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-111] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-121] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-185] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-165] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' for track '19' starts at frame 1, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_LongSnap' range [1-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [6-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [53-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-164] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-229] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-68] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-171] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-242] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-156] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-189] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-167] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-143] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-192] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-269] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '57' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.

</details>