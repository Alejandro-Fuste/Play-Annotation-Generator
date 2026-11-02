# Play-Annotation-Generator Annotation Review — JetSweep_187

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_187`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | RB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 42 | START | 42 | 106 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 78 | START | 78 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | `8` | `7` | 79 | START | 79 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 79 | START | 79 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `16` | 79 | START | 79 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 79 | START | 79 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 79 | START | 79 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 79 | START | 91 | 204 |
| ✅ EXACT | `Action_SnapReceive` | RB | `9` | `8` | 90 | END | 78 | 90 |
| ✅ EXACT | `Action_Toss` | RB | `9` | `8` | 96 | START | 96 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `2` | 107 | START | 107 | 191 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 216 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 220 | 143 | inferred_complete_timeline |
| `Action_None` | 223 | 299 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_Toss` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_None` | 107 | 258 | 152 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 278 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_JetMotion` | 42 | 106 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 191 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 270 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 121 | 43 | inferred_complete_timeline |
| `Action_LeadBlock` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_LeadBlock` | 170 | 216 | 47 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 225 | 148 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 211 | 133 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 251 | 10 | inferred_complete_timeline |
| `Action_None` | 258 | 267 | 10 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 216 | 104 | inferred_complete_timeline |
| `Action_None` | 217 | 227 | 11 | inferred_complete_timeline |
| `Action_None` | 230 | 236 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 204 | 114 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 143 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 133 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 216 | 63 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 183 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 98 | 21 | inferred_complete_timeline |
| `Action_None` | 112 | 226 | 115 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 156 | 79 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 137 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 213 | 136 | inferred_complete_timeline |
| `Action_None` | 216 | 226 | 11 | inferred_complete_timeline |
| `Action_None` | 229 | 251 | 23 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 179 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 198 | 121 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 286 | 70 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 274 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 271 | 194 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 120–299 | 180 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 145–165 | 6 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 173–221 | 45 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 198–279 | 78 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 199–299 | 98 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 235–299 | 64 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 265–299 | 31 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '7' (TE1) duration 138 frames exceeds threshold 90 frames [start=79, end=216].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 138 frames exceeds threshold 90 frames [start=79, end=216].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 138 frames exceeds threshold 90 frames [start=79, end=216].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 138 frames exceeds threshold 90 frames [start=79, end=216].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 138 frames exceeds threshold 90 frames [start=79, end=216].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [78–90], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_None' range [78-213] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-270] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [79-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [123-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-258] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-225] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-226] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-207] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
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

</details>