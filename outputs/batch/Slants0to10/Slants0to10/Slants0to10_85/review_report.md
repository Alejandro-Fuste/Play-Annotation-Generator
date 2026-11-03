# Play-Annotation-Generator Annotation Review — Slants0to10_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_85`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | QB | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE2 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `14` | `14` | 3 | START | 3 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 3 | START | 3 | 26 |
| ✅ EXACT | `Action_PassBlock` | C | `16` | `16` | 3 | START | 3 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 3 | START | 3 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 3 | START | 3 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | QB | `13` | `13` | 10 | START | 10 | 46 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `13` | `13` | 10 | END | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 47 | START | 47 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE2 | `17` | `17` | 90 | START | 90 | 149 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 10 | 46 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_None` | 81 | 299 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 268 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 299 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 78 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 149 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 263 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 274 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 276 | 282 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 26 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 299 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 26 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 74 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 138 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 299 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 23 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 26 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 41 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 85 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 299 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 299 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 25 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 60 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 299 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 52 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 299 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 299 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–299 | 287 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 17–72 | 53 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–299 | 242 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 47–67 | 21 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 54–83 | 14 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 84–93 | 10 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 116–299 | 52 | 10 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 119–299 | 181 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 125–299 | 175 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 146–299 | 153 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 155–299 | 145 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 161–178 | 17 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 197–202 | 6 | 1 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 284–296 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunSlantRoute` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `13` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 86: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Overlapping action conflict at frame 10 for track '13': 'Action_SnapReceive' vs 'Action_RunSlantRoute'. Overriding with 'Action_RunSlantRoute'.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-60] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-268] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-299] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-52] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-74] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-138] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-42] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [276-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-72] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-131] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-121] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-236] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-237] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-178] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-296] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>