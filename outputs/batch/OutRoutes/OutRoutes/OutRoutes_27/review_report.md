# Play-Annotation-Generator Annotation Review — OutRoutes_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_27`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | WR2 | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | WR2 | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | CB3 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 18 |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | `18` | `18` | 14 | START | 33 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 14 | START | 14 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 14 | START | 14 | 14 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | `21` | `21` | 14 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 14 | START | 47 | 48 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `11` | `11` | 14 | START | 14 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 19 | END | 19 | 19 |
| ✅ EXACT | `Action_ThrowPass` | WR2 | `11` | `11` | 61 | START | 61 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | WR2 | `11` | `11` | 90 | START | 90 | 153 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | CB3 | `4` | `4` | 99 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_None` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunOutRoute` | 14 | 60 | 47 | inferred_complete_timeline |
| `Action_ThrowPass` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 89 | 20 | inferred_complete_timeline |
| `Action_SecureCatch` | 90 | 153 | 64 | inferred_complete_timeline |
| `Action_SecureCatch` | 160 | 171 | 12 | inferred_complete_timeline |
| `Action_SecureCatch` | 181 | 200 | 20 | inferred_complete_timeline |
| `Action_SecureCatch` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 31 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 43 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 35 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 245 | 159 | inferred_complete_timeline |
| `Action_PassBlock` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–14
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 14 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 241 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 41 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 78 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 260 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 78 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–200 | 196 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 91–269 | 176 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 97–269 | 162 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 99–212 | 82 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 99–211 | 92 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 103–202 | 100 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 103–239 | 130 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 105–161 | 57 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 113–269 | 157 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 117–206 | 87 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 118–122 | 5 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 130–209 | 67 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 142–203 | 62 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `18` (LG): Annotated start 14 != Inferred start 33
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `11` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (CB3)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=99, end=78. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '21' has invalid range: start=14, end=7. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-71] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-78] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [90-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [160-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [181-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-41] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-121] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '19' starts at frame 14, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [14-16] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-41] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-83] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-245] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '20' starts at frame 14, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [14-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-244] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-253] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-108] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-239] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-206] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-122] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-147] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>