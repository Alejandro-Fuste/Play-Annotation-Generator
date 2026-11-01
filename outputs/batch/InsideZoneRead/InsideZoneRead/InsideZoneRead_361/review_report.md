# Play-Annotation-Generator Annotation Review — InsideZoneRead_361

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_361`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 162
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 26 | START | 26 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 29 | START | 40 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 29 | START | 29 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 29 | START | 29 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `20` | 29 | START | 29 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 39 | END | 26 | 39 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 47 | START | 47 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `9` | `8` | 54 | START | 54 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 68 | START | 68 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_Keep` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_Keep` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 205 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 213 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 84 | 59 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 124 | 99 | inferred_complete_timeline |
| `Action_None` | 130 | 220 | 91 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 69 | 44 | inferred_complete_timeline |
| `Action_None` | 72 | 219 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 71 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 87 | 110 | 24 | inferred_complete_timeline |
| `Action_None` | 130 | 204 | 75 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 86 | 1 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 155 | 31 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 222 | 17 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 86 | 58 | inferred_complete_timeline |
| `Action_None` | 87 | 123 | 37 | inferred_complete_timeline |
| `Action_None` | 127 | 155 | 29 | inferred_complete_timeline |
| `Action_None` | 157 | 164 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 78 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 63 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 108 | 83 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 158 | 14 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 58 | 33 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 110 | 85 | inferred_complete_timeline |
| `Action_None` | 112 | 168 | 57 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 196 | 18 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 67 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 196 | 171 | inferred_complete_timeline |
| `Action_None` | 198 | 221 | 24 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 82 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 12–82 | 39 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 73–239 | 122 | 11 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 135–239 | 99 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 161–209 | 31 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 172–174 | 3 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 183–186 | 4 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 184–229 | 33 | 5 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 184–192 | 9 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 187–229 | 27 | 6 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 189–212 | 9 | 3 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 200–222 | 11 | 3 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 204–213 | 4 | 2 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 209–222 | 11 | 2 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 213–221 | 6 | 2 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 218–229 | 4 | 2 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `40` | `68` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `41` | `70` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `42` | `73` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–39], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=40.
- ⚠️ Action 'Action_None' range [26-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-239] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-219] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-221] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [54-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-61] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-155] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-108] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-230] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
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

</details>