# Play-Annotation-Generator Annotation Review — JetSweep_188

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_188`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `8` | `7` | 37 | START | 37 | 81 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `20` | 53 | START | 63 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE1 | `2` | `1` | 54 | START | 54 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 54 | START | 54 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 54 | START | 54 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 54 | START | 54 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 54 | START | 54 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 61 | END | 53 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 79 | START | 79 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `8` | `7` | 82 | START | 94 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_None` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_Toss` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 122 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 200 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 124 | 67 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_JetMotion` | 37 | 81 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 102 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 153 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_LeadBlock` | 54 | 87 | 34 | inferred_complete_timeline |
| `Action_LeadBlock` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_LeadBlock` | 146 | 146 | 1 | inferred_complete_timeline |
| `Action_None` | 147 | 194 | 48 | inferred_complete_timeline |
| `Action_None` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 71 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 146 | 93 | inferred_complete_timeline |
| `Action_None` | 147 | 164 | 18 | inferred_complete_timeline |
| `Action_None` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 81 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 100 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 146 | 45 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 94 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 85 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_None` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 147 | 38 | inferred_complete_timeline |
| `Action_None` | 157 | 172 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 106 | 54 | inferred_complete_timeline |
| `Action_None` | 108 | 139 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_None` | 79 | 204 | 126 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 68 | 16 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 90 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 81 | 29 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 83 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 98 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 199 | 147 | inferred_complete_timeline |
| `Action_None` | 204 | 260 | 57 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 104 | 52 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 165 | 52 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 63–269 | 206 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 74–142 | 53 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 87–179 | 88 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 91–104 | 5 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 103–117 | 15 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 122–156 | 35 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 126–135 | 8 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 128–269 | 73 | 5 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 136–169 | 31 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 136–269 | 131 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 136–140 | 5 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 137–239 | 85 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 148–153 | 6 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 155–262 | 97 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 172–203 | 32 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 201–269 | 69 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 216–235 | 13 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 243–256 | 14 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 258–269 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 53 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '1' (TE1) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=63, end=61. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [54-85] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [54-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [90-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-194] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [37-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-104] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-178] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-262] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '41' has 1 frames without a visible bounding box.
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

</details>