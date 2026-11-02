# Play-Annotation-Generator Annotation Review — JetSweep_146

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `JetSweep_146`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 179
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | C | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | C | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_JetMotion` | C | `2` | `1` | 2 | START | 2 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 37 | START | 37 | 48 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `2` | `1` | 37 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 37 | START | 37 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 54 | END | 54 | 54 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 58 | START | 58 | 60 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | C | `2` | `1` | 68 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_Toss` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 31 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 97 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 207 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 130 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 48 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 2 | 31 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 81 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 84 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 72 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 141 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 182 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 18 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 42 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 120 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 176 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 140 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 205 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | Position_Unknown | Team_Unknown | 42–156 | 99 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 43–55 | 13 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 44–125 | 80 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 44–57 | 14 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 46–102 | 10 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 51–117 | 58 | 6 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 55–126 | 64 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 60–239 | 167 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 61–145 | 72 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 61–189 | 100 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 74–204 | 127 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 86–239 | 143 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 91–102 | 12 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 96–152 | 51 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 104–201 | 95 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 115–223 | 91 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 121–124 | 4 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 148–227 | 80 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 149–239 | 91 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 151–239 | 69 | 8 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 165–239 | 74 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 170–239 | 60 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 176–225 | 39 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 196–239 | 39 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `2` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 35 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 118 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 293: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ZoneBlock' for track '1' has invalid range: start=37, end=31. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=68, end=31. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [2-31] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-130] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-205] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [58-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-81] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-18] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-42] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-72] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-141] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-77] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-146] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-125] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-108] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-174] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-75] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-82] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-148] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-204] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-114] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-102] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-105] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-195] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-124] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-137] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-189] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-124] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-227] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-162] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-196] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-231] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-191] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-226] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-239] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-225] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-220] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>