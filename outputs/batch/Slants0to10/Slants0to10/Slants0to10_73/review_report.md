# Play-Annotation-Generator Annotation Review — Slants0to10_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_73`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 188
- **Validation Warnings:** 245
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 163
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_RunSlantRoute` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | CB3 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 194 |
| ✅ EXACT | `Action_PassBlock` | RT | `13` | `13` | 3 | START | 3 | 22 |
| ✅ EXACT | `Action_PassBlock` | RG | `15` | `15` | 3 | START | 3 | 22 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 3 | START | 3 | 27 |
| ✅ EXACT | `Action_PassBlock` | C | `2` | `2` | 3 | START | 3 | 3 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 3 | START | 3 | 22 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 3 | END | 3 | 3 |
| ✅ EXACT | `Action_RunSlantRoute` | C | `2` | `2` | 4 | START | 4 | 74 |
| ✅ EXACT | `Action_ThrowPass` | CB3 | `11` | `11` | 45 | START | 45 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `2` | `2` | 83 | START | 83 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 246 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 259 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 190 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 27 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 22 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 219 | 78 | inferred_complete_timeline |
| `Action_PassBlock` | 223 | 265 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 4 | 74 | 71 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 118 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 158 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 199 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 22 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 22 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 52 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 169 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 197 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 118 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 130 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ThrowPass` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 53 | 128 | 76 | inferred_complete_timeline |
| `Action_None` | 156 | 172 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 193 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 144 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 168 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–111 | 77 | 10 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 3–22 | 20 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 66–269 | 186 | 8 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 83–268 | 112 | 11 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 93–122 | 30 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 94–266 | 99 | 9 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 107–269 | 118 | 8 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 121–130 | 9 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 125–269 | 137 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 133–269 | 128 | 6 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 134–137 | 4 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 135–269 | 121 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 149–269 | 90 | 5 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 153–269 | 97 | 3 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 153–269 | 78 | 6 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 153–252 | 68 | 5 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 153–156 | 4 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 156–268 | 51 | 9 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 162–168 | 7 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 175–180 | 6 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 198–206 | 7 | 2 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 199–219 | 17 | 3 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 203–226 | 13 | 4 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 208–258 | 15 | 4 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 239–242 | 4 | 1 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 240–243 | 4 | 1 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 263–268 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF3` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 169 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 73: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-52] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-158] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-246] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-118] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-130] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-169] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-219] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [223-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-22] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-106] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-252] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-122] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-148] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-208] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-139] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-184] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-221] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-142] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-184] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-199] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-193] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-235] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-170] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-158] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-171] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-211] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-231] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-241] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-213] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-235] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-252] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-191] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-240] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-268] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-168] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-180] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-226] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-213] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-251] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-237] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>