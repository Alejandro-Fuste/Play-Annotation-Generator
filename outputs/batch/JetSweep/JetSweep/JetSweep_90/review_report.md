# Play-Annotation-Generator Annotation Review — JetSweep_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_90`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `9` | `8` | 41 | START | 41 | 93 |
| ✅ EXACT | `Action_BallSnap` | RG | `22` | `21` | 68 | START | 68 | 70 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `17` | `16` | 71 | START | 71 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `15` | 71 | START | 71 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 71 | START | 71 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 71 | START | 71 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 71 | START | 71 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 71 | START | 71 | 72 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 76 | END | 68 | 76 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 84 | START | 84 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `9` | `8` | 94 | START | 94 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_Toss` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_None` | 94 | 299 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 218 | 151 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_JetMotion` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 172 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 186 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 299 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_LeadBlock` | 71 | 133 | 63 | inferred_complete_timeline |
| `Action_None` | 134 | 169 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 125 | 55 | inferred_complete_timeline |
| `Action_None` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 185 | 206 | 22 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 248 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 106 | 39 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 193 | 62 | inferred_complete_timeline |
| `Action_None` | 196 | 222 | 27 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_None` | 258 | 275 | 18 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 247 | 180 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 117 | 50 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 299 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 169 | 102 | inferred_complete_timeline |
| `Action_None` | 176 | 189 | 14 | inferred_complete_timeline |
| `Action_None` | 192 | 219 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 125 | 58 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 166 | 205 | 40 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 236 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 299 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 249 | 182 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 128–299 | 169 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 143–299 | 156 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 143–299 | 156 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 143–299 | 135 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 145–299 | 149 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 145–299 | 152 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 177–299 | 120 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 184–284 | 88 | 6 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 217–228 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [68-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-222] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-247] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-186] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-159] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 68, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [68-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-248] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-189] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-250] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-284] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-228] for track '34' has 1 frames without a visible bounding box.
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

</details>