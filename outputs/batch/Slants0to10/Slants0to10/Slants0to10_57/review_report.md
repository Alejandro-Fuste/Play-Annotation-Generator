# Play-Annotation-Generator Annotation Review — Slants0to10_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_57`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 165
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DE1 | defense | `7` | `7` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | DE1 | defense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 0 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DE1 | `7` | `7` | 1 | START | N/A | N/A |
| ✅ EXACT | `Action_PassBlock` | C | `11` | `11` | 4 | START | 4 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `12` | `12` | 4 | START | 4 | 4 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `13` | `13` | 4 | START | N/A | N/A |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `10` | `10` | 10 | START | 10 | 86 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `7` | `7` | 10 | END | 1 | 10 |
| ✅ EXACT | `Action_ThrowPass` | DE1 | `7` | `7` | 57 | START | 57 | 68 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `10` | `10` | 93 | START | 93 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 44 | 44 | inferred_complete_timeline |
| `Action_None` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_None` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 111 | 111 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 10 | 86 | 77 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 239 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 25 | 25 | inferred_complete_timeline |
| `Action_None` | 30 | 38 | 9 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 46 | 95 | 50 | inferred_complete_timeline |
| `Action_None` | 97 | 239 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–14
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 14 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 4 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 20 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 25 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 73 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 90 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 56 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 69 | 177 | 109 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 6 | 6 | inferred_complete_timeline |
| `Action_None` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 47 | 84 | 38 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 222 | 111 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 91 | 91 | inferred_complete_timeline |
| `Action_None` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 128 | 128 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 143 | 143 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 15–84 | 64 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 29–64 | 23 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 29–239 | 191 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 31–122 | 92 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 39–100 | 48 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 42–62 | 9 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 42–70 | 19 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 42–239 | 114 | 7 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 53–239 | 179 | 5 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 56–126 | 37 | 3 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 68–81 | 8 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 116–239 | 122 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 139–239 | 97 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 149–239 | 75 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 151–239 | 86 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 156–167 | 8 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 157–239 | 81 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 163–239 | 60 | 6 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 180–239 | 59 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 185–239 | 47 | 6 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `7` (DE1)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (6 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `13` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 57: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '13' has invalid range: start=4, end=1. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-177] for track '7' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-84] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '12' starts at frame 4, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [4-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-90] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-35] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-84] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-84] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-134] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-178] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-147] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-221] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-239] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-196] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>